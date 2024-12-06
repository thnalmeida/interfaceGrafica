#EXERCICIO 3 - MODULO 3 - GRAFICO DE DISPERSAO
#utilizando biblioteca matplotlib

#importo biblioteca instalada anteriormente (pip install matplotlib)
import matplotlib.pyplot as plt

#Crie um gráfico de dispersão (scatter plot) para representar a relação entre x e y.

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 3, 5, 6, 7, 8, 10]

#comando para criar o grafico:
plt.scatter(x, y)

#2. Adicione título ao gráfico e rótulos aos eixos
plt.title('Relacao entre as variaveis')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

#3.Exiba o gráfico.
plt.show()


