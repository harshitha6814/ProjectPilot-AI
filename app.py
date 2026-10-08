import streamlit as st

from database import (
    create_users_table,
    create_project_history_table
)


# ==========================================
# DATABASE SETUP
# ==========================================

create_users_table()
create_project_history_table()


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI ProjectPilot",
    page_icon="🚀",
    layout="wide"
)


# ==========================================
# PAGES
# ==========================================

home = st.Page(
    "home.py",
    title="Home",
    icon="🏠"
)

login = st.Page(
    "pages/login.py",
    title="Login",
    icon="👤"
)

register = st.Page(
    "pages/register.py",
    title="Register",
    icon="📝"
)

dashboard = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon="📊"
)

ai_wizard = st.Page(
    "pages/ai_wizard.py",
    title="AI Project Wizard",
    icon="🤖"
)

ai_builder = st.Page(
    "pages/ai_builder.py",
    title="AI Project Builder",
    icon="🛠"
)

history = st.Page(
    "pages/history.py",
    title="History",
    icon="📚"
)

history_view = st.Page(
    "pages/history_view.py",
    title="Open Project",
    icon="📂"
)
settings = st.Page(
    "pages/settings.py",
    title="Settings",
    icon="⚙️"
)


# ==========================================
# NAVIGATION
# ==========================================

pg = st.navigation(
    {
        "MAIN": [
            home,
            dashboard
        ],

        "AI TOOLS": [
            ai_wizard,
            ai_builder,
            history,
            history_view,  
        ],

        "ACCOUNT": [
            login,
            register,
            settings
        ]
    }
)


# ==========================================
# RUN APP
# ==========================================

pg.run()