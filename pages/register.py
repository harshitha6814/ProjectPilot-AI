import streamlit as st
import sqlite3
from database import add_user

st.title("Register")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    if not username or not email or not password:
        st.error("Please fill in all fields.")
    elif password != confirm_password:
        st.error("Passwords do not match.")
    else:
        try:
            add_user(username, email, password)
            st.success("Account created successfully! You can now log in.")
        except sqlite3.IntegrityError:
            st.error("Username or email already exists.")