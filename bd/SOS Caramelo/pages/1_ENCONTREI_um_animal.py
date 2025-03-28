import streamlit as st
import pandas as pd
import mariadb
from datetime import datetime 

#Lê as cidades do db
def Cidade():
    sql.execute("SELECT TRIM(cidade) FROM pk_cidades")
    cidade= sql.fetchall()
    cidade = pd.DataFrame(cidade)
    return(cidade)

def Raça():
    sql.execute("SELECT raça from pk_raça")
    raça = sql.fetchall()
    raça = pd.DataFrame(raça)
    return(raça)

def Cor():
    sql.execute("SELECT cor from pk_cor")
    cor = sql.fetchall()
    cor = pd.DataFrame(cor)
    return(cor)



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
st.header("Encontrei um animal")

st.write("")
st.write("Preencha atentamente o formulário abaixo para cadastrar o animal encontrado")
st.write("")
st.write("")


#Carrega as tabelas do bd
cidade = Cidade()
raça = Raça()
cor = Cor()

#Carrega o formulário somente se conectado ao bd
if conn:
    try:    
        #Formulário
        with st.form("cadastro_animal"):
            st.write("Cadastro de animal")
            st.write("")

            #Data
            data_encontrado = st.date_input("Selecione a data em que o animal foi encontrado:", format="DD/MM/YYYY")
            st.write("")

            #Cidade
            cidade_selecionada = st.selectbox("Selecione a cidade onde o animal foi encontrado",cidade)
            st.write("")

            #Espécie
            #espécie_selecionada = st.selectbox("Selecione a espécie do animal que você procura",espécie)
            
            #Raça
            raça_selecionada = st.selectbox("Raça",raça)
            
            #Cor
            cor_selecionada = st.selectbox("Cor",cor)

            #Chip de Identificação
            chip_identificação = st.radio("Possui chip de identificação?",["Não","Sim"])

            #Observaçao
            observação = st.text_input("Observação")

            #Info de Contato
            st.divider()
            st.subheader("Informações de Contato")

            #Nome
            nome = st.text_input("Nome do cuidador temporário")
            
            #Telefone
            telefone = st.text_input("Telefone para contato")

            #Email
            email = st.text_input("E-mail")

            #Endereço
            endereço = st.text_input("Endereço")

            #Número do Endereço
            número_endereço = st.text_input("Número")


            st.write("")
            submitted = st.form_submit_button("Enviar")


            if submitted:
                try:
                    
                    #Dá match com a Primary Key

                    #Cidade
                    sql.execute(f"Select id from pk_cidades where cidade = (?)",[cidade_selecionada])
                    cidade_pk = sql.fetchone()
                    
                    #Raça           
                    sql.execute(f"Select id from pk_raça where raça = (?)",[raça_selecionada])
                    raça_pk = sql.fetchone()

                    #Cor
                    sql.execute(f"Select id from pk_cor where cor = (?)",[cor_selecionada])
                    cor_pk = sql.fetchone()

                    if chip_identificação == "Não":
                        chip_identificação = 0
                    else:
                        chip_identificação = 1

                    #Atualiza no bd
                    sql.execute("INSERT INTO cadastro_animais (data, cidade, raça, cor, chip_identificação, observação, nome, telefone, email,endereço, número) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",[data_encontrado, cidade_pk[0], raça_pk[0], cor_pk[0], chip_identificação, observação, nome, telefone, email, endereço,número_endereço])
                    conn.commit()
                    st.success("Animal cadastrado com sucesso!")
                    
                except mariadb.Error as e:
                    st.error(f"Erro ao cadastrar animal: {e}")




       
    except mariadb.Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        # Fechar a conexão
        conn.close()
        print("Conexão fechada")

            
            #espécie
            #raça
            #cor
            #possui identificaçao
            #contato: nome, e-mail, telefone, endereço