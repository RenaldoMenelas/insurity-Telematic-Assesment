import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import os

# Loads the simulated data
df = pd.read_csv("data/trips.csv")

# Aggregate by driver_id to create driver-level features
features = df.groupby("driver_id").agg({
    "avg_speed": "mean",
    "max_speed": "mean",
    "harsh_brakes": "mean",
    "night_drive": "mean",
    "distance_miles": "sum"
}).reset_index()

# Create a simulated "risk_score" — higher speed + more braking = riskier
risk_raw = (
    0.6  * features["avg_speed"] +      # speed increases risk
    3.0  * features["harsh_brakes"] +   # braking increases risk
    25.0 * features["night_drive"] +    # night driving increases risk
    0.02 * features["distance_miles"]   # small mileage effect
)

# 4) Scale to 0–100 for stable, readable scores
min_r, max_r = risk_raw.min(), risk_raw.max()
features["risk_score"] = 100 * (risk_raw - min_r) / (max_r - min_r)

# 4) Convert raw model outputs to a 0–100 normalize range so all drivers' risk scores are easy to compare
X = features[["avg_speed", "harsh_brakes", "night_drive", "distance_miles"]]
y = features["risk_score"]

# Fit linear regression model to learn risk prediction pattern
model = LinearRegression()
model.fit(X, y)

# Save the model to /models folder
os.makedirs("models", exist_ok=True)
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as models/model.pkl")
