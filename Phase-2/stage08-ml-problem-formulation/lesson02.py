
# ============================================================
# Stage 08 - Lesson 02: Features and Targets
# ============================================================

import pandas as pd

from sklearn.datasets import load_wine


# Load a real classification dataset
wine = load_wine(as_frame=True)

df = wine.frame.copy()

# Separate features and target
X = df.drop(columns=["target"])
y = df["target"]


print("=== Dataset Information ===")
print(f"Dataset shape: {df.shape}")
print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

print("\n=== Feature Names ===")
print(X.columns.tolist())

print("\n=== Class Distribution ===")
print(y.value_counts().sort_index())

print("\n=== First Five Observations ===")
print(df.head())

print("\n=== Missing Values ===")
print(df.isna().sum())
