import streamlit as st
import requests
import uuid

# ---------------- CONFIG ----------------
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="Life Partner Chatbot",
    page_icon="💍",
    layout="centered"
)

st.title("💍 Life Partner Chatbot")
st.caption("A friendly conversation about your future life partner")

# ---------------- SESSION ----------------
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Send to backend
    payload = {
        "session_id": st.session_state.session_id,
        "message": user_input
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        data = response.json()
        bot_reply = data["reply"]

    except Exception as e:
        bot_reply = "⚠️ Unable to connect to chatbot backend."

    # Show bot reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
