import streamlit as st
import pandas as pd
from serial_lib import EspLora, search
from PIL import Image


st.set_page_config(page_title="EcoVeículo", page_icon="static/Logo.ico", layout="wide", initial_sidebar_state="auto", menu_items=None)

serial_port = "COM6"
baud_rate = 115200

top1, top2, top3, top4, top5 = st.columns([1, 1, 1, 1 , 1])

top1.title('EcoVeículo')
top1.subheader('Projetando o futuro!')

logo = Image.open('static/Logo_Eco.png')
top5.image(logo)

body1, body2, body3, body4 = st.columns([1,1,1,1])

metricaVelInst = body1.empty()
metricaVelMedia = body2.empty()
metricaDistancia = body3.empty()
metricaRPM = body4.empty()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Velocidade Instantânea")
    grafVelInst = st.empty()

    st.subheader("Distância")
    grafDistancia = st.empty()

with col2:
    st.subheader("Velocidade Média")
    grafVelMed = st.empty()

    st.subheader("RPM")
    grafRPM = st.empty()
    

data_columns = ["Id","Tempo", "Distancia", "VelInst", "VelMedia", "Voltas", "RPM"]
msg = st.empty()

pacote0 = {
    "Id": int(0),
    "Tempo": int(0),
    "Distancia": float(0),
    "VelInst": float(0),
    "VelMedia": float(0),
    "Voltas": int(0),
    "RPM": int(0)
}

df = pd.DataFrame([pacote0])
df.set_index("Id",inplace=True)

dataVelInst = grafVelInst.line_chart(df["VelInst"])
dataDistancia = grafDistancia.line_chart(df["Distancia"])
dataVelMed = grafVelMed.line_chart(df["VelMedia"])
dataRPM = grafRPM.line_chart(df["RPM"])

st.write(search(comDescricao=True))
esp = EspLora(serial_port,baud_rate)
esp.open()

while True:
    pacote = esp.read()
    if pacote is not None:
        msg.write(pacote)
        df = pd.DataFrame([pacote])
        df.set_index("Id",inplace=True)
        dataVelInst.add_rows(df["VelInst"])
        dataDistancia.add_rows(df["Distancia"])
        dataVelMed.add_rows(df["VelMedia"])
        dataRPM.add_rows(df["RPM"])

        metricaVelInst = metricaVelInst.metric(label="Velocidade", value=df["VelInst"])
        metricaVelMedia = metricaVelMedia.metric(label="Vel. Media", value=df["VelMedia"])
        metricaDistancia = metricaDistancia.metric(label="Distancia", value=df["Distancia"])
        metricaRPM = metricaRPM.metric(label="RPM", value=df["RPM"])




msg.warning('Erro')

esp.close()