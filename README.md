# ⚡ Electricity Production Prediction

A Machine Learning based web application that predicts electricity production using historical electricity data.

The project uses **XGBoost** for prediction and **FastAPI** as the backend API. A simple HTML, CSS, and JavaScript frontend is integrated with the FastAPI backend to allow users to enter prediction parameters and receive a predicted electricity production value.

---

## 📌 Project Overview

Electricity production varies depending on different factors such as country, time, and energy product.

This project uses historical electricity data to train a machine learning model that can estimate electricity production based on four input features:

- **Country**
- **Year**
- **Month**
- **Product**

The trained model is saved as a `.pkl` file and integrated into a FastAPI application.

---

## 🚀 Features

- 🔹 Machine Learning based electricity production prediction
- 🔹 XGBoost regression model
- 🔹 FastAPI REST API
- 🔹 Frontend built with HTML, CSS, and JavaScript
- 🔹 Input validation using Pydantic (Country, Product, Year, Month)
- 🔹 User-friendly prediction form
- 🔹 API and frontend integration using JavaScript `fetch()`
- 🔹 JSON based API communication

---

## 🛠️ Technologies Used

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic
- Pandas
- Scikit-learn
- XGBoost

### Frontend
- HTML5
- CSS3
- JavaScript (Fetch API)

### Machine Learning
- XGBoost
- Scikit-learn
- Pandas
- NumPy

---

## 📂 Project Structure

```text
Electricity-Production-Prediction/
│
├── app.py
├── pipe.pkl
├── Business-Startups.csv
├── Business-Startup.ipynb
├── requirements.txt
├── README.md
│
└── frontend/
   └── index.html
   └── images/
       └── lightning.png
    └── static/
        ├── style.css
        └── script.js

    
