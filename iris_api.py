from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Define input schema
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Load model and target names
model, target_names = joblib.load("iris_model.pkl")

app = FastAPI(title="Iris Flower Classification API")

@app.post("/predict")
def predict_species(features: IrisFeatures):
    input_df = pd.DataFrame([features.dict()])
    pred = model.predict(input_df)[0]
    species = target_names[pred]
    return {"predicted_species": species}
