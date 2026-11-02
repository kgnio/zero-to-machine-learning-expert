
# Stage 04 - Lesson 04: GroupBy and Aggregation

import pandas as pd

df = pd.read_csv(
    "stage04-pandas-fundamentals/data/students.csv"
)

# Clean the score column
df["score"] = pd.to_numeric(
    df["score"],
    errors="coerce"
)

df = df.dropna(subset=["score"])
df = df[df["score"].between(0, 100)]


# Group students by department
department_averages = df.groupby(
    "department"
)["score"].mean()

print("=== Department Averages ===")
print(department_averages)


# Count students in each department
department_counts = df.groupby(
    "department"
)["student_id"].count()

print("\n=== Department Counts ===")
print(department_counts)


# Sort students by score
sorted_students = df.sort_values(
    by="score",
    ascending=False
)

print("\n=== Score Ranking ===")
print(sorted_students[["name", "score"]])


# ============================================================
# Challenge 01 - Maximum Score by Department
# ============================================================

department_maxes = df.groupby(
    "department"
)["score"].max()

print("\n=== Department Maximum Scores ===")
print(department_maxes)


# ============================================================
# Challenge 02 - Sort Students by Study Hours
# ============================================================

sorted_students_by_hours = df.sort_values(
    by="study_hours",
    ascending=False
)

print("\n=== Study Hours Ranking ===")
print(sorted_students_by_hours[["name", "study_hours"]])


# ============================================================
# Challenge 03 - Average Study Hours
# ============================================================

study_hours_avg = df["study_hours"].mean()

print("\n=== Average Study Hours ===")
print(f"Average study hours: {study_hours_avg:.2f}")
