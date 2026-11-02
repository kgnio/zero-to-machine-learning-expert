
# Stage 06 - Lesson 01: Scalars and Vectors

import numpy as np


# Scalars
learning_rate = 0.01
bias = 50000


# Vectors
features = np.array([100, 3, 10])
weights = np.array([20000, 50000, -5000])


# Manual dot product
manual_result = (
    features[0] * weights[0]
    + features[1] * weights[1]
    + features[2] * weights[2]
)


# NumPy dot product
numpy_result = np.dot(features, weights)

prediction = numpy_result + bias


print("=== Scalars and Vectors ===")
print(f"Features: {features}")
print(f"Weights: {weights}")

print("\n=== Dot Product ===")
print(f"Manual result: {manual_result}")
print(f"NumPy result: {numpy_result}")

print("\n=== Prediction ===")
print(f"Predicted value: {prediction:,.0f}")
