# CS-350 Temperature and Humidity Sensor Integration

Temperature and humidity sensor integration artifact for CS-350.

This repository includes a CS-350 embedded systems project that demonstrates hardware/software integration using GPIO input, I2C sensor communication, LCD output, and Python-based control logic on a Raspberry Pi.

## Artifact: AHT20 Sensor and LCD Integration

This project integrates an AHT20 temperature/humidity sensor with a 16x2 LCD display. The application reads real-world temperature and humidity data over I2C, displays the readings on the LCD, and uses a GPIO button to toggle the temperature display between Celsius and Fahrenheit.

This project was part of a larger CS-350 thermostat controller sequence involving embedded systems concepts such as GPIO, I2C communication, LCD output, state-driven behavior, and hardware/software troubleshooting.

## Demo Video

[Demo video](https://youtu.be/uvZeKR94jVU)

## Project Overview

The goal of this project was to build and validate embedded-style functionality on a Raspberry Pi. The application reads sensor data from an AHT20 temperature/humidity sensor, formats the output, displays readings on a 16x2 LCD, and responds to user input through a physical GPIO button.

The project demonstrates how software can interact with external hardware components to create a reliable and testable embedded system.

## Features

- Reads temperature and humidity from an AHT20 sensor
- Communicates with the sensor over I2C
- Displays live sensor data on a 16x2 LCD
- Uses a GPIO button to toggle Celsius/Fahrenheit output
- Updates the display with sensor readings and timestamp information
- Includes cleanup logic for LCD GPIO resources
- Demonstrates Raspberry Pi hardware/software integration

## Hardware Used

- Raspberry Pi 4B
- AHT20 temperature/humidity sensor
- 16x2 LCD display
- GPIO push button
- Breadboard and jumper wires

## Technologies Used

- Python 3
- Raspberry Pi GPIO
- I2C communication
- Adafruit CircuitPython libraries
- gpiozero
- LCD display control

## Repository Contents

- `TemperatureSensorIntegration.py`: Main sensor and LCD integration script
- `Adding a Temperature and Humidity Sensor.docx`: Project documentation
- `README.md`: Repository documentation
- `LICENSE`: MIT license
- `.gitignore`: Git ignore configuration

## How It Works

1. The Raspberry Pi initializes the I2C connection.
2. The AHT20 sensor provides temperature and humidity readings.
3. The LCD displays formatted temperature, humidity, and timestamp data.
4. A GPIO button toggles the temperature display between Celsius and Fahrenheit.
5. The program refreshes the LCD continuously until stopped by the user.
6. On exit, the program clears the LCD and releases GPIO resources.

## Skills Demonstrated

- Python programming for hardware-integrated systems
- Embedded systems fundamentals
- Raspberry Pi hardware integration
- GPIO input handling
- I2C sensor communication
- LCD display output
- Hardware/software troubleshooting
- Requirements-based validation
- Technical documentation

## Written Reflection

### Summarize the Project and What Problem It Was Solving

This artifact demonstrates the construction of an embedded-style sensor integration system on a Raspberry Pi that connects multiple hardware components: LCD output, button input, and I2C sensor communication.

The problem being solved is to create a reliable, testable application that reads real-world temperature and humidity data, presents it clearly to the user, and responds to user input with predictable behavior.

### What Did You Do Particularly Well?

I performed particularly well at implementing clear hardware/software requirements and validating behavior through structured integration.

I built the system around explicit sensor communication, LCD output, GPIO button input, timed display updates, and cleanup logic. I also used repeatable test sequences to verify sensor readings, display behavior, and button-driven temperature unit changes.

### Where Could You Improve?

I can improve how I validate and demonstrate requirements under time pressure, especially during recordings or final project checks.

Going forward, I would use a short checklist that verifies each required behavior before submission, including sensor detection, LCD output, Celsius/Fahrenheit toggling, timestamp updates, and proper cleanup when the program exits.

### What Tools and/or Resources Are You Adding to Your Support Network?

I am adding a more formal verification workflow that includes wiring validation checklists, consistent I2C verification steps such as device detection and address confirmation, and repeatable test scripts/checklists for confirming sensor readings, LCD behavior, and GPIO button input.

I will continue using lab guides and rubrics as requirement references and use targeted debug output to confirm runtime behavior.

### What Skills From This Project Will Be Particularly Transferable to Other Projects and/or Coursework?

Transferable skills include:

- Hardware/software integration using GPIO input, I2C sensor communication, and LCD output
- Debugging discipline using a baseline, isolate, test one change, and verify process
- Loop-based design for predictable embedded behavior
- Validation practices using observable hardware outputs
- Technical documentation for hardware-integrated software

These skills apply directly to future embedded projects, IoT development, QA testing, software support, and any system that requires reliable integration and troubleshooting.

### How Did You Make This Project Maintainable, Readable, and Adaptable?

I kept the project maintainable by separating responsibilities such as sensor reads, LCD updates, button handling, and cleanup behavior.

This structure makes it easier to extend the project with additional thermostat features, alternate sensors, different display formats, or expanded state-driven behavior without rewriting the entire program.

## Future Improvements

- Add full thermostat OFF / HEAT / COOL state logic
- Add set-point adjustment buttons
- Add heating and cooling LED indicators
- Add UART telemetry output
- Add a state-machine diagram
- Organize the project into `src/`, `docs/`, and `media/` folders
- Add a `requirements.txt` file
