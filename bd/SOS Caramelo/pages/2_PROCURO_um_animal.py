import streamlit as st
import pandas as pd
import mariadb
from datetime import datetime 

def Cidade():
    sql.execute("SELECT TRIM(cidade) FROM pk_cidades")
    cidade= sql.fetchall()
    cidade = pd.DataFrame(cidade)
    return(cidade)

def Consulta_BD(cidade_selecionada):
    sql.execute("""SELECT
                a.data,
                b.cidade AS Cidade,
                c.raça AS Raça,
                d.cor AS Cor,
                CASE
                    WHEN a.`chip_identificação` = 0 then "Não"
                    ELSE "Sim"
                END AS "Possui chip de identificação?",
                a.observação AS Observação,
                a.nome AS Nome,
                a.telefone AS Telefone,
                a.email AS Email,
                a.endereço AS Endereço,
                a.número
                    
                FROM cadastro_animais a

                LEFT JOIN pk_cidades b ON
                a.cidade = b.id

                LEFT JOIN pk_raça c ON
                a.`raça` = c.id

                LEFT JOIN pk_cor d ON
                a.cor = d.id

                WHERE b.cidade LIKE (?)

                """, [cidade_selecionada])
    consulta = sql.fetchall()
    return(consulta)

#______INÍCIO______#

# Conecta ao Banco de Dados
try:
    conn = mariadb.connect(
        user="caramelo",
        password="caramelo",
        host="192.168.1.102",
        port=3306,
        database="sos_caramelo"
    )
    sql = conn.cursor()
    print("Conexão bem-sucedida ao banco de dados")
except mariadb.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    conn = None



#Header
st.header("Procuro um animal")

st.write("")
st.write("Preencha atentamente o formulário abaixo para procurar o seu animal")
st.write("")
st.write("")



#Carrega o formulário somente se conectado ao bd
if conn:
    try:    
        
        #Carrega as cidades do bd
        cidade = Cidade()

        #Input da Cidade
        cidade_selecionada = st.selectbox("Selecione a cidade onde o animal foi perdido",cidade)
        st.write("")

                
        #Faz a query usando a cidade como filtro
        consulta = Consulta_BD(cidade_selecionada)
        consulta = pd.DataFrame(consulta, columns=['Data','Cidade','Raça','Cor','Possui chip de identificação','Observação','Nome','Telefone','Email','Endereço','Número'])

        if len(consulta)>=1:

            #Escreve as informações do animal encontrado.
            for i in range(len(consulta)):
                st.write("---")
                st.write("")
                st.subheader(f"Registro número {i+1}")
                st.write(f"Data que o animal foi encontrado: {consulta['Data'][i]}")
                st.write(f"Cidade:  {consulta['Cidade'][i]}")
                st.write(f"Raça: {consulta['Raça'][i]}")
                st.write(f"Cor:  {consulta['Cor'][i]}")
                st.write(f"Possui chip de identificação:  {consulta['Possui chip de identificação'][i]}")
                st.write(f"Observaçao: {consulta['Observação'][i]}")
                st.write("")
                st.write("->INFORMAÇÕES PARA CONTATO<-")
                st.write("")
                st.write(f"Nome do(a) tutor(a) temporário: {consulta['Nome'][i]}")
                st.write(f"Telefone: {consulta['Telefone'][i]}")
                st.write(f"Email: {consulta['Email'][i]}")
                st.write(f"Endereço: {consulta['Endereço'][i]}")
                st.write(f"Número: {consulta['Número'][i]}")
        else:
            st.write("")
            st.subheader("Não há registro para a cidade selecionada")



       
    except mariadb.Error as e:
        st.header(f"Erro ao inserir dados: {e}")
    finally:
        # Fechar a conexão
        conn.close()
        print("Conexão fechada")

            
            #espécie
            #raça
            #cor
            #possui identificaçao
            #contato: nome, e-mail, telefone, endereço