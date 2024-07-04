#!/usr/bin/env python3


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import nltk
import pickle

nltk.download('punkt')

# Step 1: Define the Model
def create_model(input_shape):
    model = Sequential()
    model.add(Dense(256, input_shape=input_shape, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(len(intents), activation='softmax'))  # Adjusted based on the number of intents

    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Step 2: Data Preparation
# Define the intents
intents = [
    "countdown",
    "calculate",
    "raise_finger",
    "respond_to_question",
    "rock_n_roll",
    "hello",
    "goodbye"
]

# Create a mapping of intents to labels
intent_to_label = {intent: idx for idx, intent in enumerate(intents)}

# Sample commands and corresponding intents
data = {
    'command': [
        'countdown 5 seconds',
        'countdown 3 seconds',
        'countdown 1 second',
        'countdown 10 seconds',
        'calculate 2 + 3',
        'calculate 4 * 5',
        'calculate 6 - 2',
        'calculate 8 / 4',
        'raise the thumb finger',
        'raise the index finger',
        'Are you a robot?',
        'Do you have AI?',
        'Are you a threat?',
        'rock n roll',
        'hello',
        'goodbye',
        'bye bye',
        'start a countdown of 7 seconds',
        'compute 5 + 7',
        'what is 8 * 6',
        'please calculate 9 - 4',
        'show the thumb finger',
        'show the index finger',
        'are you an AI robot?',
        'do you possess artificial intelligence?',
        'should I be worried about you?',
        'let us rock n roll',
        'say hello',
        'say goodbye',
        'farewell'
    ],
    'intent': [
        'countdown',
        'countdown',
        'countdown',
        'countdown',
        'calculate',
        'calculate',
        'calculate',
        'calculate',
        'raise_finger',
        'raise_finger',
        'respond_to_question',
        'respond_to_question',
        'respond_to_question',
        'rock_n_roll',
        'hello',
        'goodbye',
        'goodbye',
        'countdown',
        'calculate',
        'calculate',
        'calculate',
        'raise_finger',
        'raise_finger',
        'respond_to_question',
        'respond_to_question',
        'respond_to_question',
        'rock_n_roll',
        'hello',
        'goodbye',
        'goodbye'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Encode intents to numerical values
df['intent_label'] = df['intent'].map(intent_to_label)

# Tokenization and TF-IDF Vectorization
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
X = vectorizer.fit_transform(df['command']).toarray()

# Get labels
y = df['intent_label'].values

# Convert labels to one-hot encoding
y = to_categorical(y, num_classes=len(intents))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and summarize the model
input_shape = (X_train.shape[1],)  # Adjust input shape based on TF-IDF features
model = create_model(input_shape)
model.summary()

# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=4, verbose=1, validation_data=(X_test, y_test))

# Save the model for later use
model.save("intent_recognition_model_v2.h5")

# Save the vectorizer for later use
with open('vectorizer_v2.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

# Save the label encoder
with open('intent_to_label_v2.pkl', 'wb') as f:
    pickle.dump(intent_to_label, f)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'Test Accuracy: {accuracy:.4f}')

