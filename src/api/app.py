# src/api/app.py
from fastapi import FastAPI, Response
from src.api.schemas import DriverData, PredictionResponse
from src.api.pricing import predict_risk, calculate_premium

app = FastAPI(title="Telematics Insurance API")

#Root endpoint — checking to confirm the API is running
@app.get("/")
def home():
    return {"message": "Telematics API is running 🚗"}

#Handles browser requests for /favicon.ico (prevents 404 spam in logs
@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204) 

#/predict endpoint — accepts driver input data, runs ML model + pricing logic,
# and returns a validated response containing risk score and premium.
@app.post("/predict", response_model=PredictionResponse)
def predict(data: DriverData):
    risk_score = predict_risk(data)
    premium = calculate_premium(risk_score)
    return PredictionResponse(risk_score=risk_score, premium=premium)
