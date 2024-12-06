#ATIVIDADE 01 

#QUESTAO 4
''' Faça um programa que receba a altura e o sexo de uma pessoa. Por meio 
desses dados calcule e mostre o peso ideal para a pessoa. Utilize as fórmulas 
a seguir (obs: h corresponde à altura):
 Homens: (72,7 * h) - 58
 Mulheres: (62, 1 * h) – 44, 7'''

altura = float(input('Digite a altura em metros: '))
sexo = input('Digite o sexo (F/M): ')

if sexo == 'M':
    pesoIdeal = (72.7 * altura) - 58
    print("{:.2f}" .format(pesoIdeal))

elif sexo == 'F':
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"{pesoIdeal: .2f}")