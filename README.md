# Intelligence artificielle pour Handberton

# AI-pour-Handberton

This project integrates AI features into a robotic hand using TensorFlow 2 and Keras. The robotic hand is controlled via a web interface, and it responds to various commands using a neural network for intent recognition.

## Directory Structure

AI-pour-Handberton/
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
    python neural_network.py
	or ./neural_network.py
    ```

3. **Run the Flask Server**:
    ```sh
    python app.py
	or ./app.py
    ```

4. **Open the Web Interface**:
    Open `handberton-website-proto.html` in a web browser.

## Usage

Enter commands into the web interface to control the robotic hand. The recognized intents will be processed, and the corresponding actions will be sent to the Arduino to control the hand's movements.

---------------------

#NOTE - please make these changes

----
Connect Arduino to computer

ls ls /dev/tty*

--------
Update the hand_control.py after connecting the arduino 

--

replace

# Use the MockArduino class instead of serial.Serial
arduino = MockArduino()

def send_to_arduino(command):
    arduino.write(command + '\n')
    time.sleep(0.1)

--

with

# Establish a serial connection to the Arduino

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)



def send_to_arduino(command):

    arduino.write(bytes(command + '\n', 'utf-8'))

    time.sleep(0.1)

----

verify serial communication

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    if (command == "finger1:open") {
      digitalWrite(LED_BUILTIN, HIGH); // Turn the LED on
    } else if (command == "finger1:close") {
      digitalWrite(LED_BUILTIN, LOW); // Turn the LED off
    }
    // Add more commands as needed
  }
}

-------

test it

./hand_control.py

if the test is successful, update the app.py with the changes:
line 1 from flask import Flask, request, jsonify, send_from_directory
line 7: app = Flask(__name__, static_url_path='')
line 18: 
@app.route('/')

def index():

    return send_from_directory('', 'handberton-website-proto.html')


-------------------------



pip install tensorflow pandas scikit-learn nltk
pip install pyserial

AI features to the robotic hand using Tensorflow 2 and Keras. 

The index number of thumb is 1 , index number of the index finger is 2, of the middle is 3, of the ring is 4, and of the pinky is 5. The string variable of thumb is "thumb" , index number "index", of the middle is "middle", the ring is "ring", and of the pinky is "pinky". 

The Flex sensor is for each finger is between 10Ω ( when a finger is closed) to 30/50Ω (and when a finger is fully extended)


The AI receives instructions through a chat interface where the user inputs the command and the finger's shoud respond automatically.

Here are the list of commands:

Intent: countdown (n) seconds. 
Funtion: Performs a coutdown for n seconds starting from index 1. All fingers remain closed at the beginning and fingers gets extended one by one as per the value of n, staring from index 1 (thumb)
Note: n ranges from 1 to 5

Intent: (nb) +/-/*/÷ (nb) = (nb) 
Funtion: Performs a calculatins between n variables. All fingers remain closed at the beginning and starting from index 1, the fingers which have the value upto the index number which is of the same value as the result (nb), will open while the rest remain closed. If reslt n is equal to zeo all fingers will remain partially open.
Note: nb ranges from 0 to 5

Intent: Raise the (x) finger
Function: Raises finger which has the corresponds to the string variable of x . All fingers remain closed at the beginning
Note: x is a string variable that stands for any of the four values: "thumb" , "index" , "middle" , "ring" , "pinky"

Intent: Respond "yes" with only the thumb raised or the index finger raised questions.
All fingers remain closed at the begining. Only Thumb raises if the answer is yes whereas whereas all other fingers remain closed or will close if they are not. If the answer is no, Only the index raises if the answer is no whereas whereas all other fingers remain closed or will close if they are not.
Question string: "Are you a robot ?"
Answer : yes
Question string: "Do you have AI ?"
Answer : yes
Question string : "Are you a threat ?"
Answer : no

Intent: rock n roll.
Function: All fingers remain closed. Only the index and middle fingers are raised

Intent: "hello"
Function: all fingers will open

Intent: "goodbye"
Function: all fingers will close.
