import streamlit as st
import google.generativeai as genai

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Gemini-bot")

if 'chat_session' not in st.session_state:
    st.session_state["chat_session"] = model.start_chat(history=[])

for content in st.session_state.chat_session.history:
    with st.chat_message("ai" if content.role == "model" else "user"):
        st.markdown(content.parts[0].text)

if prompt := st.chat_input("메시지를 입력하세요."):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("ai"):
        response = st.session_state.chat_session.send_message(prompt)
        st.markdown(response.text)