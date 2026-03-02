# CS350-thermostat-controller
Thermostat controller final project and AHT20 temperature/humidity sensor integration.
This repository includes two CS-350 (Emerging System Architectures and Technologies) portfolio artifacts that demonstrate the fundamentals of embedded systems: GPIO input/output, I2C sensor integration, LCD output, and state-driven program design.

## Artifact 1 (Primary): Thermostat Controller Final Project
What it is: A thermostat-style controller that reads environmental data, displays system status on an LCD screen, and uses buttons to adjust a set point. LEDs indicate heating/cooling based on current conditions and temperature conditions.
## Demo video: https://youtu.be/9B7xl2bdMHM

Note on feedback and validation: In instructor feedback, the video demonstrated solid red and blinking blue, and the buttons changing the set point, but did not fully demonstrate blinking red (heater running) or solid blue (cooling on but not currently running). In my final validation workflow, I use a short checklist to trigger and verify each required state (including “on but not running” vs “running” indicators) before recording the demo.
## Artifact 2 (Option B): Temperature + Humidity Sensor Integration (AHT20 over I2C)
What it is: A clean sensor integration that reads temperature/humidity from an AHT20 via I2C, displays readings on a 16x2 LCD, and uses a button press to toggle between Celsius and Fahrenheit.

## Key features:
•	 Uses I2C (board.SCL, board.SDA) with the AHTx0 driver to read temperature and relative humidity

•	 The LCD screen updates row 1 with the formatted measurement and row 2 with the date/time every 0.5 seconds

•	 Uses a GPIO button (BCM24) to toggle between devices (C/F)

•	 Verification steps to confirm the sensor is on the I2C bus at address 0x38: ls /dev/i2c* and sudo i2cdetect -y 

# Module Eight Journal Reflection
## Summarize the project and what problem it was solving
These artifacts demonstrate the construction of an embedded-style system on a Raspberry Pi that integrates multiple hardware components and interfaces: LCD output, button input, and sensor communication. The “problem” being solved is to create a reliable, testable control-style application (thermostat) that reads real-world data, presents it clearly to the user, and responds to user input with predictable state-driven behavior.
## What did you do particularly well?
I performed particularly well at systematic troubleshooting and integration. When the behavior was no longer consistent during full integration, I took a structured approach by breaking the component down, checking the GPIO pin map against the lab guide, checking power/ground, checking device detection via the I2C bus, and gradually building back up. On the code side, I took a pure loop/state-driven approach and used output to verify button presses and state changes.
## Where could you improve?
I can improve how I validate and demonstrate requirements under time pressure, especially during recordings. For example, feedback on the final demo noted missing visual confirmation for specific LED states (“running” vs “on but not running”). Going forward, I will use a short demo checklist that forces each required condition before recording so that all rubric elements are clearly demonstrated.
## What tools and/or resources are you adding to your support network?
I am adding a more formal support/verification workflow: wiring validation checklists, consistent I2C verification steps (device detection and address confirmation), and a simple test script/checklist for triggering each state transition and LED condition prior to submission. I will continue using lab guides/rubrics as requirement references and use targeted debug output to confirm runtime behavior.
## What skills from this project will be particularly transferable to other projects and/or coursework?
### Transferable skills include:
•	Hardware/software integration (GPIO input/output + I2C sensor communication)

•	Debugging discipline (baseline → isolate → test one change → verify)

•	State-machine and loop-based design for predictable system behavior

•	Clear validation practices (observable outputs through LCD/LED + sensor detection checks)

These apply directly to future embedded projects and any system that requires reliable integration and troubleshooting.
## How did you make this project maintainable, readable, and adaptable?
I kept the project maintainable by using a structured approach that separates responsibilities (sensor reads, display updates, and input handling) and by using clear naming and predictable control flow. The sensor integration uses a dedicated display wrapper and a small, readable loop to update the LCD and respond to a button toggle, which makes it easy to extend (additional sensors, new display formats, different update rates) without rewriting the full program.
## Repository Contents
•	TemperatureSensorIntegration.py (Artifact 2: AHT20 + LCD + button toggle)

•	Adding a Temperature and Humidity Sensor.docx (Artifact 2 write-up) 
