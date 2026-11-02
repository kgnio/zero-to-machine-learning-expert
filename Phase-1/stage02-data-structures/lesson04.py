
# Stage 02 - Lesson 04: Data Validation

def validate_score(score):
    if not isinstance(score, (int, float)):
        return False

    if score < 0 or score > 100:
        return False

    return True


scores = [85, -10, 76, 150, 95, "unknown"]

for score in scores:
    if validate_score(score):
        print(f"Valid: {score}")
    else:
        print(f"Invalid: {score}")
