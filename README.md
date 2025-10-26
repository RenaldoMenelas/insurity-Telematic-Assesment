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

## ⚙️ Run Locally Clone the repoository
1. ```git clone https://github.com/RenaldoMenelas/insurity-Telematic-Assesment.git```
2. ```cd Insurity-Telematics-Assesment```
#  create and activate a virtual environment*
  macOS / Linux <br>
3. ```python3 -m venv venv``` <br> 
4. ```source venv/bin/activate```
  
  Windows (PowerShell)<br>
3. ```python3 -m venv venv```<br>
4. ```.\venv\Scripts\Activate.ps1```

  Install dependencies  
5. ```pip install -r requirements.txt```
# create folder, simulate data, train data
6.``` mkdir -p data``` <br>
7. ```python3 src/ml/simulate.py```<br>
8. ```python3 src/ml/train_model.py```
# start backend Api
9. ```uvicorn src.api.app:app --reload ```<br>
10. Activate venv again in the new terminal
11. ```source venv/bin/activate```  or ```.\venv\Scripts\Activate.ps1``` on Windows
12. ```streamlit run src/ui/app_streamlit.py```

<img width="1421" height="![Uploading Screenshot 2025-10-26 at 3.42.50 PM.png…]()
817" alt="Screenshot 2025-10-26 at 4 27 20 AM" src="https://github.com/user-attachments/assets/e5f2e66c-0f18-4c3a-8133-829ebc765657" />

<img width="1426" height="814" alt="Screenshot 2025-10-26 at 3 46 45 PM" src="https://github.com/user-attachments/assets/ffd7c71a-a0fc-40be-9b2d-573e689af0d4" />


README.md
