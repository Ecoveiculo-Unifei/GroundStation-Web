import streamlit as st

st.set_page_config(
    page_title="Evoceículo",
    page_icon="static/Logo_Eco.png",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Sobre': "# O ecoveículo, acesse nosso instagram: https://www.instagram.com/ecoveiculounifei/"
    }
)

st.warning("Aplicação ainda não implementada")
st.markdown("[![Click me](app/static/Logo_Eco.png)](https://www.instagram.com/ecoveiculounifei/)")

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )