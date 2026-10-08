import streamlit as st
import time

from backend.ai_engine import (
    chat,
    generate_specification,
    edit_specification
)

from database import (
    get_user_id,
    save_project_history,
    update_project_history
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ProjectPilot AI",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# PAGE TITLE
# ==========================================

st.title("🤖 ProjectPilot AI")

st.caption("Your AI Software Architect")


# ==========================================
# LOGIN CHECK
# ==========================================

if not st.session_state.get("logged_in", False):

    st.warning(
        "🔐 Please login to use the AI Project Wizard."
    )

    st.stop()


# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """Hi! 👋

I'm **ProjectPilot AI**.

I'll help you develop your project through a natural conversation.

Tell me your project idea and we'll build it together.
"""
        }
    ]


if "project_specification" not in st.session_state:

    st.session_state.project_specification = None


if "specification_generated" not in st.session_state:

    st.session_state.specification_generated = False


if "history_id" not in st.session_state:

    st.session_state.history_id = None


if "project_name" not in st.session_state:

    st.session_state.project_name = "New Project"


# ==========================================
# GET CURRENT USER ID
# ==========================================

user_email = st.session_state.email

user_id = get_user_id(user_email)


# ==========================================
# SHOW PROJECT SPECIFICATION
# ==========================================

if st.session_state.specification_generated:

    st.divider()

    st.subheader("📄 Project Specification")

    st.markdown(
        st.session_state.project_specification
    )

    st.divider()


# ==========================================
# SHOW CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ==========================================
# USER INPUT
# ==========================================

prompt = st.chat_input(
    "Message ProjectPilot AI..."
)


if prompt:

    # ======================================
    # ADD USER MESSAGE
    # ======================================

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # ======================================
    # CREATE HISTORY RECORD
    # ======================================

    if st.session_state.history_id is None:

        # Use the first user message as a
        # temporary project name.

        project_name = prompt.strip()

        if len(project_name) > 60:

            project_name = (
                project_name[:60] + "..."
            )

        st.session_state.project_name = (
            project_name
        )

        st.session_state.history_id = (
            save_project_history(
                user_id,
                st.session_state.project_name,
                st.session_state.messages,
                st.session_state.project_specification
            )
        )

    else:

        # Save the latest conversation

        update_project_history(
            st.session_state.history_id,
            user_id,
            st.session_state.project_name,
            st.session_state.messages,
            st.session_state.project_specification
        )


    st.rerun()


# ==========================================
# AI RESPONSE
# ==========================================

if (
    st.session_state.messages
    and st.session_state.messages[-1]["role"] == "user"
):

    user_message = (
        st.session_state.messages[-1]["content"]
    )


    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # ==================================
            # NORMAL CHAT
            # ==================================

            if not st.session_state.specification_generated:

                response = chat(
                    st.session_state.messages
                )

                placeholder = st.empty()

                displayed_response = ""

                for word in response.split():

                    displayed_response += (
                        word + " "
                    )

                    placeholder.markdown(
                        displayed_response + "▌"
                    )

                    time.sleep(0.01)

                placeholder.markdown(
                    displayed_response
                )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )


            # ==================================
            # EDIT PROJECT
            # ==================================

            else:

                updated_specification = (
                    edit_specification(
                        st.session_state.project_specification,
                        user_message
                    )
                )

                st.session_state.project_specification = (
                    updated_specification
                )

                response = (
                    "✅ Project specification updated."
                )

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )


    # ==========================================
    # UPDATE HISTORY AFTER AI RESPONSE
    # ==========================================

    if st.session_state.history_id is not None:

        update_project_history(
            st.session_state.history_id,
            user_id,
            st.session_state.project_name,
            st.session_state.messages,
            st.session_state.project_specification
        )


    st.rerun()