
# Stage 07 - Lesson 03: Probability Distributions

import matplotlib.pyplot as plt
import numpy as np


rng = np.random.default_rng(42)

# Generate normally distributed samples
samples = rng.normal(
    loc=70,
    scale=10,
    size=10000
)

print("=== Normal Distribution ===")
print(f"Sample mean: {np.mean(samples):.2f}")
print(f"Sample std: {np.std(samples):.2f}")

plt.figure(figsize=(8, 5))

plt.hist(
    samples,
    bins=40,
    density=True,
    edgecolor="black"
)

plt.axvline(
    x=70,
    color="red",
    linestyle="--",
    label="Expected Mean"
)

plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.legend()
plt.tight_layout()
plt.show()
