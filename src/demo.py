import streamlit as st
import random

st.title("🛡️ Cyberbullying Detection Demo")

st.write("Type a message below to check if it is cyberbullying or not.")

# User input
user_input = st.text_area("Enter a message:")

def dummy_predict(text):
    """
    A fake model that randomly predicts cyberbullying or not.
    Replace this with Sonika's trained model later.
    """
    return random.choice(["Cyberbullying ❌", "Not Cyberbullying ✅"])

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("⚠️ Please type a message first!")
    else:
        prediction = dummy_predict(user_input)
        st.success(f"Prediction: {prediction}")
