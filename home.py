import streamlit as st

# -------------------------------------------------
# PAGE TITLE
# -------------------------------------------------

st.title("🚀 AI ProjectPilot")

st.subheader("From Idea to Submission — Powered by AI")

st.divider()

# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------

st.header("Build Complete Software Projects with AI")

st.write("""
AI ProjectPilot helps students and professionals transform ideas into complete software projects.

Whether you're building a final-year project, preparing for placements,
developing a startup prototype, or participating in a hackathon,
AI ProjectPilot guides you through the entire journey.
""")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🚀 Get Started", use_container_width=True):
        st.success("Welcome to AI ProjectPilot!")

with col2:
    st.button("Explore Features", use_container_width=True)

st.divider()

# -------------------------------------------------
# FEATURES
# -------------------------------------------------

st.header("✨ Core Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### 🤖 AI Project Wizard

Get personalized project recommendations based on your skills and goals.
""")

with col2:
    st.info("""
### 🛠 AI Project Builder

Generate complete project structures and source code.
""")

with col3:
    st.info("""
###  Documentation Generator

Generate reports, PPTs, README files and documentation.
""")

col4, col5, col6 = st.columns(3)

with col4:
    st.info("""
###  Debug Assistant

Detect and fix project issues quickly.
""")

with col5:
    st.info("""
###  Interview Simulator

Practice viva and technical interviews.
""")

with col6:
    st.info("""
###  Resume Booster

Improve resume quality and ATS score.
""")

st.divider()

# -------------------------------------------------
# PROJECT STATISTICS
# -------------------------------------------------

st.header("📊 AI ProjectPilot")

a, b, c, d = st.columns(4)

a.metric("Projects", "100+")
b.metric("Technologies", "25+")
c.metric("AI Modules", "12")
d.metric("Success Rate", "95%")

st.divider()

# -------------------------------------------------
# WHY CHOOSE
# -------------------------------------------------

st.header(" Why Choose AI ProjectPilot?")

st.success("""
✅ Complete Project Guidance

✅ AI-Powered Development

✅ Automatic Documentation

✅ Resume Enhancement

✅ Interview Preparation

✅ Industry Readiness Analysis

Everything from **Idea → Submission** in one platform.
""")

st.divider()

st.caption("© 2026 AI ProjectPilot")