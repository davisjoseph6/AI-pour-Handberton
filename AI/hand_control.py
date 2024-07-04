#!/usr/bin/env python3

import time
from mock_arduino import MockArduino

# Use the MockArduino class instead of serial.Serial
arduino = MockArduino()

def send_to_arduino(command):
    arduino.write(command + '\n')
    time.sleep(0.1)

def reset_fingers():
    for i in range(1, 6):
        send_to_arduino(f'finger{i}:close')
    time.sleep(0.5)

def countdown(seconds):
    for i in range(1, 6):
        send_to_arduino(f'finger{i}:close')
    for i in range(1, seconds + 1):
        send_to_arduino(f'finger{i}:open')
        time.sleep(1)
        send_to_arduino(f'finger{i}:close')

def calculate(expression):
    try:
        result = eval(expression.replace('÷', '/'))
        result = round(result) if 0 <= result <= 5 else 0
        for i in range(1, 6):
            if i <= result:
                send_to_arduino(f'finger{i}:open')
            else:
                send_to_arduino(f'finger{i}:close')
    except Exception as e:
        print(f"Error in calculation: {e}")

def raise_finger(finger):
    finger_map = {"thumb": 1, "index": 2, "middle": 3, "ring": 4, "pinky": 5}
    finger_index = finger_map.get(finger, 0)
    if finger_index:
        send_to_arduino(f'finger{finger_index}:open')

def respond_to_question(question):
    if question in ["Are you a robot?", "Do you have AI?"]:
        send_to_arduino('finger1:open')  # Thumb
    elif question == "Are you a threat?":
        send_to_arduino('finger2:open')  # Index

def rock_n_roll():
    for i in range(1, 6):
        send_to_arduino(f'finger{i}:close')
    send_to_arduino('finger2:open')  # Index
    send_to_arduino('finger3:open')  # Middle

def hello():
    for i in range(1, 6):
        send_to_arduino(f'finger{i}:open')

def goodbye():
    for i in range(1, 6):
        send_to_arduino(f'finger{i}:close')

if __name__ == "__main__":
    # Example usage
    goodbye()

