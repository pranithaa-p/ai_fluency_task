"""Configuration for the Switzerland Student Trip Planner."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. Add it to your .env file."
    )

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")