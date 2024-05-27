import streamlit as st
import dotenv
from streamlit.logger import get_logger

dotenv.load_dotenv()

LOGGER = get_logger(__name__)

def run():
  st.set_page_config(
      page_title="First Page",
      page_icon="💐",
      layout="centered",
      initial_sidebar_state="collapsed",
  )

  st.markdown(
      """
      <style>
      body {
          background-color: #f7dda4;
      }
      .center-content {
          padding-top: 50px;  /* Adjusted padding to move content further down */
      }
      .title-box {
          padding-bottom: 50px;  /* Increased padding to separate the title from the box */
      }
      .content-box {
          background-color: #EEEEEE;
          padding: 20px;
          border-radius: 10px;
          margin-bottom: 10px;  /* Reduced margin-bottom to make button closer to the box */
      }
      .button-container {
          text-align: center;
          padding-top: 10px;  /* Reduced padding-top to make button closer to the box */
      }
      .button-container button {
          background-color: #facbd3;
          color: black;
          padding: 10px 20px;
          border: none;
          border-radius: 5px;
          cursor: pointer;
      }
      </style>
      """,
      unsafe_allow_html=True
  )

  st.markdown(
      """
      <div class='center-content title-box'>
          <h1 style='text-align: center; color: #9182c4;'>Welcome to the flower chat bot!</h1>
      </div>
      """,
      unsafe_allow_html=True
  )

  st.markdown(
      """
      <div class='center-content content-box'>
          <p style='text-align: center; color: #000000; margin: 0;'>This is the chat-bot that recommends flowers based on your mood.</p>
          <p style='text-align: center; color: #000000; margin: 0;'>Click the 'Get Started' button to start getting flower recommendations.</p>
      </div>
      """,
      unsafe_allow_html=True
  )

  st.markdown(
      """
      <div class='center-content button-container'>
          <a href='chat' style='text-decoration: none;'>
              <button>Get Started</button>
          </a>
      </div>
      """,
      unsafe_allow_html=True
  )


if __name__ == "__main__":
  run()