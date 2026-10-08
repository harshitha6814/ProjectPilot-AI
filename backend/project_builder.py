import os
import json
import re

from groq import Groq
from backend.config import GROQ_API_KEY


# ==========================================
# GROQ CLIENT
# ==========================================

client = Groq(api_key=GROQ_API_KEY)


# ==========================================
# PROJECT BLUEPRINT PROMPT
# ==========================================

PROJECT_BUILDER_PROMPT = """
You are an expert Senior Software Architect.

Convert the given software project specification into
a practical development blueprint.

Generate these sections:

# 🏗️ Project Architecture

# 📁 Recommended Folder Structure

# 🧩 Modules

# 🔌 Main APIs

# 🔄 System Flow

# 🚀 Development Steps

Rules:

- Keep the architecture realistic.
- Do not overcomplicate the project.
- Use the technologies mentioned in the specification.
- Keep it suitable for a final-year student.
- Do not invent unnecessary technologies.
- Keep all sections consistent.
"""


# ==========================================
# FILE STRUCTURE PROMPT
# ==========================================

FILE_STRUCTURE_PROMPT = """
You are an expert software architect.

The user has provided a software project specification.

Your task is to generate a basic starter project structure.

Return ONLY valid JSON.

The JSON must have this exact structure:

{
    "folders": [
        "folder_name",
        "another_folder"
    ],
    "files": [
        {
            "path": "folder/file.py",
            "content": "starter file content"
        }
    ]
}

Rules:

- Create a practical starter structure.
- Do not create unnecessary files.
- Use the technologies mentioned in the project specification.
- Include important configuration files.
- Include important backend/frontend entry files when appropriate.
- File contents should be simple starter templates.
- Do not generate huge amounts of code.
- Do not include markdown.
- Do not include explanations outside the JSON.
"""


# ==========================================
# BUILD PROJECT BLUEPRINT
# ==========================================

def build_project(project_specification):

    prompt = f"""
PROJECT SPECIFICATION:

{project_specification}


Create the complete development blueprint according
to your instructions.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "system",
                "content": PROJECT_BUILDER_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3,
        max_tokens=3000
    )

    return response.choices[0].message.content


# ==========================================
# CLEAN PROJECT NAME
# ==========================================

def clean_project_name(project_name):

    cleaned_name = re.sub(
        r"[^a-zA-Z0-9_-]",
        "_",
        project_name.strip()
    )

    if not cleaned_name:
        cleaned_name = "generated_project"

    return cleaned_name


# ==========================================
# GENERATE FILE STRUCTURE
# ==========================================

def generate_file_structure(project_specification):

    prompt = f"""
PROJECT SPECIFICATION:

{project_specification}


Generate the starter project structure as valid JSON.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "system",
                "content": FILE_STRUCTURE_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2,
        max_tokens=5000
    )

    result = response.choices[0].message.content.strip()

    # Remove accidental markdown code fences
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return json.loads(result)


# ==========================================
# CREATE PROJECT STRUCTURE
# ==========================================

def create_project_structure(
    project_name,
    project_specification
):

    safe_name = clean_project_name(project_name)

    # Create generated_projects directory
    base_directory = os.path.join(
        os.getcwd(),
        "generated_projects"
    )

    os.makedirs(
        base_directory,
        exist_ok=True
    )

    # Create project directory
    project_path = os.path.join(
        base_directory,
        safe_name
    )

    os.makedirs(
        project_path,
        exist_ok=True
    )

    # Ask AI for project files
    structure = generate_file_structure(
        project_specification
    )

    # ======================================
    # CREATE FOLDERS
    # ======================================

    folders = structure.get(
        "folders",
        []
    )

    for folder in folders:

        folder_path = os.path.join(
            project_path,
            folder
        )

        os.makedirs(
            folder_path,
            exist_ok=True
        )

    # ======================================
    # CREATE FILES
    # ======================================

    files = structure.get(
        "files",
        []
    )

    created_files = []

    for file_info in files:

        file_path = file_info.get(
            "path",
            ""
        )

        content = file_info.get(
            "content",
            ""
        )

        if not file_path:
            continue

        # Prevent paths from escaping
        # the generated project directory.
        safe_file_path = os.path.normpath(
            file_path
        )

        if safe_file_path.startswith(".."):
            continue

        full_file_path = os.path.join(
            project_path,
            safe_file_path
        )

        parent_directory = os.path.dirname(
            full_file_path
        )

        if parent_directory:
            os.makedirs(
                parent_directory,
                exist_ok=True
            )

        with open(
            full_file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        created_files.append(
            safe_file_path
        )

    return {
        "project_path": project_path,
        "created_files": created_files
    }