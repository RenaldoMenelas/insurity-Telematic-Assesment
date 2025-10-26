Setup Instructions
1. git clone https://github.com/RenaldoMenelas/insurity-Telematic-Assesment.git
2. cd insurity-Telematic-Assesment (make sure yuor in root of the insurity-Telematic-Assesment file)

Run these in terminal
       |
       V   ( macOS / Linux)        Windows (PowerShell)
python3 -m venv venv                 python -m venv venv
source venv/bin/activate             \venv\Scripts\Activate.ps1
       |
       V 
pip install -r requirements.txt
       |
       V
mkdir data
       |
       V 
python src/ml/simulate.py
python src/ml/train_model.py
       |
       V
uvicorn src.api.app:app --reload
       |
       V   (open a new terminal within same folder and run this activate env)
source venv/bin/activate
       |        
       V
streamlit run src/ui/app_streamlit.py


      