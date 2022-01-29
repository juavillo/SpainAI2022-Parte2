import streamlit as st

from page_sidebar import sidebar
from page_front import front



def main():

    pages_mapper = {
                        '1. Portada': front,
                    }

    ls_page_name = pages_mapper.keys()
    page_name = sidebar(ls_page_name)

    pages_mapper[page_name]()


if __name__ == '__main__':
    main()