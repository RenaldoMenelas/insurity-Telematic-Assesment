## Encountered Issues & Fixes

| Issue | Description | Fix / Resolution |
|--------|--------------|------------------|
| **Missing dependencies (FastAPI, sklearn, Uvicorn)** | Initial environment didn’t have required libraries. | Created and activated a virtual environment (`python3 -m venv venv`) and installed dependencies via `pip install -r requirements.txt`. |
| **FileNotFoundError: data/trips.csv** | Model training ran before simulation file existed. | Ran `simulate.py` first to generate the sample dataset. |
| **ModuleNotFoundError: sklearn** | scikit-learn not installed in virtual env. | Re-installed in the active environment (`pip install scikit-learn`). |
| **Risk score changing randomly** | Random seeds in simulation made predictions unstable. | Removed `random.seed()` and `np.random.seed()` to keep deterministic model behavior. |
| **Abrupt risk jumps between Safe/Moderate/High** | Raw regression output changed too fast. | Added a custom scaling function to smooth risk growth. |
| **Premium not decreasing for safe drivers** | Corridor range too narrow. | Expanded range `0.89, 1.40` and adjusted formula sensitivity to reward safe drivers. |
| **UI flicker when using sliders** | Streamlit re-ran on every slider movement. | Wrapped inputs inside `st.form()` so the app only recomputes when pressing *Calculate Premium*. |
| **favicon.ico 404 warning** | Browser requested favicon by default. | Added optional route or ignored warning (harmless). |

---

### 💡 Takeaway
Each fix improved **stability**, **clarity**, and **user experience**, showing how backend logic, ML scaling, and frontend updates work together in a clean, production-like workflow.