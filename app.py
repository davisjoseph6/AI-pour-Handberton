#!/usr/bin/env python3

import sys
sys.path.append('./AI')  # Add this line to include the AI directory in the module search path

from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import pickle
import re
from hand_control import countdown, calculate, raise_finger, respond_to_question, rock_n_roll, hello, goodbye

app = Flask(__name__)

# Load the trained model and vectorizer
model = load_model('AI/intent_recognition_model_v2.h5')
with open('AI/vectorizer_v2.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('AI/intent_to_label_v2.pkl', 'rb') as f:
    intent_to_label = pickle.load(f)

label_to_intent = {v: k for k, v in intent_to_label.items()}

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.json
    command = data['command']
    
    X = vectorizer.transform([command]).toarray()
    prediction = model.predict(X)
    intent_label = prediction.argmax()
    intent = label_to_intent[intent_label]

    if intent == 'countdown':
        seconds = int(re.search(r'\d+', command).group())
        countdown(seconds)
    elif intent == 'calculate':
        expression = re.findall(r'(\d+ \+ \d+|\d+ - \d+|\d+ \* \d+|\d+ ÷ \d+)', command)[0]
        calculate(expression)
    elif intent == 'raise_finger':
        finger = command.split(' ')[2]
        raise_finger(finger)
    elif intent == 'respond_to_question':
        respond_to_question(command)
    elif intent == 'rock_n_roll':
        rock_n_roll()
    elif intent == 'hello':
        hello()
    elif intent == 'goodbye':
        goodbye()

    return jsonify({'intent': intent, 'command': command})

if __name__ == '__main__':
    app.run(debug=True)

