#importo biblioteca streamlit 

import streamlit as st


st.title('My first App with Streamlit')
st.write('Hello, world! This is my first App')

nome = st.text_input('Digite o seu nome: ')

if nome: 
    st.write("Ola", nome)