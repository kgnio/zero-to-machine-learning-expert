
# Stage 02 - Data Processing Toolkit


# ------------------------------------------------------------
# Data Validation
# ------------------------------------------------------------

def validate_score(score):
    return (
        isinstance(score, (int, float))
        and 0 <= score <= 100
    )


# ------------------------------------------------------------
# Data Cleaning
# ------------------------------------------------------------

def clean_scores(scores):
    valid = []
    invalid = []

    for score in scores:
        if validate_score(score):
            valid.append(score)
        else:
            invalid.append(score)

    return valid, invalid


# ------------------------------------------------------------
# Statistical Calculations
# ------------------------------------------------------------

def calculate_statistics(scores):
    if not scores:
        return None

    return {
        "count": len(scores),
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores),
    }


# ============================================================
# Dataset
# ============================================================

scores = [85, 42, 76, 95, 68, 35, -10, 150]

valid_scores, invalid_scores = clean_scores(scores)
statistics = calculate_statistics(valid_scores)


# ============================================================
# Challenge 01 - Calculate Median
# ============================================================

sorted_scores = sorted(valid_scores)
n = len(sorted_scores)
middle = n // 2

if len(sorted_scores) % 2 == 0:
    left = sorted_scores[middle - 1]
    right = sorted_scores[middle]
    median = (left + right) / 2
else:
    median = sorted_scores[middle]

print(f"Median: {median}")


# ============================================================
# Challenge 02 - Remove Duplicates
# ============================================================

not_duplicate_scores = []

for score in valid_scores:
    if score not in not_duplicate_scores:
        not_duplicate_scores.append(score)

print(f"Not Duplicate: {not_duplicate_scores}")


# ============================================================
# Challenge 03 - Count Passing Scores
# ============================================================

greater_60 = []

for score in valid_scores:
    if score >= 60:
        greater_60.append(score)

print(f"Greater 60 valid: {len(greater_60)}")


# ============================================================
# Challenge 04 - Sort in Descending Order
# ============================================================

sorted_scores_descend = sorted(valid_scores, reverse=True)

print(f"Descend valid: {sorted_scores_descend}")


# ============================================================
# Results
# ============================================================

print("=== Data Processing Toolkit ===")
print(f"Valid scores: {valid_scores}")
print(f"Invalid scores: {invalid_scores}")

if statistics is not None:
    print("\n=== Statistics ===")
    print(f"Count: {statistics['count']}")
    print(f"Average: {statistics['average']:.2f}")
    print(f"Highest: {statistics['highest']}")
    print(f"Lowest: {statistics['lowest']}")
