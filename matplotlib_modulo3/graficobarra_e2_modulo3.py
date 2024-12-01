#EXERCICIO 2 - MODULO 3 - GRAFICO DE BARRAS
#utilizando biblioteca matplotlib

#importo biblioteca instalada anteriormente (pip install matplotlib)
import matplotlib.pyplot as plt

#Crie um gráfico de barras com essas categorias e valores.

categorias = ['A', 'B', 'C', 'D']
valores = [10, 25, 5, 15]

plt.bar(categorias, valores) #criacao do grafico de BARRA

#2. Adicione título ao gráfico e rótulos aos eixos
plt.title('Frequencia de alunos em cada classe socioeconômica')
plt.xlabel('Classe')
plt.ylabel('Quantidade de alunos')
plt.show()