# 📘 Developer Notes – Telematics Insurance Project

## Overview
This proof-of-concept demonstrates an **AI-driven telematics pricing system** that collects simulated driving data, analyzes driver behavior, and calculates risk-based insurance premiums.

The project is organized into:
- **Data simulation & modeling (src/ml)**  
- **API backend with FastAPI (src/api)**  
- **Interactive UI with Streamlit (src/ui)**  

## Key Features
- **Simulated Telematics Data:** Speed, braking, night driving, distance.
- **ML Model:** Linear regression with positive weights ensures monotonicity — risk always increases with speed or braking.
- **API:** `/predict` endpoint returns a `risk_score` (0–100) and a calculated `premium`.
- **UI:** Streamlit dashboard lets users adjust sliders and instantly see their risk and pricing level.

## Risk Model
- Trained on simulated trip data (5–50 drivers × 5–50 trips).  
- Factors used:
  - `avg_speed` — higher → higher risk.
  - `harsh_brakes` — frequent braking → higher risk.
  - `night_drive` — Boolean; driving at night adds moderate risk.
  - `distance_miles` — small contribution.
- Smoothed thresholds:
  - Safe Driver: <65  
  - Moderate: 65–77.9  
  - High Risk: ≥78  
- Custom scaling in `pricing.py` makes the risk increase gradually — not abruptly.

## Premium Model
- **Base Premium:** \$120  
- **Dynamic Adjustment:**
  - Safe → cheaper  
  - Moderate → base ± small margin  
  - High → higher premium
- **Corridor:** (0.5–1.6) prevents extreme prices.  
- Formula ensures fairness:

 
##  File structure overview

src/
  ml/
    simulate.py        # generate telematics trips (GPS/speed/brakes/night)
    train_model.py     # fit monotonic model, save models/model.pkl
  api/
    app.py             # FastAPI app: /predict
    pricing.py         # load model, predict risk, calculate premium
    schemas.py         # Pydantic schemas
  ui/
    app_streamlit.py   # Streamlit dashboard
data/                  # trips.csv (simulated)
models/                # model.pkl
docs/                  # (optional) notes.md, design.md
.streamlit/config.toml # (optional) theme
requirements.txt
README.md