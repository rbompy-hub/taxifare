import os
import pandas as pd
from fastapi import FastAPI
import joblib
from src.taxifare.predict import load_model, predict


app = FastAPI()

coup_de_pouce = "👍👍👍👍👍👍👍👍"
model = load_model("models/linreg_pipeline.joblib")


@app.get("/")
def root():
    """Root endpoint returning a coup de pouce"""
    return {"wsh" : coup_de_pouce}


@app.get("/predict")
def dummy(pickup_datetime: str, pickup_longitude: float, pickup_latitude: float, dropoff_longitude: float, dropoff_latitude: float, passenger_count: int):
    """model prediction"""
    X_pred = pd.DataFrame({
        "pickup_datetime": [pd.to_datetime(pickup_datetime, utc=True)],
        "pickup_longitude": [pickup_longitude],
        "pickup_latitude": [pickup_latitude],
        "dropoff_longitude": [dropoff_longitude],
        "dropoff_latitude": [dropoff_latitude],
        "passenger_count": [passenger_count],
    })

    y_pred = predict(model, X_pred)

    return {"reponse" : float(y_pred.item())}
