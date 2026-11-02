
# Stage 05 - Lesson 02: Bar Charts and Histograms

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


# Bar Chart
plt.figure(figsize=(8, 5))

plt.bar(df["name"], df["score"])

plt.title("Student Score Comparison")
plt.xlabel("Student")
plt.ylabel("Score")
plt.ylim(0, 100)

plt.tight_layout()
plt.show()


# Histogram
plt.figure(figsize=(8, 5))

plt.hist(
    df["score"],
    bins=[0, 20, 40, 60, 80, 100],
    edgecolor="black"
)

plt.title("Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()
