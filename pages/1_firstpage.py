import streamlit as st

st.set_page_config(
    page_title="First Page"
)

st.markdown(
    """
    ### 
    ### 
    ### Hello! This is chat-bot that recommend flowers.
    
    """
)
st.info('Click the Get Started button to start recommed')
import streamlit as st

on = st.toggle("If you write your email, we will send recommended flower to your email")

if on:
    st.text_input("Write your email")
st.link_button('Get Started', url = 'chat' )
