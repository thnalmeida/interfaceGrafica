import  csv
import pandas as pd

#5.1 Crie um DataFrame com alguns dados fictícios:
dados = [["Nome", "Idade", "Cidade"],["Joao", 28, "SP"], ["Maria", 34, "RJ"], ["Jose", 29, "Curitiba"]]

#5.2 Salve esse DataFrame em um arquivo CSV chamado "dados.csv".
with open("dados.csv", mode = "w", newline = "") as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=";")  # Usando ponto e vírgula como separador
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)
    
#5.3 Ler o arquivo CSV e exibir os dados
#atribuo à uma variavel df o que esta no arquivo para conseguir ler
df = pd.read_csv("dados.csv")
print(df)
