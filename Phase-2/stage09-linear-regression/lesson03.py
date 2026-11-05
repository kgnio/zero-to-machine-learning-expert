
# ============================================================
# Stage 09 - Lesson 03: Regression Evaluation
# ============================================================

import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ------------------------------------------------------------
# Example Predictions
# ------------------------------------------------------------

actual = np.array([100, 200, 300])
predicted = np.array([110, 180, 330])


# ------------------------------------------------------------
# Calculate Metrics
# ------------------------------------------------------------

mae = mean_absolute_error(actual, predicted)
mse = mean_squared_error(actual, predicted)
rmse = np.sqrt(mse)
r2 = r2_score(actual, predicted)


print("=== Regression Metrics ===")
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R2: {r2:.4f}")
