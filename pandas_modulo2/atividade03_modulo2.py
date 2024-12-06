
import pandas as pd 

#3.1 criacao de dataframe
dados = {
    #linhas  #colunas
    "Aluno": ["Joao", "Maria", "Jose", "Ana"],
    "Nota 1": [7.5, 8.2, 6.9, 9.1],
    "Nota 2": [8.0, 7.5, 6.5, 9.5]
}
df = pd.DataFrame(dados)

#3.2 exibir apenas a coluna aluno
print(df["Aluno"])

#3.3 Exiba apenas a primeira linha do DataFrame
print(df.iloc[0])

#3.4 Exiba a média das notas de Nota 1 e Nota 2 para o aluno José
jose = df.iloc[0]  #metodo iloc para filtrar a linha do aluno "Jose" pelo indice
media = (jose["Nota 1"] + jose["Nota 2"]) / 2  #Calcula a média das colunas de notas
print("A média das notas de José é:", media) 
