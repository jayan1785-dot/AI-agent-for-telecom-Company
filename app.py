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

# Load a stable model (Flan-T5 works well for Q&A)
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

# Keep conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Ask me anything:")

if user_input:
    response = chatbot(user_input, max_length=100)
    bot_reply = response[0]["generated_text"]

    # Save conversation
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Agent", bot_reply))

# Display conversation
for speaker, msg in st.session_state.history:
    if speaker == "You":
        st.write(f"👤 {speaker}: {msg}")
    else:
        st.write(f"🤖 {speaker}: {msg}")
