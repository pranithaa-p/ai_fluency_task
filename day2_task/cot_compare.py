"""Compare Direct Prompting and Chain-of-Thought."""

from config import client, MODEL

QUESTIONS = [
    (
        "A student group has 10 students travelling to "
        "Switzerland for 7 days. Per student, the round-trip "
        "flight is Rs. 45,000, hotel is Rs. 8,000 per night, "
        "food is Rs. 2,500 per day, and 7-day local transport "
        "is Rs. 12,000. Calculate the total cost per student "
        "and for all 10 students."
    ),
    (
        "A 7-day trip has 6 full sightseeing days because "
        "the first and last days are reserved for arrival "
        "and departure. The group wants to visit 3 places "
        "and spend 2 full days at each place. Is this "
        "possible within the sightseeing days? Explain."
    ),
    (
        "Ten students are travelling together. Each hotel "
        "room accommodates 2 students. How many rooms are "
        "needed? If 2 students cancel, how many rooms are "
        "needed for the remaining group?"
    )
]

DIRECT_PROMPT = (
    "Answer the question directly and concisely. "
    "Give the final answer without showing reasoning steps."
)

COT_PROMPT = (
    "Solve the problem carefully. Work through the relevant "
    "steps, then clearly state the final answer."
)


def ask_model(system_prompt, question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print("=" * 65)
    print("DIRECT PROMPTING vs CHAIN-OF-THOUGHT")
    print("=" * 65)

    for index, question in enumerate(QUESTIONS, start=1):
        print(f"\nQUESTION {index}: {question}")

        direct = ask_model(DIRECT_PROMPT, question)
        cot = ask_model(COT_PROMPT, question)

        print("\n--- DIRECT ANSWER ---")
        print(direct)

        print("\n--- CHAIN-OF-THOUGHT ---")
        print(cot)

        print("\n" + "-" * 65)