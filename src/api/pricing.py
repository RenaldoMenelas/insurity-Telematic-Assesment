import os
import pickle
import numpy as np
from pathlib import Path
from src.api.schemas import DriverData

# Load the trained model once when the API starts.
MODEL_PATH = Path("models/model.pkl")
if MODEL_PATH.exists():
    with open(MODEL_PATH, "rb") as f:
        MODEL = pickle.load(f)
else:
    MODEL = None  # Will trigger a clear error if the model isn't trained yet.
def predict_risk(driver_data: DriverData) -> float:
    """Use the trained model to predict a driver's risk score."""
    if MODEL is None:
        raise RuntimeError("Model not found. Run 'python src/ml/train_model.py' first.")

    # Prepare the data for prediction
    X = np.array([[
        driver_data.avg_speed,
        driver_data.harsh_brakes,
        int(driver_data.night_drive),
        driver_data.distance_miles
    ]])

    # Get raw model prediction
    risk = float(MODEL.predict(X)[0])

    # --- Custom scaling to make risk climb more gradually ---
    if risk < 50:
        risk = 50 + (risk - 50) * 0.3   # gentle slope for safe drivers
    elif risk < 65:
        risk = 55 + (risk - 55) * 0.6   # moderate rise
    elif risk < 78:
        risk = 65 + (risk - 65) * 0.8   # steeper curve toward high risk
    else:
        risk = min(risk, 100.0)          # cap at 100 max

    # Round the value
    risk = round(risk, 2)

    # Ensure risk never goes below 0
    if risk < 1:
        risk = 0.0

    # Print debug info (like console.log)
    print(f"[DEBUG] avg_speed={driver_data.avg_speed}, brakes={driver_data.harsh_brakes}, night={driver_data.night_drive}, miles={driver_data.distance_miles} -> risk={risk}")

    return risk

   
def calculate_premium(risk_score: float) -> float:
    """Converts a risk score into a monthly insurance premium."""
    base = 120.0        # Base monthly premium in dollars.
    risk_ref = 30.0     # Average risk level (neutral reference point).
    scale = 40.0        # Spread factor controlling price sensitivity.
    k = 0.8             # How strongly risk affects price.
    corridor = (0.89, 1.40)  # ±30% cap to prevent extreme pricing.

    # Compute premium adjustment factor based on risk difference.
    z = (risk_score - risk_ref) / scale
    factor = 1 + k * z
    factor = max(corridor[0], min(corridor[1], factor))

    premium = round(base * factor, 2)
    return premium
