
# ============================================================
# Stage 09 - House Price Predictor
# ============================================================

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import joblib

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.model_selection import train_test_split


# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

TARGET_UNIT_USD = 100000


# ------------------------------------------------------------
# 1. Load Real Dataset
# ------------------------------------------------------------

housing = fetch_california_housing(as_frame=True)

X = housing.data
y = housing.target

print("=== California Housing Dataset ===")
print(f"Observations: {len(X)}")
print(f"Features: {X.shape[1]}")
print(f"Missing values: {X.isna().sum().sum()}")


# ------------------------------------------------------------
# 2. Train/Test Split
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ------------------------------------------------------------
# 3. Train Linear Regression
# ------------------------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

joblib.dump(model, "models/house_price_model.joblib")

# ------------------------------------------------------------
# 4. Generate Predictions
# ------------------------------------------------------------

train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)


# ------------------------------------------------------------
# 5. Evaluate Model
# ------------------------------------------------------------

mae = mean_absolute_error(y_test, test_predictions)
mse = mean_squared_error(y_test, test_predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, test_predictions)

train_rmse = np.sqrt(
    mean_squared_error(y_train, train_predictions)
)


# ------------------------------------------------------------
# 6. Baseline Comparison
# ------------------------------------------------------------

baseline_value = y_train.mean()

baseline_predictions = np.full(
    shape=len(y_test),
    fill_value=baseline_value
)

baseline_rmse = np.sqrt(
    mean_squared_error(y_test, baseline_predictions)
)


# ------------------------------------------------------------
# 7. Print Evaluation Results
# ------------------------------------------------------------

print("\n=== Dataset Split ===")
print(f"Training: {len(X_train)}")
print(f"Test: {len(X_test)}")

print("\n=== Regression Metrics ===")
print(f"MAE: ${mae * TARGET_UNIT_USD:,.2f}")
print(f"MSE: {mse:.4f} (100,000 USD)^2")
print(f"RMSE: ${rmse * TARGET_UNIT_USD:,.2f}")
print(f"R2: {r2:.4f}")

print("\n=== Model Comparison ===")
print(f"Training RMSE: ${train_rmse * TARGET_UNIT_USD:,.2f}")
print(f"Test RMSE: ${rmse * TARGET_UNIT_USD:,.2f}")
print(f"Baseline RMSE: ${baseline_rmse * TARGET_UNIT_USD:,.2f}")


# ------------------------------------------------------------
# 8. Inspect Learned Coefficients
# ------------------------------------------------------------

coefficients = pd.Series(
    model.coef_,
    index=X.columns
)

print("\n=== Learned Coefficients ===")
print(coefficients)

print(f"\nIntercept: {model.intercept_:.4f}")


# ------------------------------------------------------------
# 9. Display Example Predictions
# ------------------------------------------------------------

print("\n=== Example Predictions ===")

for actual, predicted in zip(
    y_test.iloc[:5],
    test_predictions[:5]
):
    print(
        f"Actual: ${actual * TARGET_UNIT_USD:,.0f} | "
        f"Predicted: ${predicted * TARGET_UNIT_USD:,.0f}"
    )


# ------------------------------------------------------------
# 10. Plot Actual vs Predicted
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    test_predictions,
    alpha=0.25,
    s=12
)

minimum = min(y_test.min(), test_predictions.min())
maximum = max(y_test.max(), test_predictions.max())

plt.plot(
    [minimum, maximum],
    [minimum, maximum],
    color="red",
    linestyle="--",
    label="Perfect Prediction"
)

plt.title("Actual vs Predicted House Values")
plt.xlabel("Actual Value (100,000 USD)")
plt.ylabel("Predicted Value (100,000 USD)")
plt.legend()
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "actual_vs_predicted.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# 11. Plot Residuals
# ------------------------------------------------------------

residuals = y_test.to_numpy() - test_predictions

plt.figure(figsize=(8, 6))

plt.scatter(
    test_predictions,
    residuals,
    alpha=0.25,
    s=12
)

