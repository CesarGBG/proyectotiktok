import pandas as pd
import re
import matplotlib.pyplot as plt
import streamlit as st

# Título de la app
st.title("Análisis de Comentarios en TikTok")
st.write("Esta app detecta comentarios discriminatorios usando palabras ofensivas.")

# Subida de archivo CSV
archivo = st.file_uploader("Sube tu archivo CSV de comentarios", type=["csv"])

if archivo:
    # Cargar CSV
    df = pd.read_csv(archivo)

    # Mostrar primeras filas
    st.subheader("Vista previa de los datos:")
    st.write(df.head())

    # Limpiar texto
    df["texto_limpio"] = df["text"].apply(lambda x: re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]", "", str(x).lower()))

    # Lista de palabras ofensivas (puedes modificar)
    palabras_ofensivas = ["feo", "fea", "gordo", "india", "negro", "cholo", "zambo", "mongol", "maricón"]

    def es_discriminatorio(texto):
        return any(p in texto for p in palabras_ofensivas)

    df["discriminatorio"] = df["texto_limpio"].apply(es_discriminatorio)

    # Conteo
    conteo = df["discriminatorio"].value_counts()
    st.subheader("Distribución de comentarios discriminatorios:")
    st.bar_chart(conteo)

    # Mostrar ejemplos
    st.subheader("Ejemplos de comentarios discriminatorios:")
    st.write(df[df["discriminatorio"] == True][["text"]].head(10))

else:
    st.info("Por favor, sube un archivo CSV para comenzar.")
