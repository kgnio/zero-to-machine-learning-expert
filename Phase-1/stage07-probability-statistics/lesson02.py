
# Stage 07 - Lesson 02: Probability

import numpy as np

rng = np.random.default_rng(42)

rolls = rng.integers(1, 7, size=10000)

even_rolls = np.sum(rolls % 2 == 0)

experimental_probability = even_rolls / len(rolls)
theoretical_probability = 3 / 6

print("=== Dice Probability ===")
print(f"Rolls: {len(rolls)}")
print(f"Even results: {even_rolls}")
print(f"Experimental: {experimental_probability:.4f}")
print(f"Theoretical: {theoretical_probability:.4f}")
