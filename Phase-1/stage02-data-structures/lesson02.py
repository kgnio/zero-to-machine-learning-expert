
# Stage 02 - Lesson 02: Searching and Sorting

scores = [85, 42, 76, 95, 68, 35]

ascending = sorted(scores)
descending = sorted(scores, reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)

# Linear search in the original list
target = 99
found = False

for score in scores:
    if score == target:
        found = True
        break

# Filter scores above 70
scores_70 = []

for score in scores:
    if score > 70:
        scores_70.append(score)

# Calculate the average
if scores_70:
    average_70 = sum(scores_70) / len(scores_70)
else:
    average_70 = 0.0

print(f"Target found: {found}")
print(f"Average: {average_70:.2f}")
print(f"List: {scores_70}")
