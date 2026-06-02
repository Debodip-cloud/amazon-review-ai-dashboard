import streamlit as st
import joblib

st.title("Amazon Review AI Predictor")

@st.cache_resource
def load_model():
    return joblib.load("amazon_review_pipeline_FIXED.pkl")

pipeline = load_model()

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
st.markdown("---")

st.link_button(
    "View Full Analytics Dashboard",
    "https://app.powerbi.com/reportEmbed?reportId=01aa2633-8515-4806-aa5b-4ea0b74bded0&autoAuth=true&ctid=5f86736b-ef43-4992-9624-06dc6eeaf097"
)
st.write(
    "Download the Power BI dashboard file and open it using Power BI Desktop."
)

st.link_button(
    "Download Power BI Dashboard (.pbix)",
    "https://github.com/Debodip-cloud/amazon-review-ai-dashboard/raw/main/amazon_customer_review.pbix"
)
