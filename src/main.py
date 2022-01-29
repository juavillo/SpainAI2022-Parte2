import streamlit as st

from page_sidebar import sidebar
from page_front import front
from page_results import results



def main():

    pages_mapper = {
                        '1. Portada': front,
                        '2. ¿Qué vamos a hacer?': results
                    }

    ls_page_name = pages_mapper.keys()
    page_name = sidebar(ls_page_name)

    pages_mapper[page_name]()


if __name__ == '__main__':
    main()