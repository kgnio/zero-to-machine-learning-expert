
# Stage 03 - Lesson 03: Vectorized Operations

import numpy as np

scores = np.array([85, 42, 76, 95, 68, 35])

print("=== Vectorized Operations ===")
print(f"Original: {scores}")
print(f"Add 5: {scores + 5}")
print(f"Multiply by 2: {scores * 2}")
print(f"Divide by 10: {scores / 10}")

print("\n=== Boolean Masking ===")

passing_scores = scores[scores >= 70]
minus_10 = scores - 10

print(f"Passing scores 70: {passing_scores}")
print(f"Passing scores 80: {scores[scores >= 80].size}")

print(f"Passing scores: {passing_scores}")
print(f"Passing count: {passing_scores.size}")
