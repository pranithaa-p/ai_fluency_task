
"""Shared configuration for the Personal Library Assistant."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Common test questions for all three systems
QUESTIONS = [
    "Have I read The Hobbit?",
    "Find an unread fantasy book under 400 pages.",
    "Mark The Midnight Library as currently reading.",
    "Find an unread mystery book and recommend one."
]


def banner(title):
    print(
        f"\n=== {title} | provider: {PROVIDER} "
        f"| model: {MODEL} ===\n"
    )