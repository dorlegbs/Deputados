import streamlit as st
import pandas as pd

df = pd.read_csv("deputados_2022.csv")

st.dataframe(df)

partido_input = input("Digite o partido ").upper()

st.inputbox
