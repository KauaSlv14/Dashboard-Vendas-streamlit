import pandas as pd
import streamlit as st

tabela= pd.read_csv('produtos_estados_valores.csv')

st.title('Analise de Vendas por Estado')
st.subheader('Visão Geral dos Dados')


#filtro de regiao
regiao = st.multiselect( 'Selecione a Região',tabela['Estado'].unique())

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

#grafico bonito que n sei o nome
st.bar_chart(tabela.groupby('Produto')['Valor'].sum())