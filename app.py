import streamlit as st
import joblib

st.set_page_config(page_title="Amazon Review AI Predictor", page_icon="🤖")

@st.cache_resource
def load_model():
    return joblib.load("amazon_review_pipeline_FIXED.pkl")

pipeline = load_model()

st.title("Amazon Review AI Predictor")

st.write(
    "Type an Amazon customer review and the model will predict whether it is positive or negative."
)

review_text = st.text_area(
    "Enter review text:",
    "Amazon delivery was late and customer service refused to refund my money."
)

if st.button("Predict"):
    prediction = pipeline.predict([review_text])[0]
    probabilities = pipeline.predict_proba([review_text])[0]

    label = "Positive" if prediction == 1 else "Negative"

    st.subheader("Prediction Result")
    st.write("Prediction:", label)
    st.write("Confidence:", round(float(max(probabilities)), 4))
    st.write("Negative Probability:", round(float(probabilities[0]), 4))
    st.write("Positive Probability:", round(float(probabilities[1]), 4))
