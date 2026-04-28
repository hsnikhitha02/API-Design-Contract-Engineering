from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Sentiment API", version="1.0")

# Request Schema (API Contract)
class Input(BaseModel):
    text: str = Field(..., min_length=1, max_length=200)

# Response Schema
class Output(BaseModel):
    prediction: str

# Business Logic
def predict_sentiment(text: str):
    if "good" in text.lower():
        return "positive"
    return "negative"

# Versioned API Endpoint
@app.post("/v1/predict", response_model=Output)
def predict(data: Input):
    try:
        result = predict_sentiment(data.text)
        return {"prediction": result}
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")