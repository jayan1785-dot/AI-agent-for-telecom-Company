import streamlit as st
from transformers import pipeline

# Verizon-style branding
st.markdown(
    """
    <style>
    .main { background-color: #ffffff; color: #000000; }
    h1 { color: #e60000; } /* Verizon red */
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📞 Verizon Customer Service AI Agent")

# Load a stable text2text model
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

# Keep conversation history
if "history" not in st.session_state:
    st.session_state.history =
