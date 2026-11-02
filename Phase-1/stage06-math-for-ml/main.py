
# ============================================================
# Stage 06 - Math for ML From Scratch
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Dataset
# ------------------------------------------------------------

features = np.array([1.0, 2.0, 3.0, 4.0])
targets = np.array([2.0, 4.0, 6.0, 8.0])


# ------------------------------------------------------------
# Model
# ------------------------------------------------------------

def predict(features, weight):
    return features * weight


def calculate_mse(predictions, targets):
    errors = predictions - targets
    return np.mean(errors ** 2)


def calculate_gradient(features, predictions, targets):
    errors = predictions - targets
    return 2 * np.mean(features * errors)


# ------------------------------------------------------------
# Training
# ------------------------------------------------------------

weight = 0.0
learning_rate = 0.05
epochs = 30

loss_history = []

print("=== Training a Simple Model ===")

for epoch in range(epochs):
    predictions = predict(features, weight)

    loss = calculate_mse(predictions, targets)
    loss_history.append(loss)
    gradient = calculate_gradient(
        features,
        predictions,
        targets
    )

    if epoch % 5 == 0:
        print(
            f"Epoch {epoch:02d} | "
            f"Weight: {weight:.4f} | "
            f"Loss: {loss:.6f}"
        )

    weight = weight - learning_rate * gradient


# ------------------------------------------------------------
# Final Evaluation
# ------------------------------------------------------------

final_predictions = predict(features, weight)
final_loss = calculate_mse(final_predictions, targets)

print("\n=== Final Results ===")
print(f"Learned weight: {weight:.4f}")
print(f"Final loss: {final_loss:.6f}")
print(f"Predictions: {final_predictions}")


# ============================================================
# Challenge 01 - Manual Dot Product
# ============================================================

def calculate_dot_product(a, b):
    total = 0

    for i in range(len(a)):
        total += a[i] * b[i]

    return total


a = [2, 3, 4]
b = [5, 6, 7]

result = calculate_dot_product(a, b)

print("\n=== Manual Dot Product ===")
print(f"Result: {result}")


# ============================================================
# Challenge 02 - Learning Rate Comparison
# ============================================================

def train_with_learning_rate(rate):
    experiment_weight = 0.0
    experiment_epochs = 30

    for epoch in range(experiment_epochs):
        experiment_predictions = predict(
            features,
            experiment_weight
        )

        experiment_gradient = calculate_gradient(
            features,
            experiment_predictions,
            targets
        )

        experiment_weight -= rate * experiment_gradient

    final_predictions = predict(
        features,
        experiment_weight
    )

    final_loss = calculate_mse(
        final_predictions,
        targets
    )

    return experiment_weight, final_loss


learning_rates = [0.01, 0.05, 0.10, 0.20]

print("\n=== Learning Rate Comparison ===")

for rate in learning_rates:
    learned_weight, loss = train_with_learning_rate(rate)

    print(
        f"Learning rate: {rate:.2f} | "
        f"Weight: {learned_weight:.4f} | "
        f"Final loss: {loss:.6f}"
    )



# ============================================================
# Challenge 03 - Predict a New Value
# ============================================================

new_feature = 5.0

new_prediction = predict(
    new_feature,
    weight
)

print("\n=== New Prediction ===")
print(f"Input: {new_feature}")
print(f"Prediction: {new_prediction:.4f}")


# ============================================================
# Challenge 04 - Training Loss Curve
# ============================================================

plt.figure(figsize=(8, 5))

plt.plot(
    range(len(loss_history)),
    loss_history,
    marker="o"
)

plt.title("Training Loss Curve")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error")

plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
