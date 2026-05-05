import streamlit as st
import pandas as pd

df = pd.read_csv("deputados_2022.csv")

st.dataframe(df)

st.title("Consulta de Deputados por Partido")

partido_input = st.text_input("Digite o partido ").upper()

