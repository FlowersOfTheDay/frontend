import streamlit as st

st.title("Flowers of The Day")

# Initialize the session state if not already done
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate a response only when there is user input
    response = f"Bot: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})