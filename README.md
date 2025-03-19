AI-Powered Robotic Trash Collector

Project Overview

This project is an AI-powered robotic system designed to detect and collect floating trash in water bodies using YOLOv5 for object detection. The system integrates a Raspberry Pi with motors, a propeller, and a conveyor belt to autonomously navigate and collect waste.

Features

Real-time Object Detection: Uses YOLOv5 to identify floating trash (e.g., plastic bottles).

Autonomous Navigation: Moves towards detected trash and activates collection mechanism.

User Control Mode: Allows manual movement via keyboard inputs.

Motor Control: Uses GPIO to drive motors and control the collection system.

Live Camera Feed: Displays detected trash with bounding boxes.

Hardware Requirements

Raspberry Pi (with GPIO support)

Camera Module (Raspberry Pi Camera or USB Webcam)

Motors (for navigation and collection mechanism)

Propeller & Conveyor Belt System

Power Supply & Supporting Electronics

Software Requirements

Python 3.10

OpenCV

PyTorch

GPIOZero

RPi.GPIO

Installation

Clone the repository:

https://github.com/Sriharibvrsh077/Aquabot-trash-collector
cd Aquabot-trash-collector

Install dependencies:

pip install torch torchvision opencv-python numpy gpiozero

Enable Raspberry Pi camera (if using Pi Camera):

sudo raspi-config

Navigate to Interfacing Options > Enable Camera

Reboot the Raspberry Pi

Usage

Start AI-powered detection and collection:

python main.py

Manual control using keyboard inputs:

w → Move forward

s → Move backward

a → Turn left

d → Turn right

c → Stop motors

CTRL+C → Exit program and clean up GPIO

How It Works

The camera continuously captures video feed.

YOLOv5 detects floating trash in the water.

If trash is detected:

The robot moves towards it.

The conveyor belt activates to collect the trash.

Users can manually control movement if needed.

The live video feed displays detected trash with bounding boxes.

Future Improvements

Upgrade YOLOv5 model for better accuracy.

Improve navigation with GPS or ultrasonic sensors.

Implement remote monitoring via a mobile/web app.

Optimize power consumption for long-term operation.

Contributing

Feel free to contribute by submitting issues, pull requests, or feature enhancements!

License

This project is licensed under the MIT License.

Developed by Srihari and Sahiti 🚀

