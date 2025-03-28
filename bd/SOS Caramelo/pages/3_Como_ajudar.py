import streamlit as st


st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1>AJUDE-NO$</h1>

    </div>
    """, unsafe_allow_html=True)

st.write("\n")
st.write("\n")


col1, col2 = st.columns([0.2,0.8])

with col2:
    st.image(r"imagens\nota.png", width=400)

st.write("\n")
st.write("\n")
st.write("\n")

st.write("Colabore com o nosso trabalho fazendo uma doação espontânea no Pix XXXXXXXXXXXXX")