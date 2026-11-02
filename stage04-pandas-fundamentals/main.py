
# ============================================================
# Stage 04 - Student Dataset Explorer
# ============================================================

import pandas as pd


# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

df = pd.read_csv(
    "stage04-pandas-fundamentals/data/students.csv"
)


# ------------------------------------------------------------
# Data Cleaning
# ------------------------------------------------------------

clean_df = df.copy()

clean_df["score"] = pd.to_numeric(
    clean_df["score"],
    errors="coerce"
)

clean_df = clean_df.dropna(subset=["score"])
clean_df = clean_df[
    clean_df["score"].between(0, 100)
]


# ------------------------------------------------------------
# Data Analysis
# ------------------------------------------------------------

average_score = clean_df["score"].mean()
highest_score = clean_df["score"].max()
lowest_score = clean_df["score"].min()

passing_students = clean_df[
    clean_df["score"] >= 60
]

pass_rate = (
    len(passing_students) / len(clean_df)
) * 100

department_averages = clean_df.groupby(
    "department"
)["score"].mean()


# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

print("=== Student Dataset Explorer ===")

print(f"Original rows: {len(df)}")
print(f"Valid rows: {len(clean_df)}")

print("\n=== Statistics ===")
print(f"Average score: {average_score:.2f}")
print(f"Highest score: {highest_score:.0f}")
print(f"Lowest score: {lowest_score:.0f}")
print(f"Pass rate: {pass_rate:.2f}%")

print("\n=== Department Averages ===")
print(department_averages)

print("\n=== Passing Students ===")
print(passing_students[["name", "score"]])



# ============================================================
# Challenge 01 - Student With the Highest Score
# ============================================================

max_score = clean_df["score"].max()

highest_student = clean_df[
    clean_df["score"] == max_score
]

print("\n=== Highest Scoring Student ===")
print(highest_student[["name", "score"]])


# ============================================================
# Challenge 02 - Highest Average Study Hours by Department
# ============================================================

department_hours = clean_df.groupby(
    "department"
)["study_hours"].mean()

highest_hours_department = department_hours.idxmax()

print("\n=== Highest Average Study Hours ===")
print(f"Department: {highest_hours_department}")
print(f"Average hours: {department_hours.max():.2f}")


# ============================================================
# Challenge 03 - Students Meeting Both Conditions
# ============================================================

qualified_students = clean_df[
    (clean_df["study_hours"] >= 5)
    & (clean_df["score"] >= 70)
]

print("\n=== Qualified Students ===")
print(qualified_students[["name", "score", "study_hours"]])
print(f"Qualified students: {len(qualified_students)}")


# ============================================================
# Challenge 04 - Performance Classification
# ============================================================

def get_performance(score):
    if score >= 60:
        return "PASS"
    else:
        return "FAIL"


clean_df["performance"] = clean_df["score"].apply(
    get_performance
)

print("\n=== Student Performance ===")
print(clean_df[["name", "score", "performance"]])
