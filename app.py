import streamlit as st
import requests

st.title("Amazon Review AI Predictor")

st.write("Type an Amazon customer review and the model will predict whether it is positive or negative.")

review_text = st.text_area(
    "Enter review text:",
    "Amazon delivery was late and customer service refused to refund my money."
)

if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"review_text": review_text}
    )

    result = response.json()

    st.subheader("Prediction Result")
    st.write("Prediction:", result["prediction"])
    st.write("Confidence:", result["confidence"])
    st.write("Negative Probability:", result["negative_probability"])
    st.write("Positive Probability:", result["positive_probability"])