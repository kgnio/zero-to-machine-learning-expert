
# ============================================================
# Stage 09 - Lesson 02: Multiple Linear Regression
# ============================================================

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

housing = fetch_california_housing(as_frame=True)

X = housing.data
y = housing.target


print("=== Dataset Information ===")
print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

print("\n=== Feature Names ===")
print(X.columns.tolist())


# ------------------------------------------------------------
# Train/Test Split
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ------------------------------------------------------------
# Model Training
# ------------------------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)


# ------------------------------------------------------------
# Predictions
# ------------------------------------------------------------

predictions = model.predict(X_test)

print("\n=== Predictions ===")

for actual, predicted in zip(
    y_test.iloc[:5],
    predictions[:5]
):
    print(
        f"Actual: ${actual * 100000:,.0f} | "
        f"Predicted: ${predicted * 100000:,.0f}"
    )


# ------------------------------------------------------------
# Challenge 02 - Inspect Dataset Splits
# ------------------------------------------------------------

print("\n=== Challenge 02: Dataset Splits ===")

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")

print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")

total_observations = len(X)

train_percentage = len(X_train) / total_observations * 100
test_percentage = len(X_test) / total_observations * 100

print("\n=== Split Percentages ===")
print(f"Training: {train_percentage:.2f}%")
print(f"Test: {test_percentage:.2f}%")

assert len(X_train) + len(X_test) == len(X)
assert len(y_train) + len(y_test) == len(y)

print("\nDataset split verification passed.")
