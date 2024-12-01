#EXERCICIO 3 - MODULO 3 - HISTOGRAMA
#utilizando biblioteca matplotlib

#importo biblioteca instalada anteriormente (pip install matplotlib)
import matplotlib.pyplot as plt

#importo biblioteca numpy
import numpy as np

#Gere um conjunto de dados aleatórios usando numpy, com 1000 números distribuídos normalmente:
dados = np.random.randn(1000)

#1. Crie um histograma desses dados com 30 bins.
plt.hist(dados, bins = 30, edgecolor = 'red')

#2. Adicione título ao gráfico e rótulos aos eixos.
plt.title('Grafico de Dispersao')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

#3. Exiba o gráfico.
# 4. Salve o gráfico como um arquivo de imagem no formato .png.

plt.savefig('teste.png', format='png')
plt.show()

#Quando você faz plt.show(), a figura é zerada pra preparar outro gráfico. 
#Assim, chamar savefig resulta em uma imagem em branco.
#Chamar savefig antes de show