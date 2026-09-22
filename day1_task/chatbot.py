
"""System 1: Plain LLM chatbot with no private-data access."""

from config import client, MODEL, QUESTIONS, banner

SYSTEM_PROMPT = """
You are a friendly Personal Library Assistant.

You do not have access to the user's private book collection,
reading history, or library tools.

Answer general book-related questions helpfully.
If a question requires private library information,
explain that you cannot access it.
Never pretend to have checked or updated the user's library.
"""


def chatbot(question):
    """Generate a response using the LLM alone."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    banner("SYSTEM 1: PLAIN CHATBOT")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", chatbot(question))
        print("-" * 70)