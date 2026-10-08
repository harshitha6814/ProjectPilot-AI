import streamlit as st

# ======================================
# PROTECT DASHBOARD
# ======================================

if not st.session_state.get("logged_in", False):
    st.warning("🔒 Please login to access the Dashboard.")
    st.stop()

# ======================================
# DASHBOARD HEADER
# ======================================

st.title("📊 Dashboard")

st.success(f"Welcome, {st.session_state.username}! 👋")

st.write("Welcome to your personal AI ProjectPilot workspace.")

st.markdown("---")

# ======================================
# DASHBOARD METRICS
# ======================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Projects", "0")

with col2:
    st.metric("Documents", "0")

with col3:
    st.metric("Presentations", "0")

st.markdown("---")

# ======================================
# QUICK ACTIONS
# ======================================

st.subheader("🚀 Quick Actions")

col1, col2 = st.columns(2)

with col1:
    if st.button("🤖 AI Project Wizard", use_container_width=True):
        st.switch_page("pages/ai_wizard.py")

with col2:
    if st.button("🛠 AI Project Builder", use_container_width=True):
        st.switch_page("pages/ai_builder.py")

st.markdown("---")

# ======================================
# LOGOUT
# ======================================

st.subheader("Account")

if st.button("🚪 Logout", use_container_width=True):

    # Clear session
    st.session_state.clear()

    st.success("✅ Logged out successfully.")

    st.switch_page("home.py")