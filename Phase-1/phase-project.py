
# ============================================================
# Phase 1 Re-Study - Linear Regression From Scratch
# ============================================================

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

rng = np.random.default_rng(42)


# ------------------------------------------------------------
# 1. Generate Synthetic Data
# ------------------------------------------------------------

# The true relationship is approximately y = 3x + 5.
# Random noise makes the problem less artificial.

x = rng.uniform(0, 10, 100)
noise = rng.normal(0, 1.5, 100)

y = 3 * x + 5 + noise


# ------------------------------------------------------------
# 2. Split Training and Test Data
# ------------------------------------------------------------

# Shuffle observation indices reproducibly.
# Keep 80% for training and 20% for testing.

indices = rng.permutation(len(x))

train_size = int(len(x) * 0.8)

train_indices = indices[:train_size]
test_indices = indices[train_size:]

x_train = x[train_indices]
y_train = y[train_indices]

x_test = x[test_indices]
y_test = y[test_indices]


# ------------------------------------------------------------
# 3. Define the Prediction Function
# ------------------------------------------------------------

def predict(features, weight, bias):
    return weight * features + bias


# ------------------------------------------------------------
# 4. Define the Loss Function
# ------------------------------------------------------------

def calculate_mse(predictions, targets):
    errors = predictions - targets
    return np.mean(errors ** 2)


# ------------------------------------------------------------
# 5. Calculate Gradients
# ------------------------------------------------------------

def calculate_gradients(features, predictions, targets):
    errors = predictions - targets

    weight_gradient = 2 * np.mean(
        features * errors
    )

    bias_gradient = 2 * np.mean(errors)

    return weight_gradient, bias_gradient


# ------------------------------------------------------------
# 6. Train the Model
# ------------------------------------------------------------

weight = 0.0
bias = 0.0

learning_rate = 0.01
epochs = 2000

loss_history = []

print("=== Model Training ===")

for epoch in range(epochs):
    predictions = predict(
        x_train,
        weight,
        bias
    )

    loss = calculate_mse(
        predictions,
        y_train
    )

    loss_history.append(loss)

    weight_gradient, bias_gradient = calculate_gradients(
        x_train,
        predictions,
        y_train
    )

    weight -= learning_rate * weight_gradient
    bias -= learning_rate * bias_gradient

    if epoch % 200 == 0:
        print(
            f"Epoch {epoch:04d} | "
            f"Weight: {weight:.4f} | "
            f"Bias: {bias:.4f} | "
            f"Loss: {loss:.4f}"
        )


# ------------------------------------------------------------
# 7. Evaluate on Training and Test Data
# ------------------------------------------------------------

train_predictions = predict(
    x_train,
    weight,
    bias
)

test_predictions = predict(
    x_test,
    weight,
    bias
)

train_mse = calculate_mse(
    train_predictions,
    y_train
)

test_mse = calculate_mse(
    test_predictions,
    y_test
)


# ------------------------------------------------------------
# 8. Compare With a Baseline
# ------------------------------------------------------------

# The baseline always predicts the training target mean.
# It learns no relationship between x and y.

baseline_value = np.mean(y_train)

baseline_predictions = np.full_like(
    y_test,
    baseline_value
)

baseline_test_mse = calculate_mse(
    baseline_predictions,
    y_test
)


# ------------------------------------------------------------
# 9. Predict an Unseen Input
# ------------------------------------------------------------

new_x = 12.0
new_prediction = predict(new_x, weight, bias)


# ------------------------------------------------------------
# 10. Print Results
# ------------------------------------------------------------

print("\n=== Learned Parameters ===")
print(f"Weight: {weight:.4f}")
print(f"Bias: {bias:.4f}")

print("\n=== Model Evaluation ===")
print(f"Training MSE: {train_mse:.4f}")
print(f"Test MSE: {test_mse:.4f}")
print(f"Baseline Test MSE: {baseline_test_mse:.4f}")

print("\n=== New Prediction ===")
print(f"Input: {new_x}")
print(f"Prediction: {new_prediction:.4f}")


# ------------------------------------------------------------
# 11. Plot Training Loss
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(loss_history)

plt.title("Training Loss Curve")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error")

plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "training_loss.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# 12. Plot Test Predictions
# ------------------------------------------------------------

sorted_indices = np.argsort(x_test)

plt.figure(figsize=(8, 5))

plt.scatter(
    x_test,
    y_test,
    label="Test Observations"
)

plt.plot(
    x_test[sorted_indices],
    test_predictions[sorted_indices],
    color="red",
    label="Learned Regression Line"
)

plt.title("Linear Regression on Test Data")
plt.xlabel("Feature")
plt.ylabel("Target")

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "regression_predictions.png",
    dpi=150
)

plt.close()

print("\nTraining completed.")
print(f"Figures directory: {FIGURES_DIR}")
