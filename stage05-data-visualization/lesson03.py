
# Stage 05 - Lesson 03: Scatter Plots and Correlation

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "stage04-pandas-fundamentals"
    / "data"
    / "students.csv"
)

df = pd.read_csv(DATA_PATH)

df = df.dropna(subset=["score"])
df = df[df["score"].between(0, 100)]


# Calculate correlation
correlation = df["study_hours"].corr(df["score"])

print(f"Correlation: {correlation:.3f}")


# Create scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(
    df["study_hours"],
    df["score"]
)

plt.title(f"Study Hours vs Exam Score (r={correlation:.2f})")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
