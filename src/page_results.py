import streamlit as st

def user_interface():

    text =  """
            # Y estas son las respuestas
            ¿Habrá funcionado?
            """
    st.write(text)

    text = "Calcular resultados"
    pressed = st.button(text)

    return pressed