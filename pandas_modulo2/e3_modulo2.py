#importo biblioteca pandas que tera os metodos q permitirao a manipulacao do arquivo


try: 
    tabelatcc = open ("dadostcc.csv", "r")
    print("Arquivo aberto com sucesso!")
    
except:
    print("Arquivo nao foi aberto")
    
#leio o arquivo e atribuo a uma variavel
conteudo_tabelatcc = tabelatcc.read() #metodo ja incluso na biblioteca pandas q permite a leitura do documento INTEIRO
#read(): le o arquivo inteiro
#readline(): le uma linha de cada vez
#readlines(): le todas as linhas, retornando uma lista

print(conteudo_tabelatcc)

tabelatcc.close()