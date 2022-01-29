import streamlit as st
import pandas as pd
import pylab as plt
import seaborn as sns


def user_interface():

    text =  """
            # Y estas son las respuestas
            ¿Habrá funcionado?
            """
    st.write(text)

    text = "Calcular resultados"
    pressed = st.button(text)

    return pressed