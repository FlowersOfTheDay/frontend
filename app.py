import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
  st.set_page_config(
    page_title="Flowers of the day"
  )

  st.write("need to implement")

if __name__ == "__main__":
  run()