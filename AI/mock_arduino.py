#!/usr/bin/env python3


# mock_arduino.py

class MockArduino:
    def __init__(self):
        self.commands = []

    def write(self, command):
        print(f"Mock write to Arduino: {command.strip()}")
        self.commands.append(command.strip())

    def read_commands(self):
        return self.commands

