
# Stage 04 - Lesson 02: Selecting and Filtering Data

import pandas as pd

df = pd.read_csv(
    "stage04-pandas-fundamentals/data/students.csv"
)


# Display the complete dataset
print("=== Dataset ===")
print(df)


# Select columns
print("\n=== Student Names ===")
print(df["name"])

print("\n=== Names and Scores ===")
print(df[["name", "score"]])


# Select rows
print("\n=== First Student ===")
print(df.iloc[0])

print("\n=== First Three Students ===")
print(df.iloc[:3])


# Filter rows
print("\n=== Engineering Students ===")
engineering = df[df["department"] == "Engineering"]

print(engineering)


print("\n=== Scores Above 70 ===")
high_scores = df[df["score"] > 70]

print(high_scores[["name", "score"]])

# Filter rows
print("\n=== Design Students ===")
design = df[df["department"] == "Design"]

print(design)

# Filter cols
print("\n=== Study hours ===")
more_than_five = df[df["study_hours"] >= 5]

print(more_than_five)

# Filter cols
print("\n=== Score 60 ===")
more_than_60 = df[df["score"] >= 60]
print(more_than_60[["name", "score"]])
