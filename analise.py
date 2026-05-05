import streamlit as st
import pandas as pd

df = pd.read_csv("deputados_2022.csv")

st.dataframe(df)


df_masculino = df[df["sexo"] == "M"]
nomes_masculinos = df_masculino["nome"]

print(nomes_masculinos)

nomes_masculinos.to_csv("nomes_masculinos.csv", index=False)


