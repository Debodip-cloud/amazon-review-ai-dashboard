# Amazon Review Intelligence Platform

## Overview

Amazon Review Intelligence Platform is an end-to-end Data Science and Machine Learning project that combines Natural Language Processing (NLP), Sentiment Analysis, Interactive Business Intelligence, and Cloud Deployment.

The platform analyzes Amazon customer reviews to identify customer sentiment, complaint patterns, geographical trends, and business insights. Users can interact with a live AI-powered sentiment prediction application and explore analytical insights through a Power BI dashboard.

---

## Live Demo
<img width="904" height="609" alt="image" src="https://github.com/user-attachments/assets/0fedd727-684a-4ecf-9818-ac0e2e3c4812" />
<img width="619" height="437" alt="image" src="https://github.com/user-attachments/assets/b41b470c-2c59-4d97-bd34-634e381e3113" />
<img width="602" height="422" alt="image" src="https://github.com/user-attachments/assets/95e47104-af4c-4e6e-aa20-4e780663c8d8" />
<img width="925" height="598" alt="image" src="https://github.com/user-attachments/assets/e7a7ee41-b8a9-4f4c-b280-9919cbc84760" />
<img width="828" height="441" alt="image" src="https://github.com/user-attachments/assets/c7411317-09f1-4867-acd4-8aa6366569ae" />





### AI Review Predictor

https://amazon-review-ai-dashboard-6kzvphhpeehcrfxrbrb8oi.streamlit.app/

### Power BI Dashboard

Download the dashboard file:

https://github.com/Debodip-cloud/amazon-review-ai-dashboard/raw/main/amazon_customer_review.pbix

---

## Project Architecture

```text
Amazon Customer Reviews
            │
            ▼
      Data Cleaning
            │
            ▼
     Feature Engineering
            │
            ▼
 TF-IDF Vectorization
            │
            ▼
 Logistic Regression Model
            │
            ▼
      Sentiment Prediction
            │
            ▼
     Streamlit Web App
            │
            ▼
      Power BI Dashboard
```

---

## Features

### AI-Powered Sentiment Prediction

* Real-time review sentiment analysis
* Positive and Negative sentiment classification
* Confidence score calculation
* Probability-based predictions

### Interactive Analytics Dashboard

* Executive Summary Dashboard
* Sentiment Analysis Dashboard
* Geographic Analysis Dashboard
* AI Model Overview Dashboard

### Business Insights

* Customer sentiment trends
* Complaint category analysis
* Country-level review distribution
* Rating distribution analysis
* Customer satisfaction indicators

---

## Technology Stack

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorization
* Logistic Regression
* Joblib Model Serialization

### Data Analysis

* Pandas
* NumPy

### Visualization

* Power BI
* Streamlit

### Deployment

* GitHub
* Streamlit Community Cloud

---

## Model Information

### Algorithm

Logistic Regression

### Feature Extraction

TF-IDF Vectorization

### Output Classes

* Positive
* Negative

### Example Prediction

**Input Review**

> Amazon delivery was late and customer service refused to refund my money.

**Prediction**

```text
Negative
Confidence: 97.19%
```

---

## Dashboard Pages

### Executive Summary

* Total Reviews
* Average Rating
* Average Sentiment Score
* Rating Distribution
* Complaint Category Analysis

### Sentiment Analysis

* Positive vs Negative Review Distribution
* Sentiment by Complaint Category

### Geographic Analysis

* Global Review Distribution Map
* Country-Level Customer Insights

### AI Review Predictor

* Model Overview
* Prediction Examples
* AI Deployment Information

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Debodip-cloud/amazon-review-ai-dashboard.git
cd amazon-review-ai-dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## Repository Structure

```text
amazon-review-ai-dashboard/
│
├── app.py
├── main.py
├── requirements.txt
├── runtime.txt
├── amazon_review_pipeline_FIXED.pkl
├── amazon_customer_review.pbix
└── README.md
```

---

## Future Enhancements

* Multi-class sentiment classification
* Transformer-based NLP models (BERT)
* Real-time dashboard integration
* Automated review monitoring
* Cloud-native API deployment
* Generative AI-powered review summarization

---

## Author

**Debodip Chowdhury**

Data Scientist | Machine Learning Engineer | Business Intelligence Enthusiast

GitHub:
https://github.com/Debodip-cloud

---

## License

This project is intended for educational, research, and portfolio purposes.
