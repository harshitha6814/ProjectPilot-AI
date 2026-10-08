import streamlit as st
from backend.ai_engine import chat

st.title("Model Test")

if st.button("Test AI"):
    result = chat([
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ])

    st.write(result)