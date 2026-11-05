
# ============================================================
# Stage 09 - Load Trained Model and Predict
# ============================================================

from pathlib import Path

import joblib
import pandas as pd


# Load an already trained model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models/house_price_model.joblib"

model = joblib.load(MODEL_PATH)


# Example input with the same feature schema
new_data = pd.DataFrame([{
    "MedInc": 3.5,
    "HouseAge": 20.0,
    "AveRooms": 5.0,
    "AveBedrms": 1.0,
    "Population": 1000.0,
    "AveOccup": 3.0,
    "Latitude": 34.0,
    "Longitude": -118.0
}])


# Generate a prediction without training
prediction = model.predict(new_data)[0]

print("=== Prediction Using a Saved Model ===")
print(f"Predicted target: {prediction:.4f}")
print(f"Predicted value: ${prediction * 100000:,.2f}")

print("\nLearned coefficients:")
print(model.coef_)
