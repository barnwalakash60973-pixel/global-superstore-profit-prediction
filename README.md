# 🏪 Global Superstore Profit Prediction

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

**End-to-end Machine Learning system for profit forecasting using ensemble learning, SHAP explainability, FastAPI, and Streamlit.**

---

## 📌 Overview

This project analyzes the Global Superstore dataset and predicts order-level profit using machine learning. It combines exploratory data analysis, statistical testing, ensemble learning, explainable AI (SHAP), FastAPI backend services, and an interactive Streamlit dashboard to generate business insights and profit forecasts.

---

## 🌐 Live Demo

### Frontend

https://global-superstore-profit-prediction-5chk.onrender.com/

### Backend API

https://global-superstore-profit-prediction.onrender.com/docs

---

## 🎯 Objectives

* Analyze sales and profitability patterns
* Measure the impact of discounts on profit
* Identify key profit drivers
* Predict profit for future orders
* Provide explainable predictions using SHAP

---

## 📊 Dataset

**Global Superstore Dataset**

* 51,289 Orders
* 140+ Countries
* Multiple Product Categories
* Sales, Profit, Discount, Shipping Cost
* Customer Segments and Regions

---

## 🧪 Statistical Hypothesis Testing

The project validates business assumptions using statistical testing:

| Hypothesis                                   | Test Used            |
| -------------------------------------------- | -------------------- |
| Profit differs across customer segments      | Kruskal-Wallis Test  |
| Technology is more profitable than Furniture | Mann-Whitney U Test  |
| Discount negatively impacts profit           | Spearman Correlation |
| Profit differs across markets                | Kruskal-Wallis Test  |

---

## 🤖 Machine Learning Solution

### Models

* Random Forest Regressor
* Gradient Boosting Regressor
* Weighted Ensemble Model

### Final Ensemble

```text
Profit Prediction = 0.4 × Random Forest + 0.6 × Gradient Boosting
```

### Model Performance

| Metric   | Score |
| -------- | ----- |
| MAE      | 35.51 |
| RMSE     | 83.96 |
| R² Score | 0.77  |

The ensemble model achieved strong predictive performance while maintaining interpretability.

---

## 🔍 Explainable AI with SHAP

SHAP (SHapley Additive Explanations) was integrated to improve model transparency and explain individual predictions.

Key benefits:

* Transparent model predictions
* Business-friendly interpretation
* Identification of important profit drivers
* Improved stakeholder trust

The Streamlit application provides real-time SHAP explanations alongside each profit prediction.

---

## 🖥️ Application Features

* Interactive KPI Dashboard
* Exploratory Data Analysis
* Business Insights
* Profit Prediction Interface
* Real-Time Profit Forecasting
* SHAP-Based Explanations
* FastAPI Backend
* Streamlit Frontend
* Dockerized Deployment

---

## 📷 Application Screenshots

### KPI Dashboard

![KPI Dashboard](streamlit_app/Images/dashboard.png)

### Feature Importance Analysis

![Feature Importance](streamlit_app/Images/rf_feature_importance.png)

### Profit Prediction Interface

![Profit Prediction](streamlit_app/Images/prediction_result.png)

---

## 📂 Project Structure

```text
global-superstore-profit-prediction/
│
├── backend/
│   ├── main.py
│   ├── schema.py
│   ├── constants.py
│   ├── feature_engineering.py
│   └── models/
│       └── ensemble_pipeline.pkl
│
├── streamlit_app/
│   ├── app.py
│   └── Images/
│
├── notebooks/
│   └── kaggle_training_notebook.ipynb
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
├── .dockerignore
└── README.md
```

### 🧠 Model Training

Model training and evaluation were performed in Kaggle Notebooks. The final ensemble pipeline was exported and integrated into the FastAPI backend for deployment.

---

## 🛠️ Tech Stack

### Data Science & Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* SHAP

### Backend & Frontend

* FastAPI
* Streamlit

### Deployment

* Docker
* Joblib

---

## 🚀 Run Locally

### Option 1: Docker (Recommended)

Build and start the application:

```bash
docker compose up --build
```

Access:

* Frontend: http://localhost:8501
* Backend API Docs: http://localhost:8000/docs

---

### Option 2: Manual Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI Backend:

```bash
uvicorn backend.main:app --reload
```

Start Streamlit Frontend:

```bash
streamlit run streamlit_app/app.py
```

Access:

* Frontend: http://localhost:8501
* Backend API Docs: http://localhost:8000/docs

---

## 📬 Connect With Me

**Akash Kumar Barnwal**

* LinkedIn: https://www.linkedin.com/in/akash-kumar-barnwal-31968a380/
* GitHub: https://github.com/barnwalakash60973-pixel
