
# Stage 05 - Lesson 01: Matplotlib Fundamentals

import matplotlib.pyplot as plt

students = ["Alice", "Bob", "Charlie", "Diana"]
scores = [85, 72, 95, 60]

plt.figure(figsize=(8, 5))

plt.plot(students, scores, marker="s")

plt.title("Student Exam Performance")
plt.xlabel("Student")
plt.ylabel("Score")

plt.ylim(0, 100)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
