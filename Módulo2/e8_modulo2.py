import csv
import pandas as pd


dados = [["Nome", "Idade"], ["Ana", 25], ["Carlos", 30]]

with open("tabela.csv", mode = "w", newline = "") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)
    
# Ler o arquivo CSV e exibir como tabela
df = pd.read_csv("tabela.csv")
print(df)