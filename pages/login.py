import streamlit as st
from database import check_user

st.title("👤 Login")

st.write("Welcome back to AI ProjectPilot.")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if email and password:

        user = check_user(email, password)

        if user:

            st.session_state.logged_in = True
            st.session_state.username = user[1]
            st.session_state.email = user[2]

            st.success(f"✅ Welcome, {user[1]}! Login successful.")

            st.info("Redirecting to your dashboard...")

            st.switch_page("pages/dashboard.py")

        else:

            st.error("❌ Invalid email or password.")

    else:

        st.warning("⚠️ Please enter both email and password.")