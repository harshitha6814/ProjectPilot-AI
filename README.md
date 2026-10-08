# 🤖 ProjectPilot AI

ProjectPilot AI is an AI-powered software project planning assistant that helps users turn their project ideas into structured software projects through natural conversation.

## 📌 Project Overview

ProjectPilot AI allows users to describe their software idea and discuss it with an AI assistant. The application maintains project conversations, generates project specifications, and allows users to save and reopen previous projects.

The application also includes an AI Project Builder that can convert a project specification into a basic starter project structure with folders and files.

## ✨ Features

- 🤖 AI-powered project planning assistant
- 💬 Natural conversational interaction with the AI
- 🧠 Conversation memory within projects
- 📄 AI-generated project specifications
- ✏️ Update project specifications through conversation
- 📚 Project history for saved projects
- 🔐 User registration and login
- 🗄️ SQLite database for user and project data
- 🛠️ AI Project Builder for generating starter project structures
- 🌐 Streamlit-based web interface
- 🌍 Supports conversations in the user's language

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Large Language Model (LLM)
- SQLite
- bcrypt
- python-dotenv

## 🏗️ Application Structure

```text
AI projectpilot/
│
├── app.py
├── database.py
├── home.py
├── requirements.txt
├── .gitignore
├── .env
│
├── backend/
│   ├── ai_engine.py
│   ├── config.py
│   ├── project_builder.py
│   ├── project_detector.py
│   └── ...
│
├── pages/
│   ├── ai_wizard.py
│   ├── ai_builder.py
│   ├── history.py
│   ├── history_view.py
│   ├── login.py
│   ├── register.py
│   └── ...
│
└── assets/