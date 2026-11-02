
# Stage 04 - Lesson 03: Data Cleaning

import pandas as pd

df = pd.read_csv(
    "stage04-pandas-fundamentals/data/students.csv"
)


# Inspect missing values
print("=== Missing Values ===")
print(df.isna().sum())


# Create a clean copy
clean_df = df.copy()


# Convert score column to numeric values
clean_df["score"] = pd.to_numeric(
    clean_df["score"],
    errors="coerce"
)


# Remove rows with missing scores
clean_df = clean_df.dropna(subset=["score"])


# Keep scores within the valid range
clean_df = clean_df[
    clean_df["score"].between(0, 100)
]


# Display cleaned dataset
print("\n=== Cleaned Dataset ===")
print(clean_df)

print(f"\nValid rows: {len(clean_df)}")

print(len(df))
print(len(clean_df))
print(len(df) - len(clean_df))