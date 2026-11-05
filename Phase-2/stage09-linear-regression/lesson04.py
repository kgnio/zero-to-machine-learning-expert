
# ============================================================
# Stage 09 - Lesson 04: Coefficients and Residuals
# ============================================================

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# ------------------------------------------------------------
# Load and Split
# ------------------------------------------------------------

housing = fetch_california_housing(as_frame=True)

X = housing.data
y = housing.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ------------------------------------------------------------
# Train Model
# ------------------------------------------------------------

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)


# ------------------------------------------------------------
# Inspect Coefficients
# ------------------------------------------------------------

coefficients = pd.Series(
    model.coef_,
    index=X.columns
)

print("=== Model Coefficients ===")
print(coefficients)

print(f"\nIntercept: {model.intercept_:.4f}")


# ------------------------------------------------------------
# Calculate Residuals
# ------------------------------------------------------------

residuals = y_test.to_numpy() - predictions

print("\n=== Residual Statistics ===")
print(f"Mean residual: {residuals.mean():.4f}")
print(f"Residual std: {residuals.std():.4f}")
print("\n=== First Five Rows ===")
print(housing.frame.head().to_string(index=False))

# ------------------------------------------------------------
# Residual Plot
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    predictions,
    residuals,
    alpha=0.3
)

plt.axhline(
    y=0,
    color="red",
    linestyle="--"
)

plt.title("Residuals vs Predictions")
plt.xlabel("Predicted Value")
plt.ylabel("Residual")
plt.tight_layout()

plt.show()
