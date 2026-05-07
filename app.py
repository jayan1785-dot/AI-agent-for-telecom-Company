import streamlit as st
from transformers import pipeline

# Verizon-style colors
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

# Predefined menu
options = ["Check Order Status", "View Price Plans", "Upgrade Plan", "Billing Info", "Technical Support"]
choice = st.selectbox("How can I help you today?", options)

if choice == "Check Order Status":
    st.write("🔎 Your latest order #12345 is shipped and will arrive in 3–5 business days.")
elif choice == "View Price Plans":
    st.write("💰 Current plans:\n- Unlimited 5G: $70/month\n- Family Plan (4 lines): $200/month\n- Prepaid: $40/month")
elif choice == "Upgrade Plan":
    st.write("⬆️ You can upgrade to Unlimited 5G for $10 extra per month.")
elif choice == "Billing Info":
    st.write("📄 Your current bill is $85, due on May 15th.")
elif choice == "Technical Support":
    st.write("⚙️ Please restart your router. If issues persist, contact support at 1‑800‑VERIZON.")

# AI chatbot (trained on general dialogue)
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

user_input = st.text_input("Ask me anything:")
if user_input:
    response = chatbot(user_input, max_length=100)
    st.write("🤖 Agent:", response[0]["generated_text"])
