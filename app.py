import streamlit as st

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

# Simple telecom FAQ knowledge base
faq = {
    "order": "Your latest order #12345 has been shipped and will arrive in 3–5 business days.",
    "plan": "We offer Unlimited 5G ($70/month), Family Plan (4 lines $200/month), and Prepaid ($40/month).",
    "billing": "Your current bill is $85, due on May 15.",
    "upgrade": "You can upgrade to Unlimited 5G for $10 extra per month.",
    "support": "Please restart your router. If issues persist, call 1‑800‑VERIZON."
}

# Conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Ask me anything:")

if user_input:
    reply = "Sorry, I don’t have that info yet."
    for key, answer in faq.items():
        if key in user_input.lower():
            reply = answer
            break

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Agent", reply))

# Display conversation
for speaker, msg in st.session_state.history:
    if speaker == "You":
        st.write(f"👤 {speaker}: {msg}")
    else:
        st.write(f"🤖 {speaker}: {msg}")
