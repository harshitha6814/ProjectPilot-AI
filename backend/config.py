import os

from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")