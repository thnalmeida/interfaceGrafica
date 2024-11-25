import csv
import pandas as pd

#2.1 criando arquivo produtos.csv
dados = [["ID", "Produto", "Preco"], ["Produto A", 10, 50], ["Produto B", 20, 75], ["Produto C", 15, 20]]

with open("produtos.csv", mode = "w", newline = "") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)
    
#2.2 Ler o arquivo CSV e exibir como tabela
df = pd.read_csv("produtos.csv")
print(df)

#2.3 criar novo arquivo cvs com precos atualizado com desconto de 10%
dados = [["ID", "Produto", "Preco atualizado"], ["Produto A", 10, 50 -(50*0.1)], ["Produto B", 20, 75 - (75*0.1)], ["Produto C", 15, 20 - (20*0.1)]]

with open("produtos_desconto.csv", mode = "w", newline = "") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)
    
#2.2 Ler o arquivo CSV e exibir como tabela
df = pd.read_csv("produtos_desconto.csv")
print(df)