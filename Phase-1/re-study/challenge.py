
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

def clean_and_summarize(scores):
    valid_scores = []
    invalid_scores = []

    for score in scores:
        if isinstance(score, (int, float)) and 0 <= score <= 100:
            valid_scores.append(score)
        else:
            invalid_scores.append(score)

    unique_scores = []

    for score in valid_scores:
        if score not in unique_scores:
            unique_scores.append(score)


    sorted_scores = sorted(unique_scores)
    n = len(sorted_scores)

    if n == 0:
        median = None

    elif n % 2 == 0:
        middle = n // 2

        left = sorted_scores[middle - 1]
        right = sorted_scores[middle]

        median = (left + right) / 2

    else:
        middle = n // 2
        median = sorted_scores[middle]
       

    return {
        "valid_scores": valid_scores,
        "invalid_scores": invalid_scores,
        "unique_scores": unique_scores,
        "median": median
    }

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

def analyze_matrix(matrix, weights):

    # 1. Calculate row averages
    row_means = np.mean(matrix, axis=1)

    # 2. Calculate column averages
    column_means = np.mean(matrix, axis=0)

    # 3. Calculate dot product manually
    def manual_dot_product(a, b):
        total = 0

        for i in range(len(a)):
            total += a[i] * b[i]

        return total

    first_student = matrix[0]

    dot_product = manual_dot_product(
        first_student,
        weights
    )

    # 4. Calculate weighted scores
    weighted_scores = matrix @ weights

    return {
        "row_means": row_means,
        "column_means": column_means,
        "manual_dot_product": dot_product,
        "weighted_scores": weighted_scores
    }


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

def analyze_dataframe(df, output_dir):

    # 1. Create a copy of the original DataFrame
    clean_df = df.copy()

    # 2. Convert scores to numeric values
    clean_df["score"] = pd.to_numeric(
        clean_df["score"],
        errors="coerce"
    )

    # 3. Remove missing scores
    clean_df = clean_df.dropna(subset=["score"])

    # 4. Remove scores outside the valid range
    clean_df = clean_df[
        clean_df["score"].between(0, 100)
    ].copy()

    # 5. Calculate average score by department
    department_averages = (
        clean_df.groupby("department")["score"].mean()
    )

    # 6. Find the student with the highest score
    highest_index = clean_df["score"].idxmax()
    highest_student = clean_df.loc[highest_index]

    # 7. Create the output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 8. Create and save the bar chart
    plt.figure(figsize=(8, 5))

    plt.bar(
        department_averages.index,
        department_averages.values
    )

    plt.title("Average Score by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Score")
    plt.ylim(0, 100)
    plt.tight_layout()

    plt.savefig(
        output_dir / "department_averages.png",
        dpi=150
    )

    plt.close()

    # 9. Display summary
    print(f"Valid records: {len(clean_df)}")
    print(f"Highest scoring student: {highest_student['name']}")
    print(f"Highest score: {highest_student['score']:.2f}")

    print("\nDepartment averages:")
    print(department_averages)

    # 10. Return results
    return clean_df, department_averages


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

def analyze_probability(scores, rng):

    # 1. Probability of scoring at least 80
    high_score_probability = np.mean(scores >= 80)

    # 2. Probability of scoring between 60 and 80
    range_mask = (scores >= 60) & (scores <= 80)
    range_probability = np.mean(range_mask)

    # 3. Population and sample standard deviations
    population_std = np.std(scores, ddof=0)
    sample_std = np.std(scores, ddof=1)

    # 4. Generate sample means
    sample_sizes = [5, 30]
    sample_means = {}

    for size in sample_sizes:
        means = []

        for _ in range(200):
            sample = rng.choice(
                scores,
                size=size,
                replace=True
            )

            means.append(np.mean(sample))

        sample_means[size] = np.array(means)

    # 5. Compare the sampling distributions
    std_means_5 = np.std(sample_means[5])
    std_means_30 = np.std(sample_means[30])

    # 6. Display results
    print("=== Probability Analysis ===")
    print(f"P(Score >= 80): {high_score_probability:.2%}")
    print(f"P(60 <= Score <= 80): {range_probability:.2%}")

    print("\n=== Standard Deviation ===")
    print(f"Population std: {population_std:.4f}")
    print(f"Sample std: {sample_std:.4f}")

    print("\n=== Sampling Comparison ===")
    print(f"Sample size 5 - Std of means: {std_means_5:.4f}")
    print(f"Sample size 30 - Std of means: {std_means_30:.4f}")

    return {
        "high_score_probability": high_score_probability,
        "range_probability": range_probability,
        "population_std": population_std,
        "sample_std": sample_std,
        "sample_mean_std_5": std_means_5,
        "sample_mean_std_30": std_means_30
    }



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

def train_linear_model(x, y, learning_rate=0.05, epochs=500):

    # 1. Initialize model parameters
    weight = 0.0
    bias = 0.0

    loss_history = []

    # 2. Training loop
    for epoch in range(epochs):

        # Generate predictions
        predictions = weight * x + bias

        # Calculate prediction errors
        errors = predictions - y

        # Calculate Mean Squared Error
        loss = np.mean(errors ** 2)

        # Store the current loss
        loss_history.append(loss)

        # Calculate gradients
        weight_gradient = 2 * np.mean(x * errors)
        bias_gradient = 2 * np.mean(errors)

        # Update model parameters
        weight -= learning_rate * weight_gradient
        bias -= learning_rate * bias_gradient

    # 3. Final evaluation
    final_predictions = weight * x + bias
    final_loss = np.mean((final_predictions - y) ** 2)

    print("=== Linear Regression Training ===")
    print(f"Learned weight: {weight:.4f}")
    print(f"Learned bias: {bias:.4f}")
    print(f"Final loss: {final_loss:.6f}")
    
    print("\n=== Predictions ===")

    for actual, predicted in zip(y, final_predictions):
        print(
            f"Actual: {actual:.2f} | "
            f"Predicted: {predicted:.2f}"
        )

    return weight, bias, loss_history



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
