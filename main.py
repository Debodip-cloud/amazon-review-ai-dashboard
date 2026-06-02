from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import traceback

app = FastAPI(title="Amazon Review AI")

try:
    pipeline = joblib.load("amazon_review_pipeline_FIXED.pkl")
    print("Pipeline loaded successfully")
except Exception as e:
    print("Pipeline loading failed")
    print(e)
    pipeline = None


class ReviewInput(BaseModel):
    review_text: str


@app.get("/")
def home():
    return {"message": "Amazon Review AI API Running"}


@app.post("/predict")
def predict(data: ReviewInput):
    try:
        if pipeline is None:
            return {"error": "Pipeline not loaded"}

        prediction = pipeline.predict([data.review_text])[0]
        probabilities = pipeline.predict_proba([data.review_text])[0]

        label = "Positive" if prediction == 1 else "Negative"

        return {
            "prediction": label,
            "confidence": round(float(max(probabilities)), 4),
            "negative_probability": round(float(probabilities[0]), 4),
            "positive_probability": round(float(probabilities[1]), 4)
        }

    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }