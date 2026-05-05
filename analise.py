import streamlit as st
import pandas as pd

df = pd.read_csv("deputados_2022.csv")

st.title("Consulta de Deputados por Partido")

partido_input = st.text_input("Digite a sigla do partido ").upper()

if partido_input:
    partido_input = partido_input.upper()

    df_filtrado = df[df["partido"].str.upper() == partido_input]

    if df_filtrado.empty:
        st.warning("Esse partido não existe.")
    else:
        st.subheader(f"Deputados do partido {partido_input}")
        st.write(df_filtrado["nome"])
        st.write(f"Total: {df_filtrado.shape[0]}")
