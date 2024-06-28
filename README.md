# Machine Learning model for Arduino

This project integrates AI features into a robotic hand (Arduino) using TensorFlow 2 and Keras. The robotic hand is controlled via a web interface, and it responds to various commands using a deep neural network for intent recognition. 

Reuse of prexisting models through Transfer learning or use of data sets for training purposes was avoided, to solidify foundations of Deep Learning processes and architecures.

---

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
    Navigate to http://localhost:8000 in a web browser.

5. **Click `Connect to Arduino`**


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


   arduino = serial.Serial('/dev/tty.usbmodem101', 9600, timeout=1)  # Update the port as necessary

   def send_to_arduino(command):
       arduino.write((command + '\n').encode())
       time.sleep(0.1)
  ```

- Ensure Ensure the serial port `/dev/ttyUSB0` is correct. 

   ```sh
   ls /dev/tty*
  ```

- Identify the correct port for your Arduino (it could be /dev/ttyUSB0, /dev/ttyACM0, etc.) and update the serial.Serial line in `hand_control.py` accordingly.

- Update `app.py` if necessary

- (Optional) Verify serial communication: 
	- Upload a simple Arduino sketch to your Arduino board to verify the communication. This sketch will send and receive data over the serial port.
	- Upload the Sketch
	- Test Communication Using a Serial Monitor
	- Verify Serial Communication

### Improving the AI model's accuracy

- If everything works well, retraining of the Deep Learning model `neural_network.py` with more larger data to improve the accuracy of the predictions.

---

### Questions to ask the AI

Here's a comprehensive list of intents with specifics and details for each intent. These intents are recognized by the intent recognition model and the corresponding actions they trigger in the hand control system.

#### Intents and their Specifics
1. **countdown**
- Description: Starts a countdown where each second is indicated by the movement of fingers.
- Example Commands:
	- "countdown 5 seconds"
	- "countdown 3 seconds"
	- "countdown 1 second"
- Action: Each second, a finger is opened and closed in sequence.

2. **calculate**
- Description: Evaluates a simple arithmetic expression and indicates the result using finger movements.
- Example Commands:
	- "calculate 2 + 3"
	- "calculate 4 * 5"
	- "calculate 6 - 2"
- Action: The result is shown by opening a corresponding number of fingers (up to 5).

3. **raise_finger**
- Description: Raises a specified finger.
- Example Commands:
	- "raise the thumb finger"
	- "raise the index finger"
- Action: The specified finger is raised (opened).

4. **respond_to_question**
- Description: Responds to predefined questions by moving specific fingers.
- Example Commands:
	- "Are you a robot?"
	- "Do you have AI?"
	- "Are you a threat?"
- Action: Moves a specific finger (thumb for "yes" responses, index for "no" responses).

5. **rock_n_roll**
- Description: Performs a "rock n roll" gesture.
- Example Commands:
	- "rock n roll"
- Action: Closes all fingers and opens the index and middle fingers.

6. **hello**
- Description: Performs a waving gesture as a greeting.
- Example Commands:
	- "hello"
- Action: Opens all fingers.

7. **goodbye**
- Description: Closes all fingers as a farewell gesture.
- Example Commands:
	- "goodbye"
	- "bye bye"
- Action: Closes all fingers.

#### Command Processing
- countdown: Extracts the number of seconds from the command and calls the countdown(seconds) function.
- calculate: Extracts the arithmetic expression from the command and calls the calculate(expression) function.
- raise_finger: Extracts the finger name from the command and calls the raise_finger(finger) function.
- respond_to_question: Identifies the question from the command and calls the respond_to_question(question) function.
- rock_n_roll: Calls the rock_n_roll() function.
- hello: Calls the hello() function.
- goodbye: Calls the goodbye() function.

## About the Project:

AI features to the robotic hand using Tensorflow 2 and Keras. The index number of thumb is 1 , index number of the index finger is 2, of the middle is 3, of the ring is 4, and of the pinky is 5. The string variable of thumb is "thumb" , index number "index", of the middle is "middle", the ring is "ring", and of the pinky is "pinky". The value for the Flex sensor is for each finger is between 10Ω (when a finger is closed) to 30/50Ω (and when a finger is fully extended). The AI receives instructions through a chat interface where the user inputs the command and the finger's shoud respond automatically.

### Implementation Details
Intent Recognition Model
- Model Architecture:
	- Input Layer: Dense layer with 128 units and ReLU activation.
	- Hidden Layers: Dense layers with 64 and 32 units with ReLU activation.
	- Output Layer: Dense layer with softmax activation for intent classification.
	- Dropout Layer: Dropout rate of 0.5 for regularization.
- Data Preparation:
	- Commands are tokenized and vectorized using TF-IDF.
	- Intent labels are encoded as categorical values.
	- Data is split into training and testing sets.
Flask API
- Endpoint: /process_command
- Request: JSON payload with the command.
- Response: JSON with the predicted intent and the original command.
- Processing:
	- Transforms the command using the loaded vectorizer.
	- Predicts the intent using the loaded model.
	- Executes the corresponding hand control function based on the predicted intent.
This setup allows the system to understand a range of commands, classify them into predefined intents, and perform specific actions with the robotic hand accordingly.

## Authors

The AI model, features and their integration were designed and developed by a team of robotics, machine learning, and backend engineers at [Holberton School Paris](https://www.holbertonschool.fr/campus/paris) . 

Members of the team:

- Robotics engineer: [Maël Cuny](https://github.com/maelpseudo)
- Machine Learning engineer: [Saber Cherif](https://github.com/hakun0) 
- Backend and Database engineer: [Alfred Gibeau--Ahoussinou](https://github.com/alfredgibeau-ahoussinou)

Advisors, Consultants and sponsors:

- Machine Learning and Deep Learning Consultant: [Davis Joseph](https://github.com/davisjoseph6)
