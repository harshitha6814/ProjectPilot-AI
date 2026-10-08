import streamlit as st

from database import (
    get_user_id,
    get_project_history
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Project History",
    page_icon="📚",
    layout="wide"
)


# ==========================================
# PAGE TITLE
# ==========================================

st.title("📚 Project History")

st.caption(
    "View your previous ProjectPilot projects."
)


# ==========================================
# LOGIN CHECK
# ==========================================

if not st.session_state.get("logged_in", False):

    st.warning(
        "🔐 Please login to view your project history."
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
# GET PROJECT HISTORY
# ==========================================

projects = get_project_history(user_id)


# ==========================================
# NO PROJECTS
# ==========================================

if not projects:

    st.info(
        "📭 You don't have any saved projects yet."
    )

    st.write(
        "Start a conversation in the AI Project Wizard "
        "and your project will appear here."
    )


# ==========================================
# SHOW PROJECTS
# ==========================================

else:

    st.write(
        f"**{len(projects)} project(s) found.**"
    )

    st.divider()


    for project in projects:

        history_id = project[0]
        project_name = project[1]
        created_at = project[2]
        updated_at = project[3]


        with st.container(border=True):

            st.subheader(
                f"📁 {project_name}"
            )

            st.caption(
                f"Created: {created_at}"
            )

            st.caption(
                f"Last updated: {updated_at}"
            )

            if st.button(
                "📂 Open Project",
                key=f"open_{history_id}",
                use_container_width=True
            ):

                st.session_state.selected_history_id = (
                    history_id
                )

                st.switch_page(
                    "pages/history_view.py"
                )