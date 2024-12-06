#para trabalhar com dataframes em python eh comum utilizar a biblioteca pandas
#essa biblioteca fornece estruturas de dados faceis de usar, de alto desempenho e ferramentas de analises de dados
#importanto a biblioteca

import pandas as pd #forma mais comum de importar a biblitoeca pandas, para usar no codigo vamos chamar de pd
dados = {
    #linhas  #colunas
    "Nome": ['Ana', 'Carlos', 'Lucas', "Maria"],
    "Idade": [23, 34, 25, 31],
    "Cidade": ['SP', 'RJ', 'Curitiba', 'BH']
}

#crio uma variavel (df) e faço a conversao do dicionario Dados em DataFrame por meio da biblioteca pandas 
#(metodo DataFrame). df armazena 
df = pd.DataFrame(dados)

#exibicao dos dados
print(df)

print(df.head())  #exibe as primeiras 5 linhas do dataframe

print(df.shape) #exibe numero de linhas e colunas (x,y) x -> nro de linhas e y -> nro de colunas

print(df.tail()) #exibe as ultimas 5 linhas do dataframe

print(df.iloc[0]) #para acesssar uma linha, 0 é o indice da linha, python coloca automaticamente 

#filtro de dados
maiores_que_26 = df[df["Idade"] > 26]

print("Tem idade maior que 26 anos: " + "\n", maiores_que_26)

#modificacao de filtros 
#quero alterar idade do carlos para 35
df.at[1, "Idade"] = 35 #argumentos: nro do indice da linha + nome da coluna #at eh um metodo
print(df)

#quero alterar uma coluna inteira, vou passar as siglas para o nome por extenso
df["Cidade"] = ["Sao Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
print(df)

#adicionando coluna: 
df["Profissao"] = ["Engenheira", "Medico", "Designer", "Arquiteta"]
print(df)

#removendo coluna
df = df.drop("Profissao", axis = 1) #metodo drop, sintaxe = (label, axis = 0 (para remover linha)  ou 1 (para remover coluna)) 

print(df)

#operacoes com dados, estatistica basica, funcoes ja no dataframe
#medida das idades:
media = df["Idade"].mean()
print("A media das idades é", media)

soma = df["Idade"].sum()
print("A soma das idades é", soma)

#criando uma nova coluna com a idade dobrada
df["Idade dobrada"] = df["Idade"] * 2
print(df)

#ordenando dados
df_idade_ordem = df.sort_values(by= "Idade", ascending = True)
print(df_idade_ordem)