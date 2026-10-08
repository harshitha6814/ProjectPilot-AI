import streamlit as st

from backend.project_builder import create_project_structure


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Project Builder",
    page_icon="🛠",
    layout="wide"
)


# ==========================================
# PAGE TITLE
# ==========================================

st.title("🛠 AI Project Builder")

st.write(
    "Convert your project specification into "
    "a real starter project structure."
)


# ==========================================
# PROJECT NAME
# ==========================================

project_name = st.text_input(
    "📌 Project Name",
    placeholder="Example: AI Resume Analyzer"
)


# ==========================================
# PROJECT SPECIFICATION
# ==========================================

project_details = st.text_area(
    "📄 Project Specification",
    height=350,
    placeholder=(
        "Paste the project specification generated "
        "by the AI Project Wizard here..."
    )
)


# ==========================================
# BUILD BUTTON
# ==========================================

if st.button(
    "🚀 Build Complete Project",
    use_container_width=True
):

    if project_name.strip() == "":

        st.warning(
            "Please enter a project name."
        )

    elif project_details.strip() == "":

        st.warning(
            "Please provide the project specification."
        )

    else:

        try:

            with st.spinner(
                "🤖 AI is creating your project..."
            ):

                result = create_project_structure(
                    project_name,
                    project_details
                )

            st.success(
                "✅ Project created successfully!"
            )

            # ==================================
            # PROJECT LOCATION
            # ==================================

            st.subheader("📁 Project Location")

            st.code(
                result["project_path"]
            )

            # ==================================
            # CREATED FILES
            # ==================================

            st.subheader("📄 Created Files")

            if result["created_files"]:

                for file in result["created_files"]:

                    st.write(
                        f"📄 `{file}`"
                    )

            else:

                st.info(
                    "No files were created."
                )

        except Exception as e:

            st.error(
                "❌ Something went wrong while "
                "creating the project."
            )

            st.exception(e)