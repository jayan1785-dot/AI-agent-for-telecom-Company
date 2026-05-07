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

# Load conversational model
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill
