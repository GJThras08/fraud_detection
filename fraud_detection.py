import streamlit as st
import pandas as pd
import joblib as joblib

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transaction detailes and use the predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value = 0.0, value = 1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_values = 0.0, value = 10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value = 0.0, value = 9000.0)