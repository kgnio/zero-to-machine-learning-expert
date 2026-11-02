
# ============================================================
# Phase 1 Re-Study - Python and ML Cheat Sheet
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. Python Basics
# ============================================================

name = "Alice"
age = 21
score = 87.5
active = True

print(f"Name: {name}")
print(f"Score: {score:.2f}")
print(f"Accuracy: {0.8567:.2%}")


# ============================================================
# 2. Lists, Dictionaries, and Loops
# ============================================================

scores = [85, 42, 76, 95, 68]

print(scores[0])
print(scores[-1])
print(scores[:3])
print(scores[::-1])

scores.append(90)

print(sorted(scores))
print(sorted(scores, reverse=True))

student = {"name": "Alice", "score": 85}

print(student["name"])

for index, value in enumerate(scores):
    print(index, value)


# ============================================================
# 3. Functions and Conditions
# ============================================================

def is_passing(value):
    return value >= 60


valid_scores = []

for value in scores:
    if is_passing(value):
        valid_scores.append(value)

print(valid_scores)


# ============================================================
# 4. NumPy Arrays
# ============================================================

array = np.array([10, 20, 30, 40])

print(array.shape)
print(array.ndim)
print(array.size)
print(array.dtype)

print(array + 5)
print(array * 2)
print(array[array >= 20])

print(np.mean(array))
print(np.median(array))
print(np.std(array))
print(np.var(array))

print(np.max(array))
print(np.argmax(array))
print(np.clip(array, 0, 35))


# ============================================================
# 5. NumPy Matrices
# ============================================================

matrix = np.array([
    [80, 70, 90],
    [60, 85, 75]
])

weights = np.array([0.5, 0.3, 0.2])

print(matrix.shape)
print(matrix[0])
print(matrix[:, 1])

print(np.mean(matrix, axis=0))
print(np.mean(matrix, axis=1))

print(matrix @ weights)
print(matrix.T)


# ============================================================
# 6. Pandas DataFrames
# ============================================================

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "department": [
        "Engineering", "Design", "Engineering"
    ],
    "score": [85, 42, 95]
})

print(df.head())
print(df.tail())
print(df.shape)
print(df.dtypes)

print(df["score"])
print(df[["name", "score"]])

print(df.iloc[0])
print(df.loc[0, "name"])

print(df[df["score"] >= 60])

print(
    df[
        (df["score"] >= 60)
        & (df["department"] == "Engineering")
    ]
)

print(df.groupby("department")["score"].mean())

print(df.sort_values("score", ascending=False))

print(df["score"].idxmax())
print(df["score"].isna().sum())


# ============================================================
# 7. Probability and Statistics
# ============================================================

rng = np.random.default_rng(42)

samples = rng.normal(
    loc=70,
    scale=10,
    size=1000
)

print(np.mean(samples))
print(np.median(samples))

print(np.var(samples, ddof=0))
print(np.var(samples, ddof=1))

print(np.std(samples, ddof=0))
print(np.std(samples, ddof=1))

print(np.mean(samples >= 80))

range_mask = (
    (samples >= 60)
    & (samples <= 80)
)

print(np.mean(range_mask))


# ============================================================
# 8. Matplotlib
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    samples,
    bins=30,
    edgecolor="black"
)

plt.title("Sample Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# 9. Linear Regression
# ============================================================

def predict(x, weight, bias):
    return weight * x + bias


def mse(predictions, targets):
    return np.mean((predictions - targets) ** 2)


def gradients(x, predictions, targets):
    errors = predictions - targets

    weight_gradient = 2 * np.mean(x * errors)
    bias_gradient = 2 * np.mean(errors)

    return weight_gradient, bias_gradient


# ============================================================
# 10. Gradient Descent
# ============================================================

x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([5.0, 8.0, 11.0, 14.0])

weight = 0.0
bias = 0.0

learning_rate = 0.05

for epoch in range(500):
    predictions = predict(x, weight, bias)

    weight_gradient, bias_gradient = gradients(
        x,
        predictions,
        y
    )

    weight -= learning_rate * weight_gradient
    bias -= learning_rate * bias_gradient

print(f"Learned weight: {weight:.4f}")
print(f"Learned bias: {bias:.4f}")
print(f"Final MSE: {mse(predict(x, weight, bias), y):.6f}")
