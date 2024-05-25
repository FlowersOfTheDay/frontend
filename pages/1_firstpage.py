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
st.text_input("Write your name")
st.link_button('Get Started', url = 'chat' )
