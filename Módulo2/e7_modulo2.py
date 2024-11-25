#MANIPULANDO ARQUIVOS CSV

import csv

with open("dadostcc.csv", mode = "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)