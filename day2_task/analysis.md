# Day 2 Task – Analysis

## Scenario: Student Trip Planner – Switzerland

The scenario involves planning a 7-day trip to Switzerland for 10 students. Fictional sample travel costs are used to compare Direct Prompting, Chain-of-Thought (CoT), and ReAct. The task includes budget calculation, itinerary feasibility, room allocation, and retrieving travel-cost information using tools.

### Sample Travel Data

| Expense | Cost |
|---|---:|
| Round-trip flight per student | ₹45,000 |
| Hotel per student per night | ₹8,000 |
| Food per student per day | ₹2,500 |
| Local transport per student (7 days) | ₹12,000 |
| Total budget per student | ₹1,30,500 |
| Total budget for 10 students | ₹13,05,000 |

## Comparison Table

| Basis for Comparison | Direct Prompting | Chain-of-Thought (CoT) | ReAct Agent |
|---|---|---|---|
| Reasoning Depth | Provides a direct answer without explicitly requesting step-by-step reasoning. | Breaks the trip-planning problem into smaller reasoning steps. | Combines reasoning with tool actions and observations to solve the problem. |
| Tool Usage | Does not use external tools; relies on the information provided in the prompt. | Does not use tools; reasons using the available information. | Uses tools to retrieve fictional travel costs and calculate the trip budget. |
| Reliability on Multi-step Questions | May overlook costs or make mistakes in multi-step calculations. | Step-by-step prompting can make calculations easier to follow and verify. | Tool-based retrieval and calculation can improve reliability, provided the tools return correct results. |
| Transparency | Shows the final answer, with limited explanation. | Shows the reasoning steps leading to the answer. | Shows tool calls and observations, making the information-gathering process traceable. |
| Speed / Cost | Usually faster and requires fewer tokens. | May take longer due to additional reasoning output. | May take longer because of multiple tool calls and reasoning steps. |
| Consistency Across Repeated Runs | Answers may vary across runs. | Reasoning and answers may vary across runs. | Tool outputs remain consistent when the same fixed sample data is used, although responses and tool-call sequences may vary. |

## Reasoning and Budget Observations

Using the fictional sample data, the total estimated cost is ₹1,30,500 per student and ₹13,05,000 for 10 students. The six sightseeing days are sufficient to allocate two days each to three destinations, excluding arrival and departure days. Ten students sharing two students per room require five rooms. If two students cancel, the remaining eight students require four rooms at the same occupancy.

Direct Prompting, CoT, and ReAct approach the scenario differently. Direct Prompting gives a quick response, CoT provides a structured reasoning process, and ReAct can retrieve information through tools before calculating the budget. The actual accuracy and response length of each approach should be recorded from the program outputs.

## Self-Consistency Observation

Self-consistency generates multiple CoT responses using a non-zero temperature and selects the most frequent final answer. For this task, five runs at a temperature of 0.8 can be compared using the extracted final answers. At temperature 0, responses are likely to be more similar, reducing the benefit of majority voting. The observed answers and majority result should be added after running the experiment.

## Suitability

Direct Prompting is suitable for simple questions with clearly provided information. CoT is useful for multi-step reasoning and calculations when the required data is already available. ReAct is suitable when the task requires external information or tool-based calculations, such as retrieving travel costs and computing a group budget.

## Conclusion

This experiment compares Direct Prompting, CoT, and ReAct on a student trip-planning scenario. It demonstrates the differences between direct answers, step-by-step reasoning, and reasoning combined with tool use. The most suitable approach depends on whether the task requires only the supplied information, careful reasoning, or external data retrieval and calculation.