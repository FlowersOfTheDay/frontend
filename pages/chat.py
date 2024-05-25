# app.py
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
    try:
        response = requests.post(
            "https://computer-system-team-14.dev.mobilex.kr/api/v1/",
            json={"content": prompt}
        ).json()
        assistant_message = response.get("content", "No response from API")
    except Exception as e:
        assistant_message = f"Error: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown(assistant_message)
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})