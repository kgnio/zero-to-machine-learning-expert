
# Stage 03 - Lesson 04: Matrices

import numpy as np

scores = np.array([
    [85, 90, 78],
    [72, 65, 80],
    [95, 88, 92]
])

print("=== Student Score Matrix ===")
print(scores)

print(f"Shape: {scores.shape}")
print(f"Dimensions: {scores.ndim}")

print("\n=== Matrix Operations ===")
print(f"First student: {scores[0]}")
print(f"Math scores: {scores[:, 0]}")
print(f"First student's science score: {scores[0, 1]}")

print("\n=== Statistics ===")
print(f"Overall mean: {np.mean(scores):.2f}")
print(f"Average by student: {np.mean(scores, axis=1)}")
print(f"Average by subject: {np.mean(scores, axis=0)}")


print(f"Second student: {scores[1]}")
print(f"Eng scores: {scores[:, 2]}")
print(f"Max by student: {np.max(scores, axis=1)}")