import streamlit as st

st.set_page_config(
    page_title="Evoceículo",
    page_icon="static/Logo_Eco.png",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "# O ecoveículo, acesse nosso instagram: [![Click me](app/static/Logo_Eco.png)](https://www.instagram.com/ecoveiculounifei/)"
    }
)

st.warning("Aplicação ainda não implementada")
st.markdown("[![Click me](app/static/Logo_Eco.png)](https://www.instagram.com/ecoveiculounifei/)")

with st.sidebar:
    st.markdown("#Tenha um bom dia")