# 🏦 Banking Customer Churn Prediction System using Machine Learning

A Machine Learning based web application that predicts whether a banking customer is likely to churn or stay with the bank. The project uses customer demographic and banking information to identify churn patterns and provide churn probability predictions through an interactive Streamlit dashboard.

🔗 **Live Demo:**  
https://banking-churn-prediction-ml-krqcbnyfrhsl8arbdriion.streamlit.app/

---

## 📌 Project Overview

Customer retention is one of the biggest challenges for banking organizations. Losing customers affects revenue and long-term growth.

This project builds a classification model that analyzes customer attributes such as:

- Credit Score
- Age
- Tenure
- Account Balance
- Number of Products
- Credit Card Ownership
- Active Membership
- Estimated Salary
- Geography
- Gender

The trained Machine Learning model predicts:

- ✅ Customer likely to stay
- ⚠️ Customer likely to churn

along with the churn probability score.

---

# 🚀 Features

✔ Machine Learning based churn prediction  
✔ Interactive Streamlit web application  
✔ Customer input based prediction  
✔ Churn probability estimation  
✔ Scaled input processing  
✔ User-friendly interface  

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Machine Learning
- Scikit-Learn
- NumPy
- Pandas

## Model Deployment
- Streamlit

## Model Serialization
- Pickle / Joblib

## Development Environment
- Google Colab
- VS Code

---

# 📂 Project Structure

```

Banking-Churn-Prediction-ML
│
├── app.py
│
├── models
│   ├── churn_model.pkl
│   └── scaler.pkl
├── PowerBI
|     ├── Bank_Customer_Churn_Analysis_Dashboard_Debdut_Nandy.pbix
├── data
│   └── Churn_Modeling.csv
│
├── requirements.txt
│
└── README.md

```

---

# 📊 Dataset Information

The project uses a banking customer dataset containing information about customers and their churn status.

### Important Features:

| Feature | Description |
|---|---|
| CreditScore | Customer credit score |
| Age | Customer age |
| Tenure | Years with bank |
| Balance | Account balance |
| NumOfProducts | Number of bank products |
| HasCrCard | Credit card ownership |
| IsActiveMember | Active customer status |
| EstimatedSalary | Customer salary estimate |
| Geography | Customer country |
| Gender | Customer gender |

Target Variable:


Exited


- 0 → Customer stays
- 1 → Customer churns

---

# 📊 Dashboard

<img src="Screenshot 2026-06-15 105358.png" width="700">

---


# 🤖 Machine Learning Workflow

## 1. Data Collection

Loaded banking customer dataset.

## 2. Data Preprocessing

Performed:

- Missing value handling
- Encoding categorical variables
- Feature scaling

## 3. Model Training

Multiple classification algorithms were evaluated.

Models considered:

- Logistic Regression
- Random Forest
- Decision Tree
- Gradient Boosting

Best performing model was selected.

## 4. Model Saving

The trained model and scaler were saved:



churn_model.pkl
scaler.pkl


---

# 🌐 Streamlit Application

The application allows users to enter customer details:

Example:


Credit Score: 650
Age: 40
Balance: 50000
Active Member: Yes


The model returns:


Customer is likely to stay

Retention Probability: 82%


or


Customer is likely to churn

Churn Probability: 75%


---

# ▶️ Run Locally

Clone repository:

```bash
git clone https://github.com/yourusername/Banking-Churn-Prediction-ML.git
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

# 📦 Requirements

```
streamlit
numpy
pandas
scikit-learn
joblib
```

---

# 📈 Future Improvements

* Add customer risk segmentation
* Add model comparison dashboard
* Add SHAP explainability
* Connect with real banking databases
* Deploy using cloud platforms

---

# 👨‍💻 Author

**Debdut Nandy**

Machine Learning | Data Analytics | Python


---

⭐ If you found this project useful, consider giving it a star!
