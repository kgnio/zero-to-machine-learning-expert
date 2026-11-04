
# ============================================================
# Stage 09 - Lesson 01: Simple Linear Regression
# ============================================================

import numpy as np

from sklearn.linear_model import LinearRegression


# ------------------------------------------------------------
# Dataset
# ------------------------------------------------------------

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

y = np.array([15, 25, 35, 45, 55])


# ------------------------------------------------------------
# Model Training
# ------------------------------------------------------------

model = LinearRegression()

model.fit(X, y)


# ------------------------------------------------------------
# Learned Parameters
# ------------------------------------------------------------

weight = model.coef_[0]
bias = model.intercept_

print("=== Learned Parameters ===")
print(f"Weight: {weight:.4f}")
print(f"Bias: {bias:.4f}")


# ------------------------------------------------------------
# Predictions
# ------------------------------------------------------------

new_distances = np.array([
    [6],
    [7],
    [8],
    [10]
])

predictions = model.predict(new_distances)

print("\n=== Predictions ===")

for distance, prediction in zip(
    new_distances.ravel(),
    predictions
):
    print(
        f"Distance: {distance} km | "
        f"Predicted price: {prediction:.2f}"
    )
