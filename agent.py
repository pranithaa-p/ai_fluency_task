
import json

from config import client, MODEL, QUESTIONS
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a Personal Library Assistant.

You can access the user's private book collection through tools.
Use the available tools whenever a question requires library data
or a change to a book's reading status.

Do not invent book details or claim an update succeeded unless
the tool confirms it.

Answer clearly and naturally using the tool results.
"""


def run_agent(question):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ]

    # Allow the model to make tool calls and then respond
    for _ in range(5):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )

        assistant_message = response.choices[0].message

        # If the model doesn't request a tool, return its answer
        if not assistant_message.tool_calls:
            return assistant_message.content

        # Add the assistant's tool-call message to conversation
        messages.append(
            assistant_message.model_dump(exclude_none=True)
        )

        # Execute each requested tool
        for tool_call in assistant_message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            function = TOOL_FUNCTIONS.get(function_name)

            if function is None:
                result = f"Unknown tool: {function_name}"
            else:
                try:
                    result = function(**arguments)
                except Exception as error:
                    result = f"Tool error: {error}"

            # Send the tool result back to the model
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

    return "The agent could not complete the request."


if __name__ == "__main__":
    print("SYSTEM 3: TOOL-USING AI AGENT\n")

    for question in QUESTIONS:
        print(f"\nQuestion: {question}")
        answer = run_agent(question)
        print(f"Answer: {answer}")