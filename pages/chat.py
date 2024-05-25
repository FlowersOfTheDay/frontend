# app.py
import os
import streamlit as st
import requests

st.title("💬 Flowers of The Day 💐")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Call the FastAPI endpoint to get the response
    print('Hello')
    try:
        response = requests.get(
            os.environ.get("FRONTEND_CLIENT_BASE_URL")
        ).json()
        assistant_message = response.get("name")
    except Exception as e:
        assistant_message = f"Error: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown(assistant_message)
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
