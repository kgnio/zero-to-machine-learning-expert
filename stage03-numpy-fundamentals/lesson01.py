
# Stage 03 - Lesson 01: Introduction to NumPy

import numpy as np

scores = np.array([85, 42, 76, 95, 68, 35])

print("=== NumPy Array ===")
print(f"Scores: {scores}")
print(f"Type: {type(scores)}")
print(f"Shape: {scores.shape}")
print(f"Dimensions: {scores.ndim}")
print(f"Size: {scores.size}")
print(f"Data type: {scores.dtype}")

print("\n=== Basic Operations ===")
print(f"Sum: {np.sum(scores)}")
print(f"Mean: {np.mean(scores):.2f}")
print(f"Maximum: {np.max(scores)}")
print(f"Minimum: {np.min(scores)}")
