#1.1 Criacao do arquivo de texto, modo write
arquivo = open("notas.txt", "w")

#escrever no arquivo
arquivo.write("Joao: 8\n")
arquivo.write("Maria: 9\n")
arquivo.write("Ana: 7\n")

arquivo.close()

#1.2 leitura do arquivo, modo read
arquivo = open("notas.txt", "r")
#atribuo à variavel conteudo o que esta no arquivo de texto
conteudo = arquivo.read()
print("Leitura dos dados antes da modificacao:")
print(conteudo)
arquivo.close()

#Adicionando nova nota no arquivo, modo append: 
arquivo = open("notas.txt", "a")
#adiciono o que quero escrever
arquivo.write("Carlos: 10")
arquivo.close()

#1.3 leitura apos modificacao, modo read
print("Leitura apos modificacao: ")
arquivo = open("notas.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()


