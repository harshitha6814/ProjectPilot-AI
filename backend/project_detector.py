from groq import Groq
from backend.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def is_project_complete(messages):

    conversation = ""

    for message in messages:

        conversation += f"{message['role']}: {message['content']}\n"

    prompt = f"""
You are a Senior Software Architect.

Read the following conversation.

{conversation}

Determine whether you have enough information to generate a complete software project specification.

A complete specification requires understanding:

- Main project idea
- Purpose
- Target users
- Main features

If enough information exists reply ONLY:

YES

Otherwise reply ONLY:

NO

Do not explain.
"""

    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0,

        max_tokens=5
    )

    return response.choices[0].message.content.strip().upper() == "YES"