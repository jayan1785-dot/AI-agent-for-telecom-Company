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

# Load a conversational model
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

# Keep conversation history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask me anything:")

if user_input:
    response = chatbot(user_input, max_length=100)
    bot_reply = response[0]["generated_text"]
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Agent", bot_reply))

# Display conversation
for speaker, msg in st.session_state.history:
    if speaker == "You":
        st.write(f"👤 {speaker}: {msg}")
    else:
        st.write(f"🤖 {speaker}: {msg}")
