import pandas as pd
import joblib

def load_model():
    return joblib.load("attrition_model.pkl")

def predict_risk(model, df):
    predictions = model.predict_proba(df)[:,1]
    return predictions
