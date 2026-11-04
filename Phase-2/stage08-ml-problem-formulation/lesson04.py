
# ============================================================
# Stage 08 - Lesson 04: Stratification and Data Leakage
# ============================================================

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


wine = load_wine(as_frame=True)

X = wine.data
y = wine.target


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Learn scaling parameters only from training data
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


print("=== Class Distribution ===")

print("\nTraining proportions:")
print(y_train.value_counts(normalize=True).sort_index())

print("\nTest proportions:")
print(y_test.value_counts(normalize=True).sort_index())


print("\n=== Feature Scaling ===")
print(f"Training mean: {X_train_scaled.mean():.6f}")
print(f"Training std: {X_train_scaled.std():.6f}")

print(f"Test shape: {X_test_scaled.shape}")
