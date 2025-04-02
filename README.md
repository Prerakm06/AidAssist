# AidAssist

## Introduction
* AidAssist is a first-aid guidance device designed to provide immediate medical instructions for common injuries.
* This project was developed for the HOSA Medical Innovation Competition, where our team placed in the top 15.
* AidAssist utilizes a **Raspberry Pi**, **LCD display**, and **GPIO inputs** to allow users to navigate through first-aid instructions.
* This project is for **educational and non-commercial use** only.
* Please read through all documentation before starting this project.

![AidAssist Prototype](./images/aidassist_prototype.png)

## Features
* Guides users through medical procedures for various injuries using an LCD display.
* Uses **physical buttons** to navigate through instructions.
* Provides **step-by-step** assistance for injuries such as cuts, burns, fractures, and more.

## Known Issues and Limitations
* The device does not provide emergency medical services and should not replace professional medical assistance.
* The LCD screen may have readability issues under **direct sunlight**.
* The response time for button presses may experience slight delays.

## Bill of Materials
* Below is a list of required components to assemble AidAssist.

### Required Items
Qty | Item Description | Notes
--- | --- | ---
1 | Raspberry Pi (any model with GPIO support) | Used to control the system.
1 | 16x2 LCD Display | Displays first-aid instructions.
2 | Push Buttons | For user navigation.
1 | 5V Power Supply | Required to power the Raspberry Pi.
1 | GPIO Wires | Used to connect components.
1 | Enclosure (3D printed or custom) | Protects the device.

## Software Setup
1. Ensure you have **Raspberry Pi OS** installed on your device.
2. Install required Python libraries:
   ```sh
   pip install RPi.GPIO
Copy the aidassist.py script onto the Raspberry Pi.

Connect the LCD display and buttons to the GPIO pins according to the circuit diagram.

Code Overview
The AidAssist software is written in Python and utilizes the RPi.GPIO library. Below is a brief explanation of the key functions:

python
Copy
Edit
import RPi.GPIO as GPIO
import drivers
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup([26, 21], GPIO.IN)
GPIO.setup(4, GPIO.OUT)
display = drivers.Lcd()
display.lcd_clear()

injuries = ["Head Injury", "Cut", "Burn", "Eye Injury", "Nosebleed", "Fractures", "Splinter"]

instructions = {
    "Head Injury": ["1. Control bleeding: Apply pressure with cloth",
                    "2. Clean wound: Use sterile gauze",
                    "3. Apply sterile dressing to cover",
                    "4. Apply cold compress to reduce swelling",
                    "5. Seek medical help if severe",
                    "Finished"]
}

while True:
    display.lcd_display_string("Select an Injury:", 1)
    display.lcd_display_string(injuries[0], 2)

    if GPIO.input(26) == 1:
        display.lcd_clear()
        choice = injuries[0]
        for step in instructions[choice]:
            display.lcd_display_string(step, 2)
            time.sleep(2)
Soldering and Installation
Wire all components on a breadboard for initial testing.

Ensure button presses register properly in the software.

Once confirmed, solder all components onto a PCB or permanent board.

Mount the system inside an enclosure to protect the components.

Operation
Power on the AidAssist device.

Use the navigation buttons to scroll through the injury list.

Select an injury, and the device will display step-by-step first-aid guidance.

Follow the instructions displayed on the LCD screen.

Future Improvements
Integrate a voice assistant to read out instructions.

Improve power efficiency by using a battery pack.

Add a touchscreen interface for easier navigation.

Acknowledgments
This project was inspired by real-world first-aid needs and aims to assist individuals in emergency situations.

Developed by the AidAssist Team for the HOSA Medical Innovation Competition.

vbnet
Copy
Edit

This Markdown file is formatted for GitHub and will display correctly when copied into a `.md` file. Let me know if you need any modifications! 🚀
