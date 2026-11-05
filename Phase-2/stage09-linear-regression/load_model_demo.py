from pathlib import Path

import joblib

model_path = Path(__file__).resolve().parent / "house_price_model.joblib"

loaded_model = joblib.load(model_path)

print("=== Loaded Model ===")
print("Coefficients:", loaded_model.coef_)
print("Intercept:", loaded_model.intercept_)