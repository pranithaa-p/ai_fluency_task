"""ReAct agent for the Switzerland Student Trip Planner."""

import json
from config import client, MODEL
from tools import TOOL_FUNCTIONS

SYSTEM_PROMPT = """
You are a trip-planning assistant for a group of 10 students
travelling to Switzerland for 7 days.

All travel prices are fictional sample data.

The user wants the total trip budget per student and for
the group.

You MUST use lookup_travel_cost to retrieve:
flight, hotel, food, and transport prices.

Then use calculate_trip_budget with the retrieved values.
Do not invent or assume prices.

Use the tools before giving the final answer.
After observing the tool results, summarize the result clearly.
"""

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_travel_cost",
            "description": "Look up a fictional travel cost.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": ["flight", "hotel", "food", "transport"]
                    }
                },
                "required": ["category"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_trip_budget",
            "description": "Calculate per-student and group trip cost.",
            "parameters": {
                "type": "object",
                "properties": {
                    "students": {"type": "integer"},
                    "days": {"type": "integer"},
                    "flight": {"type": "number"},
                    "hotel_per_night": {"type": "number"},
                    "food_per_day": {"type": "number"},
                    "transport": {"type": "number"}
                },
                "required": [
                    "students", "days", "flight",
                    "hotel_per_night", "food_per_day",
                    "transport"
                ]
            }
        }
    }
]


def run_react_agent():
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                "Plan the budget for 10 students visiting "
                "Switzerland for 7 days. Retrieve the travel "
                "prices and calculate the total cost per "
                "student and for the group."
            )
        }
    ]

    for step in range(1, 12):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOL_SCHEMAS,
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print("\nFINAL ANSWER:")
            print(message.content or "")
            return

        for tool_call in message.tool_calls:
            name = tool_call.function.name
            arguments = json.loads(
                tool_call.function.arguments
            )

            print(f"\nSTEP {step}")
            print(f"ACTION: {name}({arguments})")

            function = TOOL_FUNCTIONS.get(name)

            if function is None:
                result = {"error": "Tool not found"}
            else:
                result = function(**arguments)

            print(f"OBSERVATION: {result}")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

    print("Stopped: maximum tool-call steps reached.")


if __name__ == "__main__":
    print("=" * 65)
    print("REACT AGENT — SWITZERLAND STUDENT TRIP PLANNER")
    print("=" * 65)

    run_react_agent()