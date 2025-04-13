import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Stock Prediction AI Dashboard")

st.markdown("Upload your feature CSV to view stock trends and predictions.")
file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.line_chart(df['Close'])
    st.line_chart(df['SMA_10'])