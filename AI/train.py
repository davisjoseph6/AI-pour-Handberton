#!/usr/bin/env python3

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create a simple model
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Dummy data for demonstration purposes
import numpy as np
X = np.random.rand(100, 1)
y = X * 2 + np.random.rand(100, 1)

# Train the model
model.fit(X, y, epochs=10)

# Save the model
model.save('model.h5')

