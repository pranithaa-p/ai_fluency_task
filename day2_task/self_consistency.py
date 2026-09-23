"""Self-Consistency experiment for the trip planner."""

import re
from collections import Counter
from config import client, MODEL

RUNS = 5

QUESTION = """
For one student on a 7-day Switzerland trip:
round-trip flight = Rs. 45,000
hotel = Rs. 8,000 per night for 7 nights
food = Rs. 2,500 per day for 7 days
local transport for 7 days = Rs. 12,000

Calculate the total trip cost per student.

End your response with exactly:
FINAL ANSWER: INR <number>
"""


def run_once(temperature):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Solve carefully. Show concise calculation "
                    "steps. The last line must be FINAL ANSWER: "
                    "INR followed by the numerical amount."
                )
            },
            {"role": "user", "content": QUESTION}
        ],
        temperature=temperature
    )

    return response.choices[0].message.content or ""


def extract_answer(text):
    matches = re.findall(
        r"FINAL ANSWER:\s*INR\s*([\d,]+(?:\.\d+)?)",
        text,
        flags=re.IGNORECASE
    )

    if matches:
        value = float(matches[-1].replace(",", ""))
        return f"INR {value:,.2f}"

    return "Could not extract final answer"


def run_experiment(temperature):
    answers = []

    print(f"\nTEMPERATURE = {temperature}")

    for run in range(1, RUNS + 1):
        response = run_once(temperature)
        answer = extract_answer(response)
        answers.append(answer)

        print(f"Run {run}: {answer}")

    counts = Counter(answers)
    majority, count = counts.most_common(1)[0]

    print(
        f"Majority answer: {majority} "
        f"({count}/{RUNS} runs)"
    )

    return answers, majority, count


if __name__ == "__main__":
    print("=" * 65)
    print("SELF-CONSISTENCY EXPERIMENT")
    print("=" * 65)

    print("Question: Calculate the 7-day trip cost per student.")
    print("Expected answer: INR 130,500.00")

    run_experiment(temperature=0.8)
    run_experiment(temperature=0)