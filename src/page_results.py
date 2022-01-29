import streamlit as st

def results():

    text =  """
            # Y estas son las respuestas
            ¿Habrá funcionado?
            """
    st.write(text)

    text = "Calcular resultados"
    pressed = st.button(text)

    return pressed