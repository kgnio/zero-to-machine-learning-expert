
# Stage 07 - Lesson 01: Descriptive Statistics

import numpy as np

scores = np.array([55, 60, 65, 70, 75, 80, 85, 90, 100])

print("=== Descriptive Statistics ===")

print(f"Mean: {np.mean(scores):.2f}")
print(f"Median: {np.median(scores):.2f}")

print(f"Population variance: {np.var(scores):.2f}")
print(f"Population std: {np.std(scores):.2f}")

print(f"Sample variance: {np.var(scores, ddof=1):.2f}")
print(f"Sample std: {np.std(scores, ddof=1):.2f}")

print(f"Minimum: {np.min(scores)}")
print(f"Maximum: {np.max(scores)}")
print(f"Range: {np.ptp(scores)}")
