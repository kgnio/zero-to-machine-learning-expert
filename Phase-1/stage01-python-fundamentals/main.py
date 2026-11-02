
# Stage 01 - Student Grade Analyzer

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 42},
    {"name": "Charlie", "score": 76},
    {"name": "Diana", "score": 35},
    {"name": "Eve", "score": 95},
    {"name":"Frank", "score": 68},
]


def calculate_average(scores):
    if not scores:
        return 0.0

    return sum(scores) / len(scores)


def analyze_students(students):
    scores = []
    passed = 0

    print("=== Student Grade Analyzer ===")

    for student in students:
        name = student["name"]
        score = student["score"]

        scores.append(score)

        if score >= 60:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"

        print(f"{name}: {score} - {status}")

    average = calculate_average(scores)
    highest = max(scores)
    lowest = min(scores)
    pass_rate = (passed / len(students)) * 100
    failed_students = (len(students) - passed)

    print("\n=== Summary ===")
    print(f"Total students: {len(students)}")
    print(f"Average score: {average:.2f}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Pass rate: {pass_rate:.1f}%")
    print(f"Failed students count: {failed_students}")


analyze_students(students)
