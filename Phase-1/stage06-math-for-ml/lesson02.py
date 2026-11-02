
# Stage 06 - Lesson 02: Matrix Multiplication

import numpy as np


scores = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])

weights = np.array([0.4, 0.4, 0.2])


# Matrix-vector multiplication
weighted_scores = scores @ weights

print("=== Matrix Multiplication ===")
print(f"Scores shape: {scores.shape}")
print(f"Weights shape: {weights.shape}")

print("\n=== Weighted Scores ===")
print(weighted_scores)


# Matrix transpose
transposed = scores.T

print("\n=== Transposed Matrix ===")
print(transposed)
print(f"Transposed shape: {transposed.shape}")
