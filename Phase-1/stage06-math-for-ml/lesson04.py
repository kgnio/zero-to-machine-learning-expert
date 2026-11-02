
# Stage 06 - Lesson 04: Gradients


def loss_function(weight):
    return (weight - 3) ** 2


def gradient(weight):
    return 2 * (weight - 3)


weight = 8.0
learning_rate = 1.1

print("=== Gradient Descent ===")

for step in range(10):
    loss = loss_function(weight)

    print(
        f"Step {step:02d} | "
        f"Weight: {weight:.4f} | "
        f"Loss: {loss:.4f}"
    )

    weight = weight - learning_rate * gradient(weight)

print(f"\nFinal weight: {weight:.4f}")
print(f"Final loss: {loss_function(weight):.4f}")
