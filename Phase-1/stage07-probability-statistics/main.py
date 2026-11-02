
# ============================================================
# Stage 07 - Statistical Simulation Lab
# ============================================================

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

rng = np.random.default_rng(42)


# ------------------------------------------------------------
# Generate Synthetic Dataset
# ------------------------------------------------------------

scores = rng.normal(
    loc=70,
    scale=12,
    size=1000
)

scores = np.clip(scores, 0, 100)


# ------------------------------------------------------------
# Descriptive Statistics
# ------------------------------------------------------------

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

passing_scores = scores >= 60
pass_probability = np.mean(passing_scores)


# ------------------------------------------------------------
# Sampling Experiment
# ------------------------------------------------------------

sample_means = []

for _ in range(500):
    sample = rng.choice(
        scores,
        size=30,
        replace=True
    )

    sample_means.append(np.mean(sample))


# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

print("=== Statistical Simulation Lab ===")
print(f"Total records: {len(scores)}")

print("\n=== Statistics ===")
print(f"Mean: {mean_score:.2f}")
print(f"Median: {median_score:.2f}")
print(f"Standard deviation: {std_score:.2f}")

print("\n=== Probability ===")
print(f"Estimated pass probability: {pass_probability:.2%}")

print("\n=== Sampling ===")
print(f"Mean of sample means: {np.mean(sample_means):.2f}")


# ------------------------------------------------------------
# Plot 01 - Score Distribution
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(scores, bins=30, edgecolor="black")

plt.axvline(
    mean_score,
    color="red",
    linestyle="--",
    label=f"Mean: {mean_score:.2f}"
)

plt.title("Synthetic Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "score_distribution.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Plot 02 - Sampling Distribution
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    sample_means,
    bins=30,
    edgecolor="black"
)

plt.title("Sampling Distribution of the Mean")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "sampling_distribution.png",
    dpi=150
)

plt.close()


# ============================================================
# Challenge 01 - Probability of Scoring at Least 80
# ============================================================

high_scores = scores >= 80

high_score_probability = np.mean(high_scores)

print("\n=== High Score Probability ===")
print(f"High score count: {np.sum(high_scores)}")
print(f"Probability of scoring at least 80: {high_score_probability:.2%}")


# ============================================================
# Challenge 02 - Standard Deviation Comparison
# ============================================================

population_std = np.std(scores, ddof=0)
sample_std = np.std(scores, ddof=1)

print("\n=== Standard Deviation Comparison ===")
print(f"Population std: {population_std:.4f}")
print(f"Sample std: {sample_std:.4f}")
print(f"Difference: {sample_std - population_std:.6f}")


# ============================================================
# Challenge 03 - Probability Between 60 and 80
# ============================================================

scores_between_60_and_80 = (
    (scores >= 60) & (scores <= 80)
)

range_probability = np.mean(scores_between_60_and_80)

print("\n=== Score Range Probability ===")
print(f"Scores between 60 and 80: {np.sum(scores_between_60_and_80)}")
print(f"Probability: {range_probability:.2%}")


# ============================================================
# Challenge 04 - Sample Size Comparison
# ============================================================


def run_sampling_experiment(data, sample_size, iterations=500):
    sample_means = []

    for _ in range(iterations):
        sample = rng.choice(
            data,
            size=sample_size,
            replace=True
        )

        sample_means.append(np.mean(sample))

    return np.array(sample_means)



sample_sizes = [5, 30, 100]
sampling_results = {}

print("\n=== Sample Size Comparison ===")

for size in sample_sizes:
    means = run_sampling_experiment(
        scores,
        sample_size=size
    )

    sampling_results[size] = means

    print(
        f"Sample size: {size:3d} | "
        f"Mean: {np.mean(means):.2f} | "
        f"Std of means: {np.std(means):.4f}"
    )


# ------------------------------------------------------------
# Challenge 04 - Sampling Distribution Comparison
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

for size in sample_sizes:
    plt.hist(
        sampling_results[size],
        bins=25,
        density=True,
        alpha=0.4,
        label=f"Sample size: {size}"
    )

plt.title("Sampling Distributions by Sample Size")
plt.xlabel("Sample Mean")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True, alpha=0.2)
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "sample_size_comparison.png",
    dpi=150
)

plt.close()
