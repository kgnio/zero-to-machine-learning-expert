
# ============================================================
# Stage 08 - Dataset Preparation Pipeline
# ============================================================

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)


# ------------------------------------------------------------
# 1. Load Dataset
# ------------------------------------------------------------

wine = load_wine(as_frame=True)

df = wine.frame.copy()

print("=== Dataset Information ===")
print(f"Dataset shape: {df.shape}")
print(f"Missing values: {df.isna().sum().sum()}")


# ------------------------------------------------------------
# 2. Define Features and Target
# ------------------------------------------------------------

X = df.drop(columns=["target"])
y = df["target"]

print("\n=== Problem Formulation ===")
print("Problem type: Multiclass Classification")
print(f"Features: {X.shape[1]}")
print(f"Target classes: {sorted(y.unique())}")


# ------------------------------------------------------------
# 3. Split Dataset
# ------------------------------------------------------------

X_dev, X_test, y_dev, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

X_train, X_val, y_train, y_val = train_test_split(
    X_dev,
    y_dev,
    test_size=0.25,
    random_state=42,
    stratify=y_dev
)


# ------------------------------------------------------------
# 4. Validate Splits
# ------------------------------------------------------------

print("\n=== Dataset Splits ===")
print(f"Training: {len(X_train)}")
print(f"Validation: {len(X_val)}")
print(f"Test: {len(X_test)}")

assert (
    len(X_train) + len(X_val) + len(X_test)
    == len(X)
)

assert set(X_train.index).isdisjoint(X_val.index)
assert set(X_train.index).isdisjoint(X_test.index)
assert set(X_val.index).isdisjoint(X_test.index)


# ------------------------------------------------------------
# 5. Inspect Class Distribution
# ------------------------------------------------------------

class_distribution = pd.DataFrame({
    "train": y_train.value_counts(normalize=True),
    "validation": y_val.value_counts(normalize=True),
    "test": y_test.value_counts(normalize=True)
}).sort_index()

print("\n=== Class Distribution ===")
print(class_distribution.round(3))


# ------------------------------------------------------------
# 6. Feature Scaling
# ------------------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

print("\n=== Scaled Feature Shapes ===")
print(f"Train: {X_train_scaled.shape}")
print(f"Validation: {X_val_scaled.shape}")
print(f"Test: {X_test_scaled.shape}")


# ------------------------------------------------------------
# 7. Save Class Distribution Chart
# ------------------------------------------------------------

class_distribution.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Class Distribution Across Dataset Splits")
plt.xlabel("Class")
plt.ylabel("Proportion")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "class_distribution.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# 8. Final Summary
# ------------------------------------------------------------

print("\n=== Pipeline Summary ===")
print("Dataset loaded successfully.")
print("Features and target separated.")
print("Train, validation and test splits created.")
print("Class proportions inspected.")
print("Scaling fitted on training data only.")
print("No model has been trained.")

print(f"\nFigures directory: {FIGURES_DIR}")


# ============================================================
# Stage 08 - Mini Project Challenges
# ============================================================


# ------------------------------------------------------------
# Challenge 01 - Count Observations in Each Class
# ------------------------------------------------------------

class_counts = y.value_counts().sort_index()

print("\n=== Challenge 01: Class Counts ===")
print(class_counts)


# ------------------------------------------------------------
# Challenge 02 - Calculate Dataset Split Percentages
# ------------------------------------------------------------

total_records = len(X)

train_percentage = len(X_train) / total_records * 100
validation_percentage = len(X_val) / total_records * 100
test_percentage = len(X_test) / total_records * 100

print("\n=== Challenge 02: Dataset Split Percentages ===")
print(f"Training: {train_percentage:.2f}%")
print(f"Validation: {validation_percentage:.2f}%")
print(f"Test: {test_percentage:.2f}%")


# ------------------------------------------------------------
# Challenge 03 - Verify No Overlapping Observations
# ------------------------------------------------------------

train_indices = set(X_train.index)
validation_indices = set(X_val.index)
test_indices = set(X_test.index)

train_val_overlap = train_indices.intersection(validation_indices)
train_test_overlap = train_indices.intersection(test_indices)
val_test_overlap = validation_indices.intersection(test_indices)

no_overlap = (
    len(train_val_overlap) == 0
    and len(train_test_overlap) == 0
    and len(val_test_overlap) == 0
)

print("\n=== Challenge 03: Split Integrity ===")
print(f"Train/Validation overlap: {len(train_val_overlap)}")
print(f"Train/Test overlap: {len(train_test_overlap)}")
print(f"Validation/Test overlap: {len(val_test_overlap)}")
print(f"No overlapping observations: {no_overlap}")

assert no_overlap, "Dataset splits contain overlapping observations."


# ------------------------------------------------------------
# Challenge 04 - Compare Feature Statistics Before and After
# ------------------------------------------------------------

feature_name = "alcohol"
feature_index = X_train.columns.get_loc(feature_name)

original_values = X_train[feature_name]
scaled_values = X_train_scaled[:, feature_index]

original_mean = np.mean(original_values)
original_std = np.std(original_values)

scaled_mean = np.mean(scaled_values)
scaled_std = np.std(scaled_values)

print("\n=== Challenge 04: Feature Scaling Comparison ===")
print(f"Feature: {feature_name}")

print("\nBefore Scaling:")
print(f"Mean: {original_mean:.4f}")
print(f"Standard deviation: {original_std:.4f}")

print("\nAfter Scaling:")
print(f"Mean: {scaled_mean:.4f}")
print(f"Standard deviation: {scaled_std:.4f}")
