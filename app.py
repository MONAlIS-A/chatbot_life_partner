import streamlit as st
import requests
import uuid

API_URL = "http://127.0.0.1:8001/chat"

st.set_page_config(page_title="Casual Life Partner Chatbot")
st.title("🤖 Casual Life Partner Chatbot")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# Call GET once at startup
if not st.session_state.messages:
    response = requests.get(API_URL).json()
    bot_reply = response["reply"]
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
user_input = st.chat_input("Type your message...")
if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    payload = {"session_id": st.session_state.session_id, "message": user_input}
    response = requests.post(API_URL, json=payload).json()
    bot_reply = response["reply"]

    st.chat_message("assistant").write(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    if response.get("end"):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []
