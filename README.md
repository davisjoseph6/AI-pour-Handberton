# Artificial Inteligence Model for Handberton (Arduino)

This project integrates AI features into a robotic hand (Arduino) using TensorFlow 2 and Keras. The robotic hand is controlled via a web interface, and it responds to various commands using a neural network for intent recognition.

## Directory Structure

AI for Handberton/
│
├── AI/
│ ├── intent_recognition_model.h5
│ ├── intent_recognition_model_v2.h5
│ ├── intent_to_label.pkl
│ ├── intent_to_label_v2.pkl
│ ├── neural_network.py
│ ├── vectorizer.pkl
│ ├── vectorizer_v2.pkl
│ ├── hand_control.py
│
├── handberton-website-proto.html
├── README.md
├── requirements.txt
├── app.py

## Setup Instructions.

1. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

2. **Train the Neural Network**:
    ```sh
    cd AI
    ./neural_network.py
    ```

3. **Run the Flask Server**:
    ```sh
    ./app.py
    ```

4. **Open the Web Interface**:
    Navigate to `http://localhost:8000` in a web browser.

5. **Click Connect to Arduino**


## Usage

Enter commands into the web interface to control the robotic hand. The recognized intents will be processed, and the corresponding actions will be sent to the Arduino to control the hand's movements.

---

# NOTE:


1. For now, it works well with the mock signal. A few changes required before testing with actual Arduino.

2. The AI Deep Learning model works but it needs to be trained more as it still makes mistakes. More testing and training data is required for the model.


## Resume of changes to be made

### Before testing it with the real Arduino

- Manually connect Arduino to computer


   ```sh
   ls /dev/tty*
  ```

- Update the `hand_control.py`  


   ```sh
   #!/usr/bin/env python3

   import time
   import serial


   arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Update the port as necessary

   def send_to_arduino(command):
       arduino.write((command + '\n').encode())
       time.sleep(0.1)
  ```

- Ensure Ensure the serial port `/dev/ttyUSB0` is correct. 

   ```sh
   ls /dev/tty*
  ```

- Identify the correct port for your Arduino (it could be /dev/ttyUSB0, /dev/ttyACM0, etc.) and update the serial.Serial line in `hand_control.py` accordingly.

- Update app.py if necessary

- (Optional) Verify serial communication: 
	- Upload a simple Arduino sketch to your Arduino board to verify the communication. This sketch will send and receive data over the serial port.
	- Upload the Sketch
	- Test Communication Using a Serial Monitor
	- Verify Serial Communication

### Improving the AI model's accuracy

- If everything works well, retraining of the Deep Learning model `neural_network.py` with more larger data to improve the accuracy of the predictions.

---

## The AI Project Objectives:

AI features to the robotic hand using Tensorflow 2 and Keras. 

The index number of thumb is 1 , index number of the index finger is 2, of the middle is 3, of the ring is 4, and of the pinky is 5. The string variable of thumb is "thumb" , index number "index", of the middle is "middle", the ring is "ring", and of the pinky is "pinky". 

The value for the Flex sensor is for each finger is between 10Ω (when a finger is closed) to 30/50Ω (and when a finger is fully extended).

The AI receives instructions through a chat interface where the user inputs the command and the finger's shoud respond automatically.

Here are the list of commands:

- Intent: countdown (n) seconds.
- Funtion: Performs a coutdown for n seconds starting from index 1. All fingers remain closed at the beginning and fingers gets extended one by one as per the value of n, staring from index 1 (thumb)
- Note: n ranges from 1 to 5

- Intent: (nb) +/-/*/÷ (nb) = (nb) 
- Funtion: Performs a calculatins between n variables. All fingers remain closed at the beginning and starting from index 1, the fingers which have the value upto the index number which is of the same value as the result (nb), will open while the rest remain closed. If reslt n is equal to zeo all fingers will remain partially open.
- Note: nb ranges from 0 to 5

- Intent: Raise the (x) finger
- Function: Raises finger which has the corresponds to the string variable of x . All fingers remain closed at the beginning
- Note: x is a string variable that stands for any of the four values: "thumb" , "index" , "middle" , "ring" , "pinky"

- Intent: Respond "yes" with only the thumb raised or the index finger raised questions.
- All fingers remain closed at the begining. Only Thumb raises if the answer is yes whereas whereas all other fingers remain closed or will close if they are not. If the answer is no, Only the index raises if the answer is no whereas whereas all other fingers remain closed or will close if they are not.
- Question string: "Are you a robot ?"
- Answer : yes
- Question string: "Do you have AI ?"
- Answer : yes
- Question string : "Are you a threat ?"
- Answer : no

- Intent: rock n roll.
- Function: All fingers remain closed. Only the index and middle fingers are raised

- Intent: "hello"
- Function: all fingers will open

- Intent: "goodbye"
- Function: all fingers will close.
