# Telematics-Based Insurance Pricing (MVP)

## Overview
Proof-of-concept showing how telematics data can drive fairer, usage-based auto insurance pricing.

## Components
| Folder | Purpose |
|---------|----------|
| src/ml | Data simulation & model training |
| src/api | FastAPI backend (risk & pricing endpoints) |
| src/ui | Streamlit front-end dashboard |
| data | Simulated trip data |
| models | Trained model (.pkl) |

## Workflow
1. `python src/ml/simulate.py` → generate telematics trips  
2. `python src/ml/train_model.py` → train risk model  
3. `uvicorn src.api.app:app --reload` → start API  
4. `streamlit run src/ui/app_streamlit.py` → open dashboard  

## Key Features
- Monotonic ML model (non-negative weights)
- Smooth sigmoid calibration (Safe→Moderate→High)
- Dynamic premium calculation
- Deterministic outputs (no random noise)

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
