from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
scaler = joblib.load("models/scaler.pkl")
iso = joblib.load("models/isolation_forest.pkl")
xgb = joblib.load("models/xgboost_model.pkl")

@app.post("/predict")
def predict(record: dict):
    df = pd.DataFrame([record])
    X_scaled = scaler.transform(df)
    prediction = xgb.predict(X_scaled)[0]
    proba = xgb.predict_proba(X_scaled)[0][1]
    risk_score = int(proba * 100)
    risk_level = "High" if risk_score > 70 else "Medium" if risk_score > 30 else "Low"
    return {"riskScore": risk_score, "riskLevel": risk_level, "reason": "Model-flagged deviation"}  