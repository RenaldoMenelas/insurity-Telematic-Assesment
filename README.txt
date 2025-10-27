Public Repository:
https://github.com/RenaldoMenelas/insurity-Telematic-Assesment

Setup & Run Instructions:
1. Clone the repository:
   git clone https://github.com/RenaldoMenelas/insurity-Telematic-Assesment.git
   cd insurity-Telematic-Assesment (if not already inside)

2. Create and activate a virtual environment:
   macOS / Linux:
      python3 -m venv venv
      source venv/bin/activate
   Windows (PowerShell):
      python -m venv venv
      .\venv\Scripts\Activate.ps1

3. Install dependencies:
   pip install -r requirements.txt

4. Create data folder (if missing):
   mkdir data

5. Generate simulated data and train model:
   python src/ml/simulate.py
   python src/ml/train_model.py

6. Start backend API:
   uvicorn src.api.app:app --reload

💡 Note:
You only need to activate the environment once per terminal session.
If you open a new terminal (for example, to run Streamlit or FastAPI),
run the source venv/bin/activate (or Windows equivalent) again —
unless you’re using a split terminal in VS Code, which often keeps the same environment active automatically.

7. Open a new terminal (reactivate venv) and launch Streamlit UI:
   streamlit run src/ui/app_streamlit.py

Evaluation Steps:
- Open http://127.0.0.1:8501 to view the dashboard.
- Adjust average speed, harsh brakes, and night drive toggles.
- Observe the calculated risk score and dynamic premium.

Notes:
- Model: Linear Regression with non-negative weights.
- Data: Simulated telematics trips (avg_speed, harsh_brakes, night_drive, distance_miles).
- Output: Risk score scaled from 0–100 and converted to insurance premium using corridor logic.
- Tools used: FastAPI, Streamlit, scikit-learn, pandas, numpy.
- Future improvement: Incorporate GPS-based regional risk modifiers (city/state).

Author: Renaldo Menelas



      
