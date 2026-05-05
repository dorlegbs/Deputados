import panda as pd

url = "https://github.com/dorlegbs/Deputados/blob/main/deputados_2022.csv"

df = pd.read_csv(url)

df_masculino = [df[df["sexo"] == M
