#!/usr/bin/env python3
#
# TemperatureSensorIntegration.py
#
# Integrate AHT20 temp/humidity sensor with the 16x2 LCD
# and existing button. Button toggles between C and F.

import time
from datetime import datetime

import board
import busio
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import adafruit_ahtx0

from gpiozero import Button


# -----------------------------
# LCD wrapper (matches Milestone 3 wiring)
# -----------------------------

class ManagedDisplay:
    def __init__(self):
        # GPIO pin mapping for the LCD (BCM numbering via board module)
        self.lcd_rs = digitalio.DigitalInOut(board.D17)
        self.lcd_en = digitalio.DigitalInOut(board.D27)
        self.lcd_d4 = digitalio.DigitalInOut(board.D5)
        self.lcd_d5 = digitalio.DigitalInOut(board.D6)
        self.lcd_d6 = digitalio.DigitalInOut(board.D13)
        self.lcd_d7 = digitalio.DigitalInOut(board.D26)

        # 16x2 display
        self.lcd_columns = 16
        self.lcd_rows = 2

        # Create LCD object
        self.lcd = characterlcd.Character_LCD_Mono(
            self.lcd_rs,
            self.lcd_en,
            self.lcd_d4,
            self.lcd_d5,
            self.lcd_d6,
            self.lcd_d7,
            self.lcd_columns,
            self.lcd_rows,
        )

        # Clear screen on startup
        self.lcd.clear()

    def clear(self):
        self.lcd.clear()

    def update(self, line1: str, line2: str = ""):
        """
        Update both lines of the LCD.
        Lines longer than 16 chars are truncated.
        """
        line1 = line1[:16]
        line2 = line2[:16]
        self.lcd.clear()
        self.lcd.message = f"{line1}\n{line2}"

    def cleanup(self):
        # Clear display and release pins
        self.lcd.clear()
        self.lcd_rs.deinit()
        self.lcd_en.deinit()
        self.lcd_d4.deinit()
        self.lcd_d5.deinit()
        self.lcd_d6.deinit()
        self.lcd_d7.deinit()


# -----------------------------
# Main program
# -----------------------------

# Button on BCM 24 (same as Milestone 3)
BUTTON_PIN = 24


def main():
    # I2C for AHT20
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_ahtx0.AHTx0(i2c)

    # LCD and button
    display = ManagedDisplay()
    button = Button(BUTTON_PIN, pull_up=True)

    # Start in Celsius mode
    use_celsius = True

    def toggle_units():
        nonlocal use_celsius
        use_celsius = not use_celsius

    # Toggle C/F whenever button is pressed
    button.when_pressed = toggle_units

    try:
        display.update("Temp Sensor Demo", "Initializing...")
        time.sleep(2)

        while True:
            # Read sensor
            temp_c = sensor.temperature          # degrees C
            humidity = sensor.relative_humidity  # %

            # Convert if needed
            if use_celsius:
                temp_value = temp_c
                unit = "C"
            else:
                temp_value = temp_c * 9.0 / 5.0 + 32.0
                unit = "F"

            # Format line 1: "T:23.4C H:45.2%"
            line1 = f"T:{temp_value:4.1f}{unit} H:{humidity:4.1f}%"

            # Line 2: date/time
            now = datetime.now()
            # Example: "02/20 14:35"
            line2 = now.strftime("%m/%d %H:%M")

            display.update(line1, line2)

            # Update 2x per second 
            time.sleep(0.5)

    except KeyboardInterrupt:
        # Allow clean exit with Ctrl+C
        pass
    finally:
        display.cleanup()


if __name__ == "__main__":
    main()