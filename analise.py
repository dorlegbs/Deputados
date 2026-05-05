import streamlit as st

import pandas as pd

url = "https://raw.github.com/dorlegbs/Deputados/blob/main/deputados_2022.csv"

df = pd.read_csv("deputados_2022.csv")

df.datafram(df)


