
# Stage 04 - Lesson 01: Introduction to Pandas

import pandas as pd


# Create a DataFrame
students = {
    "name": ["Alice", "Bob", "Charlie","Diana"],
    "math": [85, 72, 95, 60],
    "science": [90, 65, 88, 75],
    "english": [78, 80, 92, 70],
}

df = pd.DataFrame(students)


# Display DataFrame information
print("=== Student DataFrame ===")
print(df)

print("\n=== DataFrame Properties ===")
print(f"Shape: {df.shape}")
print(f"Rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")

print("\n=== First Rows ===")
print(df.head(2))
print(df.tail(2))

print("\n=== Data Types ===")
print(df.dtypes)
