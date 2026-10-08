import streamlit as st
from backend.settings_manager import load_settings, save_settings

st.title("⚙️ Settings")

settings = load_settings()

current_theme = settings.get("theme", "System")

theme = st.radio(
    "Choose your preferred theme",
    ["System", "Light", "Dark"],
    index=["System", "Light", "Dark"].index(current_theme)
)

if st.button("💾 Save Settings", use_container_width=True):
    settings["theme"] = theme
    save_settings(settings)
    st.success("Settings saved successfully!")