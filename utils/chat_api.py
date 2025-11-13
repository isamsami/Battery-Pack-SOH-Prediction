import openai
import streamlit as st

def ask_chatgpt(question):
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return response["choices"][0]["message"]["content"]
