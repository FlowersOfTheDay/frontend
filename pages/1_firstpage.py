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
if st.button('Go to Chat'):
    js_code = "window.location.href = '/chat;"
    