
# ============================================================
# Phase 1 Re-Study - Five Comprehensive Challenges
# ============================================================

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ============================================================
# Challenge 01 - Python and Data Cleaning
# ============================================================

def clean_and_summarize(scores):
    """
    Requirements:
    1. Separate valid and invalid scores.
    2. Accept numeric scores from 0 to 100.
    3. Remove duplicate valid scores while preserving order.
    4. Calculate the median of unique valid scores.
    5. Return a dictionary containing all results.

    Expected result for the provided dataset:
    Valid unique scores: [85, 42, 76, 95, 68, 35]
    Invalid scores: [-10, 150, "unknown"]
    Median: 72.0
    """
    raise NotImplementedError("Complete Challenge 01")


# ============================================================
# Challenge 02 - NumPy and Linear Algebra
# ============================================================

def analyze_matrix(matrix, weights):
    """
    Requirements:
    1. Calculate the mean of each row.
    2. Calculate the mean of each column.
    3. Implement dot product using a Python loop.
    4. Calculate weighted scores using matrix multiplication.
    5. Return the results in a dictionary.

    Expected weighted scores:
    [79.0, 70.5, 92.1]
    """
    raise NotImplementedError("Complete Challenge 02")


# ============================================================
# Challenge 03 - Pandas and Visualization
# ============================================================

def analyze_dataframe(df, output_dir):
    """
    Requirements:
    1. Convert the score column to numeric values.
    2. Remove missing or invalid scores.
    3. Calculate mean scores by department.
    4. Find the student with the highest score.
    5. Save a department-average bar chart.

    Return the cleaned DataFrame and department averages.
    """
    raise NotImplementedError("Complete Challenge 03")


# ============================================================
# Challenge 04 - Probability and Statistics
# ============================================================

def analyze_probability(scores, rng):
    """
    Requirements:
    1. Estimate P(score >= 80).
    2. Estimate P(60 <= score <= 80).
    3. Calculate population and sample standard deviations.
    4. Generate 200 sample means for sample sizes 5 and 30.
    5. Compare the standard deviations of those sample means.

    Return a dictionary of numerical results.
    """
    raise NotImplementedError("Complete Challenge 04")


# ============================================================
# Challenge 05 - Gradient Descent From Scratch
# ============================================================

def train_linear_model(x, y, learning_rate=0.05, epochs=500):
    """
    Model:
        prediction = weight * x + bias

    Requirements:
    1. Initialize weight and bias to zero.
    2. Calculate predictions.
    3. Calculate Mean Squared Error.
    4. Calculate the gradients for weight and bias.
    5. Update both parameters using gradient descent.
    6. Save training losses for every epoch.
    7. Return weight, bias, and loss history.

    Use the dataset below to learn:
        y = 3 * x + 2

    Expected:
        Weight approaches 3.
        Bias approaches 2.
        Loss approaches 0.
    """
    raise NotImplementedError("Complete Challenge 05")


# ============================================================
# Challenge Runner
# ============================================================

def main():
    scores = [
        85, 42, 76, 95, 68, 35,
        85, 42, -10, 150, "unknown"
    ]

    matrix = np.array([
        [80, 70, 90],
        [60, 85, 75],
        [95, 90, 88]
    ])

    weights = np.array([0.5, 0.3, 0.2])

    df = pd.DataFrame({
        "name": [
            "Alice", "Bob", "Charlie",
            "Diana", "Eve", "Frank"
        ],
        "department": [
            "Engineering", "Design", "Engineering",
            "Design", "Engineering", "Marketing"
        ],
        "score": [85, 42, 76, None, 95, 68]
    })

    rng = np.random.default_rng(42)

    probability_scores = np.clip(
        rng.normal(70, 12, 1000),
        0,
        100
    )

    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    y = 3 * x + 2

    output_dir = (
        Path(__file__).resolve().parent / "figures"
    )
    output_dir.mkdir(exist_ok=True)

    challenges = [
        ("01", lambda: clean_and_summarize(scores)),
        ("02", lambda: analyze_matrix(matrix, weights)),
        (
            "03",
            lambda: analyze_dataframe(df, output_dir)
        ),
        (
            "04",
            lambda: analyze_probability(
                probability_scores, rng
            )
        ),
        (
            "05",
            lambda: train_linear_model(x, y)
        ),
    ]

    for number, challenge in challenges:
        print(f"\n=== Challenge {number} ===")

        try:
            result = challenge()
            print(result)
        except NotImplementedError:
            print("Not completed yet.")


if __name__ == "__main__":
    main()
