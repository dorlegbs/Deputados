import panda as pd

url = "https://github.com/dorlegbs/Deputados/blob/main/deputados_2022.csv"

df = pd.read_csv(url)

df_masculino = [df[df["sexo"] == 'M']
nome_masculino = df_masculino["nome"]

print(nomes_masculinos)

nomes_masculinos.to_csv("nomes_masculinos.csv", index=False)
