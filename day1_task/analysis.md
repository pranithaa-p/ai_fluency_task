
# Day 1 Analysis: Personal Library Assistant

## 1. Scenario Overview

The selected scenario is a Personal Library Assistant that helps users
manage and explore their personal book collection. It should answer
questions about reading status, find books based on genre and page
count, recommend books, and update reading progress.

Three approaches were implemented and compared:

1. System 1 – Plain LLM Chatbot
2. System 2 – Rule-Based Workflow
3. System 3 – Tool-Using AI Agent

## 2. System Descriptions

### System 1: Plain LLM Chatbot

The plain chatbot uses a language model to respond to user questions.
It does not have access to the private book collection or library tools.
It can provide general book-related information, but it cannot reliably
verify personal reading status or update a user's library.

### System 2: Rule-Based Workflow

The rule-based workflow uses predefined conditions to identify the
question and execute the corresponding function. It accesses the
library data through programmed functions and can search books,
check reading status, and update a book's status.

However, it depends on fixed question patterns and predefined logic.
Questions outside those patterns may not be handled correctly.

### System 3: Tool-Using AI Agent

The tool-using AI agent uses an LLM to understand the user's request
and decide which available tool to call. It can use library functions
to search books, retrieve reading status, and update the collection.

The agent combines language understanding with access to the
application's tools. Its performance depends on the model's tool
selection and the correctness of the underlying functions.

## 3. Comparison Across Seven Criteria

| Criteria | Plain LLM Chatbot | Rule-Based Workflow | Tool-Using AI Agent |
|---|---|---|---|
| Flexibility | Understands natural language, but has no access to private library data. | Low flexibility; depends on predefined rules and question patterns. | More flexible; can interpret varied requests and select relevant tools. |
| Decision-Making | Generates responses based on its language-model knowledge, without checking the library. | Decisions are determined by fixed conditions. | Uses the LLM to decide which tool or tools are needed. |
| Tool Usage | Does not use library tools. | Calls predefined functions through programmed logic. | Selects and calls available tools based on the user's request. |
| Private-Data Access | Cannot access the user's private book collection. | Can access the in-memory library through programmed functions. | Can access the in-memory library through its available tools. |
| Multi-Step Task Handling | Cannot reliably perform actions on the library. | Can perform only the steps explicitly programmed. | Can support tool-call-and-response cycles for requests requiring actions. |
| Automation | Does not perform library operations. | Automates known tasks when their conditions match. | Can automate library tasks by choosing and invoking tools dynamically. |
| Reliability | May provide plausible but unverified answers about private data. | Predictable for supported patterns, but brittle when inputs differ. | Can handle varied requests, but depends on model decisions, tool execution, and correct data. |

## 4. Suitability Analysis

### Plain LLM Chatbot

The plain LLM chatbot is suitable for general book discussions,
summaries, and recommendations based on general knowledge.
It is not suitable as a standalone personal library manager because
it cannot access or modify the user's private collection.

### Rule-Based Workflow

The rule-based workflow is suitable for simple, repetitive, and
well-defined library operations. It provides predictable results
when user questions match the programmed conditions. However,
it becomes difficult to maintain as the number and variety of
supported requests increase.

### Tool-Using AI Agent

The tool-using AI agent is suitable for a Personal Library Assistant
that must understand natural-language requests and perform actions
using private library data. It can select tools dynamically instead
of relying entirely on fixed question patterns. However, it still
requires reliable tool implementations, validation, and appropriate
error handling.

For this scenario, the tool-using AI agent aligns most closely with
the desired functionality because it combines natural-language
understanding with access to the library's operations.

## 5. Conclusion

This task demonstrated three approaches to building a Personal
Library Assistant. The plain LLM chatbot can respond to general
questions but cannot access private library information. The
rule-based workflow can perform specific library operations
reliably when the input matches its predefined conditions, but
it lacks flexibility. The tool-using AI agent combines the
language understanding of an LLM with tools that retrieve and
modify library data. This makes it suitable for handling varied
natural-language requests that require real actions. Although
the agent offers greater flexibility, its reliability still depends
on correct tool execution and validation. The experiment
illustrates how connecting an LLM to tools can extend it beyond
text generation into task-oriented applications.