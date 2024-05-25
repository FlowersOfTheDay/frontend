import streamlit as st
import dotenv
from streamlit.logger import get_logger

dotenv.load_dotenv()

LOGGER = get_logger(__name__)

def run():
  st.set_page_config(
    page_title="Flowers of the day"
  )


if __name__ == "__main__":
  run()