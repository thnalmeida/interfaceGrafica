#EXERCICIO 1 - MODULO 3 - GRAFICO DE LINHAS
#utilizando biblioteca matplotlib

#Criar um gráfico de linhas simples para entender a relação entre duas variáveis.
#Dado o seguinte conjunto de dados:
#x = [1, 2, 3, 4, 5]
#y = [2, 4, 6, 8, 10]

#importo biblioteca instalada anteriormente (pip install matplotlib)
import matplotlib.pyplot as plt

#1. Crie um gráfico de linhas que mostre a relação entre x e y.

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x,y) #criacao do grafico

#2. Adicione título ao gráfico e rótulos aos eixos X e Y.
plt.title('Faturamento em milhoes da loja dos meses de janeiro a maio')
plt.xlabel('Meses')
plt.ylabel('Faturamento R$')

#3. Exiba o gráfico na tela.peco para mostrar o grafico. grafico esta criado para exibir o comando eh:
plt.show()

