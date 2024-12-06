#MODULO 4 - DASHBOARD COM A BIBLIOTECA STREAMLIT

# QUESTÃO 1) Escolher um dataset (base de dados) em formato (.CSV) de qualquer tema de sua preferência do 
# site kaggle no seguinte endereço: https://www.kaggle.com/datasets

#Banco de dados escolhido = Risco de Obesidade

#importo bibliotecas necessárias para realizar o projeto
import pandas as pd #importo bliblioteca PANDAS para trabalhar com dataframes em python
import streamlit as st #STREAMLIT para construir a dashboard 
import plotly.express as px #módulo da biblioteca PLOTLY que simplifica a criação de gráficos

#Configuro a dash inicialmente
st.set_page_config(layout = "wide", page_title = "Dashboard - Obesity Risk") 
st.title('Dashboard - Obesity Risk') #titulo da dash 

# QUESTÃO 2) Tratar/ converter o arquivo em formato (.CSV) como um arquivo do tipo dataframe em python
df = pd.read_csv("datasetObesity.csv", header=0, sep = ",", decimal = ".") #indico nome do arquivo csv a ser transformado em dataframe
#header = 0 indica que a primeira linha eh o cabeçario da tabela - nome das colunas
#indico o separador das colunas "," e como decimal será tratado  "."

print(df) #para verificar se foi corretamente convertido em dataframe

#peço para imprimir o nome das colunas
print(df.columns.tolist())
df.columns = df.columns.str.strip() #retiro espaços vazios dos titulos das colunas q podem confundir
print(df.columns.tolist())

#QUESTAO 5) Criar um filtro com o componente selectbox de um determinado período para
#variar as informações apresentadas nos gráficos.
gender = st.sidebar.selectbox("Genero", df["Gender"].unique())
df_filtered = df[df["Gender"] == gender]

#QUESTAO 3)Criar um gráfico de linha, um gráfico de barra, um gráfico de dispersão e um gráfico de pizza.
#Gráfico de linha
grafico1 = px.line(
    data_frame=df,
    x=df["NObeyesdad"],  # Nome da coluna para o eixo X
    y=["Age"],         # Nome da coluna para o eixo Y
    title="Estado nutricional x Idade",
    color_discrete_sequence=["blue"]  # Definindo cor do gráfico
)
st.plotly_chart(grafico1)

#Grafico de barra
grafico2 = px.bar(df_filtered, x="SMOKE", y="Age", title="Fumar x idade")
st.plotly_chart(grafico2)

#Grafico de pizza
grafico3 = px.pie(df_filtered, values='Weight', names='NObeyesdad', title = "Classificação do Estado nutricional")
st.plotly_chart(grafico3)

#Grafico de dispersao
grafico4 = px.scatter(df_filtered, x="Age", y="Weight", title = "Idade x peso")
st.plotly_chart(grafico4)








