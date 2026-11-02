
def calculate_average(scores):
    if len(scores) == 0:
        return 0.0

    total = sum(scores)
    count = len(scores)

    return total / count


exam_scores = [85, 92, 76, 88, 95]

average = calculate_average(exam_scores)

print(f"Average score: {average:.2f}")
