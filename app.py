import streamlit as st
from transformers import pipeline, Conversation

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
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

# Keep conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = Conversation()

# User input
user_input = st.text_input("Type your question here:")

if user_input:
    st.session_state.conversation.add_user_input(user_input)
    response = chatbot(st.session_state.conversation)
    bot_reply = response.generated_responses[-1]
