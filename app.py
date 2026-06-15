import streamlit as st
import joblib
import numpy as np

model = joblib.load("models/churn_model (2).pkl")

scaler = joblib.load("models/scaler (1).pkl")


st.title("🏦 Banking Customer Churn Prediction")


credit = st.number_input(
"Credit Score",
300,
900
)


age = st.number_input(
"Age",
18,
100
)


tenure = st.slider(
"Tenure",
0,
10
)


balance = st.number_input(
"Balance"
)


products = st.selectbox(
"Number of Products",
[1,2,3,4]
)


salary = st.number_input(
"Estimated Salary"
)


active = st.selectbox(
"Active Member",
["Yes","No"]
)


card = st.selectbox(
"Has Credit Card",
["Yes","No"]
)


gender = st.selectbox(
"Gender",
["Male","Female"]
)


country = st.selectbox(
"Geography",
["France","Germany","Spain"]
)

geo_Germany = 1 if country=="Germany" else 0
geo_Spain = 1 if country=="Spain" else 0

gender_male = 1 if gender=="Male" else 0

card_value = 1 if card=="Yes" else 0

active_value = 1 if active=="Yes" else 0


if st.button("Predict"):


    data=np.array(
    [
    credit,
    age,
    tenure,
    balance,
    products,
    card_value,
    active_value,
    salary,
    geo_Germany,
    geo_Spain,
    gender_male
    ]
    )


    data=data.reshape(1,-1)


    data=scaler.transform(data)


    prediction=model.predict(data)


    probability=model.predict_proba(data)[0][1]


    if prediction[0]==1:

        st.error(
        "⚠️ Customer is likely to churn"
        )

        st.write(
        f"Churn Probability: {probability:.2%}"
        )


    else:

        st.success(
        "Customer is likely to stay"
        )

        st.write(
        f"Retention Probability: {(1-probability):.2%}"
        )
