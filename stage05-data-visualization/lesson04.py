
# Stage 05 - Lesson 04: Box Plots

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


# Display descriptive statistics
print("=== Score Statistics ===")
print(df["score"].describe())


# Create box plot
plt.figure(figsize=(7, 5))

plt.boxplot(
    df["score"],
    tick_labels=["Exam Scores"]
)

plt.title("Exam Score Distribution")
plt.ylabel("Score")

plt.tight_layout()
plt.show()

