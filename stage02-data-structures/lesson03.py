
# Stage 02 - Lesson 03: Algorithm Complexity

import time


def linear_search(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False


numbers = list(range(1_000_000))

start = time.perf_counter()

result = linear_search(numbers, 999_999)

end = time.perf_counter()

print(f"Found: {result}")
print(f"Execution time: {end - start:.6f} seconds")
