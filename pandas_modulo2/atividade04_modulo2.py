import pandas as pd


#4.1 Crie um DataFrame com os dados sobre empregados:

dados = {
    "Nome": ["Carlos", "Pedro", "Ana", "Fernanda"],
    "Idade": [25, 35, 28, 45],
    "Salário": [2500, 3500, 2800, 4200]
}

df = pd.DataFrame(dados)

#exibindo dataframe
print(df)

#4.2 Filtre e exiba apenas os empregados com idade maior que 30.
maiores_que_30 = df[df["Idade"] > 30]

print("Os empregados com idade maior que 30 anos são: " + "\n", maiores_que_30)


#4.3 Filtre e exiba os empregados que têm salário maior que 3000
salario_maior_3000 = df[df["Salário"] > 3000]

print("Os empregados com salário maior que R$3000 sao: " + "\n", salario_maior_3000)