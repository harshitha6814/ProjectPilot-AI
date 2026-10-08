from backend.ai_engine import generate_project


def generate_file(file_type, project_details):

    prompt = f"""
You are an expert Software Engineer.

Project Details:
{project_details}

Generate ONLY the content for this file:

{file_type}

Rules:
- Do not explain anything.
- Return only the file content.
- Make it production-ready.
"""

    return generate_project(prompt)