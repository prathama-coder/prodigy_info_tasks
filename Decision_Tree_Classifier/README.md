# 🏦 Bank Marketing Subscription Prediction using Decision Tree

A Machine Learning web application that predicts whether a customer is likely to subscribe to a bank term deposit based on demographic and marketing campaign information.

---

## 📌 Project Overview

This project uses a **Decision Tree Classifier** trained on the **UCI Bank Marketing Dataset** to predict customer subscription decisions.

The application provides an interactive Streamlit dashboard where users can enter customer information and receive real-time predictions.

---

## 🚀 Features

- Interactive Streamlit Dashboard
- Decision Tree Classifier
- Customer Profile Input
- Marketing Campaign Details
- Real-time Prediction
- Confidence Score
- Feature Importance Visualization
- Customer Summary Table

---

## 🖥️ Dashboard Preview

### Main Dashboard

![Dashboard](dashboard.PNG)

---

### Prediction Result

![Prediction](prediction_result.PNG)

---

### Feature Importance

![Feature Importance](feature_importance.PNG)

---

## 📊 Dataset

**Dataset:** UCI Machine Learning Repository - Bank Marketing Dataset

Features Used:

- Age
- Job
- Marital Status
- Education
- Credit Default
- Balance
- Housing Loan
- Personal Loan
- Contact Type
- Contact Day
- Month
- Call Duration
- Campaign Contacts
- Previous Contacts
- Previous Campaign Outcome

Target Variable:

- Customer Subscription (Yes / No)

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Matplotlib

---

## 📂 Project Structure

```
Decision-Tree-Classifier/
│
├── app.py
├── bank_marketing_decision_tree.pkl
├── bank-full.csv
├── requirements.txt
├── README.md
├── images/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Decision-Tree-Classifier.git
```

Move into the project

```bash
cd Decision-Tree-Classifier
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📈 Model Performance

| Metric | Value |
|---------|------:|
| Algorithm | Decision Tree Classifier |
| Accuracy | **89.5%** |
| Features | 16 |
| Dataset | UCI Bank Marketing |

---

## 🎯 Future Improvements

- Random Forest Classifier
- XGBoost Model
- Hyperparameter Tuning
- Model Comparison Dashboard
- SHAP Explainability
- Cloud Deployment

---

## 👩‍💻 Author

**Prathama Debnath**

B.Tech Computer Science (AI & ML)

SRM Institute of Science and Technology

GitHub: https://github.com/prathama-coder