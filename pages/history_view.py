import streamlit as st

from database import (
    get_user_id,
    get_project
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Open Project",
    page_icon="📂",
    layout="wide"
)


# ==========================================
# LOGIN CHECK
# ==========================================

if not st.session_state.get("logged_in", False):

    st.warning(
        "🔐 Please login to open a project."
    )

    st.stop()


# ==========================================
# GET CURRENT USER
# ==========================================

user_email = st.session_state.get("email")

user_id = get_user_id(user_email)


if user_id is None:

    st.error(
        "Unable to identify the logged-in user."
    )

    st.stop()


# ==========================================
# GET SELECTED PROJECT
# ==========================================

history_id = st.session_state.get(
    "selected_history_id"
)


if history_id is None:

    st.warning(
        "⚠️ No project was selected."
    )

    st.stop()


# ==========================================
# LOAD PROJECT
# ==========================================

project = get_project(
    history_id,
    user_id
)


if project is None:

    st.error(
        "❌ Project could not be found."
    )

    st.stop()


# ==========================================
# LOAD PROJECT INTO SESSION
# ==========================================

st.session_state.messages = (
    project["messages"]
)

st.session_state.project_specification = (
    project["project_specification"]
)

st.session_state.history_id = (
    project["id"]
)

st.session_state.project_name = (
    project["project_name"]
)

st.session_state.specification_generated = (
    project["project_specification"] is not None
)


# ==========================================
# OPEN PROJECT
# ==========================================

st.switch_page(
    "pages/ai_wizard.py"
)