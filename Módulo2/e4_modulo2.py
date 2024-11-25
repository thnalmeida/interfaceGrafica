

#leitura linha por linha
arquivo = open("dadostcc.csv", "r")

#utilizo estrutura de repetição for
for linha in arquivo:
    print(linha.strip())
    
arquivo.close()
