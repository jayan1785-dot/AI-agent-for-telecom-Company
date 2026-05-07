import streamlit as st
from transformers import pipeline

# Verizon-style branding
st.set_page_config(page_title="Verizon AI Agent", page_icon="📞")

st.markdown(
    """
    <style>
    .main { background-color: #ffffff; color: #000000; }
    h1 { color: #cd040b; font-weight: bold; } /* Verizon brand red */
    .stChatMessage { border-radius: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📞 Verizon Customer Service AI Agent")

# Cache the model so it doesn't reload on every interaction
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small")

chatbot = load_model()

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Display conversation history using modern chat UI
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input using st.chat_input
if prompt := st.chat_input("How can I help you today?"):
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.history.append({"role": "user", "content": prompt})

    # Generate AI response
    with st.spinner("Agent is typing..."):
        # We add a simple prefix to help the model understand context
        formatted_prompt = f"answer this customer service query: {prompt}"
        response = chatbot(formatted_prompt, max_length=100)
        bot_reply = response[0]["generated_text"]

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    
    # Add assistant response to chat history
    st.session_state.history.append({"role": "assistant", "content": bot_reply})
