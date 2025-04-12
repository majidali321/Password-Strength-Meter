import streamlit as st
import re
import random

blacklist = ["password", "123456", "123456789", "qwerty", "abc123", "password123"]

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in blacklist:
        feedback.append("Password is too common.")
        return 0, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    return score, feedback

def generate_strong_password(length=12):
    if length < 8:
        length = 8
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*"
    all_chars = upper + lower + digits + special

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

st.set_page_config(" Password Strength Checker", layout="centered")
st.title(" Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)

    st.markdown("---")
    if score == 4:
        st.success(" Strong Password! Great job! 🔒")
    elif score == 3:
        st.warning(" Moderate Password. Consider improving:")
        for f in feedback:
            st.write(f)
    else:
        st.error(" Weak Password. Please improve it:")
        for f in feedback:
            st.write(f)

    if score < 4:
        st.markdown("###  Suggested Strong Password:")
        st.code(generate_strong_password(), language="text")

if st.button("Generate Strong Password"):
    st.markdown("###  Generated Password:")
    st.code(generate_strong_password(), language="text")
