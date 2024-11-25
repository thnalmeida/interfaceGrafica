#ATIVIDADE 01 

#QUESTAO 1
'''Faça um programa em Python que receba o valor de uma conta e um percentual 
de desconto. Calcule o novo valor da conta ao ser aplicado o percentual de 
desconto e escreva o resultado obtido.'''
#recebo do usuario o valor da conta, como o eh isnerido pelo usuario eh recebido como string, coloco float para
#fazer a conversao - o mesmo vale para o desconto
conta = float(input('Digite o valor da conta: '))
desconto = float(input('Digite o valor do desconto (%): '))

novoValor = conta - (conta * (desconto / 100)) #como o desconto inserido pelo usuario eh em percentual, preciso fazer a divisao para efetuar o calculo

print('O valor da conta com o desconto é: R$', novoValor)