import os
import streamlit as st
import requests

st.title("💬 Flowers of The Day 💐")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.context = ""
    st.session_state.conversation_id = None  # 새로운 상태 변수 추가

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("오늘의 기분을 입력하여 대화를 시작해보세요"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("loading..."):
        try:
            response = requests.post(
                os.environ.get("FRONTEND_CLIENT__BASE_URL") + '/chat',
                json={
                    "chat": prompt,
                    "id": st.session_state.conversation_id 
                }
            ).json()
            assistant_message = response.get("output")
            conversation_id = response.get("id")
        except Exception as e:
            assistant_message = f"Error: {str(e)}"
            conversation_id = st.session_state.conversation_id 

    with st.chat_message("assistant"):
        st.markdown(assistant_message)
    st.session_state.conversation_id = conversation_id
