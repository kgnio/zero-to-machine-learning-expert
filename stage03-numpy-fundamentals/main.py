
# ============================================================
# Stage 03 - Student Performance Analyzer
# ============================================================

import numpy as np


# ------------------------------------------------------------
# Dataset
# ------------------------------------------------------------

students = ["Alice", "Bob", "Charlie", "Diana"]
subjects = ["Math", "Science", "English"]

scores = np.array([
    [85, 90, 78],
    [72, 65, 80],
    [95, 88, 92],
    [60, 75, 70]
])


# ------------------------------------------------------------
# Data Analysis
# ------------------------------------------------------------

student_averages = np.mean(scores, axis=1)
subject_averages = np.mean(scores, axis=0)

highest_score = np.max(scores)
lowest_score = np.min(scores)

passing_scores = scores[scores >= 60]


# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

print("=== Student Performance Analyzer ===")
print(f"Dataset shape: {scores.shape}")

print("\n=== Student Averages ===")

for index, student in enumerate(students):
    print(f"{student}: {student_averages[index]:.2f}")

print("\n=== Subject Averages ===")

for index, subject in enumerate(subjects):
    print(f"{subject}: {subject_averages[index]:.2f}")

print("\n=== Summary ===")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Passing scores: {passing_scores}")


# ============================================================
# Challenge 01 - Highest Average Student
# ============================================================

highest_average_index = np.argmax(student_averages)
highest_average_student = students[highest_average_index]

print(f"Highest average student: {highest_average_student}")
print(f"Highest average score: {student_averages[highest_average_index]:.2f}")


# ============================================================
# Challenge 02 - Lowest Average Subject
# ============================================================

lowest_average_index = np.argmin(subject_averages)
lowest_average_subject = subjects[lowest_average_index]

print(f"Lowest average subject: {lowest_average_subject}")
print(f"Lowest average score: {subject_averages[lowest_average_index]:.2f}")


# ============================================================
# Challenge 03 - Count Scores Below 70
# ============================================================

print(f"Scores count below 70: {scores[scores < 70].size}")


# ============================================================
# Challenge 04 - Increase Scores and Cap at 100
# ============================================================

increased_scores = scores + 5
capped_scores = np.clip(increased_scores, 0, 100)

print("Scores increased by 5, capped at 100:")
print(capped_scores)
