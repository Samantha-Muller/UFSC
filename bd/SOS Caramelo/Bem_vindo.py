import pandas as pd
import streamlit as st

st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1>S.O.S Caramelo</h1>
        <p>O seu amiCÃO nos momentos mais difíceis</p>
    </div>
    """, unsafe_allow_html=True)

st.write("\n\n\n\n")
col1, col2 = st.columns([0.25,0.75])

with col2:

    st.image('imagens\logo.jfif', caption="Viralata caramelo, patrimônio nacional de quatro patas")


st.write("\n\n")
st.write("Criado no seio do melhor curso da UFSC, o SOS Caramelo é o software de excelência para a localização de animais perdidos e encontrados em catástrofes naturais.")

st.write("\n")
st.write("\n")
st.write("\n")

st.subheader("Selecione na coluna a esquerda o serviço desejado")