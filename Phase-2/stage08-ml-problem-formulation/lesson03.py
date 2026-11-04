
# ============================================================
# Stage 08 - Lesson 03: Train, Validation and Test Split
# ============================================================

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split


wine = load_wine(as_frame=True)

X = wine.data
y = wine.target


# First split: 80% development, 20% test
X_dev, X_test, y_dev, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Second split: 75% train, 25% validation
# Relative to the original data: approximately 60/20
X_train, X_val, y_train, y_val = train_test_split(
    X_dev,
    y_dev,
    test_size=0.25,
    random_state=42,
    stratify=y_dev
)


print("=== Dataset Splitting ===")
print(f"Total observations: {len(X)}")
print(f"Training observations: {len(X_train)}")
print(f"Validation observations: {len(X_val)}")
print(f"Test observations: {len(X_test)}")

print("\n=== Feature Shapes ===")
print(f"X_train: {X_train.shape}")
print(f"X_val: {X_val.shape}")
print(f"X_test: {X_test.shape}")
