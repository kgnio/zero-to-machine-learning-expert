
# ============================================================
# Stage 05 - Student Data Visualization Dashboard
# ============================================================

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# ------------------------------------------------------------
# File Paths
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = (
    BASE_DIR.parent
    / "stage04-pandas-fundamentals"
    / "data"
    / "students.csv"
)

FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)


# ------------------------------------------------------------
# Load and Clean Dataset
# ------------------------------------------------------------

df = pd.read_csv(DATA_PATH)

df["score"] = pd.to_numeric(
    df["score"],
    errors="coerce"
)

df = df.dropna(subset=["score"])
df = df[df["score"].between(0, 100)]


# ------------------------------------------------------------
# Data Analysis
# ------------------------------------------------------------

department_averages = df.groupby(
    "department"
)["score"].mean()

correlation = df["study_hours"].corr(
    df["score"]
)


# ------------------------------------------------------------
# Chart 01 - Department Average Scores
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    department_averages.index,
    department_averages.values
)


# Add value labels above the bars

for department, average in department_averages.items():
    plt.text(
        department,
        average + 2,
        f"{average:.2f}",
        ha="center"
    )


plt.title("Average Scores by Department")
plt.text(100, 100, "label")
plt.xlabel("Department")
plt.ylabel("Average Score")
plt.ylim(0, 100)

plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "department_averages.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 02 - Score Distribution
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["score"],
    bins=[0, 20, 40, 60, 80, 100],
    edgecolor="black"
)


# Calculate the mean score
average_score = df["score"].mean()

# Add a vertical mean line
plt.axvline(
    x=average_score,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Mean: {average_score:.2f}"
)

plt.legend()


plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "score_distribution.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 03 - Study Hours vs Exam Score
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["study_hours"],
    df["score"]
)


# Find the student with the highest score
highest_index = df["score"].idxmax()
highest_student = df.loc[highest_index]

# Highlight the highest-scoring student
plt.scatter(
    highest_student["study_hours"],
    highest_student["score"],
    color="red",
    s=150,
    label=highest_student["name"]
)

plt.legend()


plt.title(
    f"Study Hours vs Exam Score (r={correlation:.2f})"
)

plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "study_hours_scatter.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 04 - Score Box Plot
# ------------------------------------------------------------

plt.figure(figsize=(7, 5))

plt.boxplot(
    df["score"],
    tick_labels=["Scores"]
)

plt.title("Score Box Plot")
plt.ylabel("Score")

plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "score_boxplot.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 05 - Number of Students by Department
# ------------------------------------------------------------

department_counts = df["department"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    department_counts.index,
    department_counts.values
)

plt.title("Number of Students by Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "department_counts.png",
    dpi=150
)

plt.close()



# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

print("=== Student Data Visualization Dashboard ===")
print(f"Valid records: {len(df)}")
print(f"Average score: {df['score'].mean():.2f}")
print(f"Median score: {df['score'].median():.2f}")
print(f"Correlation: {correlation:.3f}")
print(f"Charts saved to: {FIGURES_DIR}")
