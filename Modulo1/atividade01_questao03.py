#crio lista para armazenar dados inseridos pelo usuario de acordo com sinal do numero: 
positivos = []
numeros = []
# #crio um laco para manter o programa em execucao ate chegar a uma condicao que pare. No caso, a condicao eh um numero egativo
while True:
    #solicito a entrada do usuario
    x = int(input("Digite um numero: "))
    
    #adiciono o numero à lista q armazena todos os numeros digitados
    numeros.append(x)

    if x > 0:
        positivos.append(x)

    else: 
        y = x #apenas um numero negativo, pois apos sua leitura programa encerra
        break #para o loop while

#letra a: imprimir a soma dos números positivos lidos
soma_positivos = sum(positivos)
print("LETRA A - A soma dos numeros positivos digitados eh: ", soma_positivos)

#letra b: imprimir a médias de todos os números lidos
media_numeros = sum(numeros) / len(numeros) #len pega qtd de numeros na lista
print("LETRA B - A media dos numeros lidos eh: ", media_numeros)

#letra c:  imprimir o número com maior valor
maior_numero = max(numeros) if numeros else None
if maior_numero is not None:
        print("LETRA C - Maior valor entre os numeros lidos: ", maior_numero)

#letra d:  imprimir todos os números negativos
print("LETRA D - Numero negativo digitado: ", y) #ha apenas um numero lido pois a leitura deste interrompe a leitura 
