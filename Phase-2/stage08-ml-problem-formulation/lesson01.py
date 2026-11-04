
# ============================================================
# Stage 08 - Lesson 01: ML Problem Formulation
# ============================================================


def describe_ml_problem(name, features, target, problem_type):
    print(f"\n=== {name} ===")
    print(f"Problem type: {problem_type}")
    print(f"Features: {features}")
    print(f"Target: {target}")


describe_ml_problem(
    name="House Price Prediction",
    features=["area", "rooms", "building_age"],
    target="price",
    problem_type="regression"
)

describe_ml_problem(
    name="Email Spam Detection",
    features=["message_length", "link_count", "word_frequency"],
    target="is_spam",
    problem_type="classification"
)
