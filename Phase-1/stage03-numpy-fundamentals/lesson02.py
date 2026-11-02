
# Stage 03 - Lesson 02: Indexing and Slicing

import numpy as np

scores = np.array([85, 42, 76, 95, 68, 35])

print("=== Indexing ===")
print(f"First: {scores[0]}")
print(f"Last: {scores[-1]}")

print("\n=== Slicing ===")
print(f"First two: {scores[:2]}")
print(f"Last two: {scores[-2:]}")
print(f"Reverse: {scores[::-1]}")
print(f"Middle elements: {scores[1:4]}")
print(f"Every second: {scores[::2]}")