plt.axhline(
    y=0,
    color="red",
    linestyle="--"
)

plt.title("Residual Analysis")
plt.xlabel("Predicted Value (100,000 USD)")
plt.ylabel("Residual (100,000 USD)")
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "residual_analysis.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# 12. Plot Coefficients
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

coefficients.sort_values().plot(kind="barh")

plt.title("Linear Regression Coefficients")
plt.xlabel("Coefficient Value")
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "model_coefficients.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Final Summary
# ------------------------------------------------------------

print("\n=== Training Complete ===")
print("Model trained successfully.")
print("Predictions evaluated.")
print("Baseline comparison completed.")
print("Three figures saved.")

print(f"\nFigures directory: {FIGURES_DIR}")



# ============================================================
# Stage 09 - Final Challenges
# ============================================================


# ------------------------------------------------------------
# Challenge 01 - Compare Training and Test Metrics
# ------------------------------------------------------------

print("\n=== Challenge 01: Training vs Test ===")

for name, actual, predicted in [
    ("Training", y_train, train_predictions),
    ("Test", y_test, test_predictions)
]:
    current_mae = mean_absolute_error(actual, predicted)
    current_mse = mean_squared_error(actual, predicted)
    current_rmse = np.sqrt(current_mse)
    current_r2 = r2_score(actual, predicted)

    print(f"\n{name}:")
    print(f"MAE: ${current_mae * TARGET_UNIT_USD:,.2f}")
    print(f"MSE: {current_mse:.4f}")
    print(f"RMSE: ${current_rmse * TARGET_UNIT_USD:,.2f}")
    print(f"R2: {current_r2:.4f}")


# ------------------------------------------------------------
# Challenge 02 - Calculate Baseline Improvement
# ------------------------------------------------------------

improvement = (
    (baseline_rmse - rmse) / baseline_rmse
) * 100

print("\n=== Challenge 02: Baseline Improvement ===")
print(f"Baseline RMSE: ${baseline_rmse * TARGET_UNIT_USD:,.2f}")
print(f"Model RMSE: ${rmse * TARGET_UNIT_USD:,.2f}")
print(f"RMSE improvement: {improvement:.2f}%")


# ------------------------------------------------------------
# Challenge 03 - Find the Five Largest Errors
# ------------------------------------------------------------

error_analysis = pd.DataFrame({
    "actual": y_test.to_numpy() * TARGET_UNIT_USD,
    "predicted": test_predictions * TARGET_UNIT_USD
})

error_analysis["absolute_error"] = np.abs(
    error_analysis["actual"] - error_analysis["predicted"]
)

largest_errors = error_analysis.nlargest(
    5,
    "absolute_error"
)

print("\n=== Challenge 03: Largest Errors ===")
print(largest_errors.round(2).to_string(index=False))


# ------------------------------------------------------------
# Challenge 04 - Train a Single Feature Model
# ------------------------------------------------------------

single_feature = ["MedInc"]

X_train_single = X_train[single_feature]
X_test_single = X_test[single_feature]

single_model = LinearRegression()

single_model.fit(X_train_single, y_train)

single_predictions = single_model.predict(X_test_single)

single_mae = mean_absolute_error(y_test, single_predictions)
single_mse = mean_squared_error(y_test, single_predictions)
single_rmse = np.sqrt(single_mse)
single_r2 = r2_score(y_test, single_predictions)

print("\n=== Challenge 04: Model Comparison ===")

print("\nFull Model (8 features):")
print(f"MAE: ${mae * TARGET_UNIT_USD:,.2f}")
print(f"RMSE: ${rmse * TARGET_UNIT_USD:,.2f}")
print(f"R2: {r2:.4f}")

print("\nSingle Feature Model (MedInc):")
print(f"MAE: ${single_mae * TARGET_UNIT_USD:,.2f}")
print(f"RMSE: ${single_rmse * TARGET_UNIT_USD:,.2f}")
print(f"R2: {single_r2:.4f}")
