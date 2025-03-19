import torch
import cv2
import numpy as np
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Motor

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Use 'yolov5s' or custom-trained model

# Initialize webcam or external camera
cap = cv2.VideoCapture(0)

# Define motor control
motor_left = Motor(forward=17, backward=18)
motor_right = Motor(forward=22, backward=23)
propeller = Motor(forward=17, backward=27)
belt = Motor(forward=22, backward=23)

# Function to move robot forward
def move_forward():
    motor_left.forward()
    motor_right.forward()

# Function to stop robot
def stop_robot():
    motor_left.stop()
    motor_right.stop()

# Function to collect trash
def collect_trash():
    print("Activating collection mechanism")
    # Code to activate collection mechanism (e.g., servo/motorized arm)
    sleep(2)  # Simulate collection time

# Wrap main content in a try block to catch user pressing CTRL-C
# and run GPIO cleanup function.
try:
    # Create Infinite loop to read user input
    while True:
        # Get user Input
        user_input = input()

        if user_input == 'w':
            propeller.forward()
            belt.forward()
            print("Forward")

        elif user_input == 's':
            propeller.backward()
            belt.backward()
            print('Back')

        elif user_input == 'd':
            propeller.forward()
            belt.backward()
            print('Right')

        elif user_input == 'a':
            propeller.backward()
            belt.forward()
            print('Left')

        # Press 'c' to stop the motors
        elif user_input == 'c':
            propeller.stop()
            belt.stop()
            print('Stop')

except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()
    print("GPIO Clean up")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform object detection
    results = model(frame)
    
    # Parse detection results
    detections = results.xyxy[0].cpu().numpy()
    for *box, conf, cls in detections:
        label = results.names[int(cls)]
        if label == "bottle" or label == "plastic":  # Detect trash items
            x1, y1, x2, y2 = map(int, box)
            
            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Move towards trash and collect
            move_forward()
            sleep(1)
            stop_robot()
            collect_trash()
    
    # Display output
    cv2.imshow('Trash Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
stop_robot()
