import pandas as pd
import streamlit as st

tabela= pd.read_csv('produtos_estados_valores.csv')

st.title('Analise de Vendas por Estado')
st.subheader('Visão Geral dos Dados')

st.sidebar.subheader('Filtrar por Produtos')

#filtro de regiao
regiao = st.sidebar.multiselect( 'Selecione a Região',tabela['Estado'].unique())

#se for filtrado, aqui ele junta todas as regioes como uma só
if regiao:
    tabela = tabela.loc[tabela['Estado'].isin(regiao)]

#total de vendas
st.metric('Total de Vendas', f'R$ {tabela['Valor'].sum():,.2f}')

#total/media
st.metric('Media de vendas por Estado', f'R$ {tabela['Valor'].mean():,.2f}')

#forma de tabela
st.dataframe(tabela)

st.subheader('Vendas por Estado')

#grafico do valor por estado
st.bar_chart(tabela.groupby('Estado')['Valor'].sum())

st.subheader('Vendas por Produto')

st.sidebar.subheader('Valor por Produto')

#grafico bonito
st.bar_chart(tabela.groupby('Produto')['Valor'].sum())


valor= st.sidebar.slider('Selecione o valor máximo para filtro',0,10000,5000)
st.sidebar.write(f'Produtos com valor até R$ {valor}')
filtro_valor = tabela.loc[tabela['Valor'] <= valor]
st.sidebar.dataframe(filtro_valor)
