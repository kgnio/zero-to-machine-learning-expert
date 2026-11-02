
# Stage 07 - Lesson 04: Central Limit Theorem

import matplotlib.pyplot as plt
import numpy as np


rng = np.random.default_rng(42)

population = rng.exponential(
    scale=10,
    size=100000
)

sample_size = 30
number_of_samples = 1000

sample_means = []

for _ in range(number_of_samples):
    sample = rng.choice(
        population,
        size=sample_size,
        replace=True
    )

    sample_means.append(np.mean(sample))


print("=== Sampling Experiment ===")
print(f"Population mean: {np.mean(population):.2f}")
print(f"Mean of sample means: {np.mean(sample_means):.2f}")
print(f"Std of sample means: {np.std(sample_means):.2f}")


plt.figure(figsize=(8, 5))

plt.hist(
    sample_means,
    bins=35,
    edgecolor="black"
)

plt.title("Sampling Distribution of the Mean")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
