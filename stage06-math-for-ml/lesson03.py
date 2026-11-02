
# Stage 06 - Lesson 03: Derivatives


def function(x):
    return x ** 2


def analytical_derivative(x):
    return 2 * x


def numerical_derivative(x, h=0.0001):
    return (function(x + h) - function(x)) / h


x = -2

print("=== Derivatives ===")
print(f"Input: {x}")
print(f"Function value: {function(x)}")
print(f"Analytical derivative: {analytical_derivative(x)}")
print(f"Numerical derivative: {numerical_derivative(x):.4f}")
