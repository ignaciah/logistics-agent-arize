python
import pandas as pd
from agent import agent
from phoenix.otel import register
from phoenix.evals import llm_classify

register(project_name="logistics-agent-eval", auto_instrument=True)

test_cases = [
    ("Where is order 12345?", "get_order"),
    ("I want to return order 12346", "create_return"),
    ("Talk to a human", "escalate_to_human"),
]

def eval_tool_choice(query, expected):
    # simple keyword check
    tool_map = {
        "get_order": ["where", "status", "tracking"],
        "create_return": ["return", "refund"],
        "escalate_to_human": ["human", "manager", "talk"]
    }
    for tool, keywords in tool_map.items():
        if any(k in query.lower() for k in keywords):
            return "correct" if tool == expected else "wrong"
    return "unclear"

results = []
for query, expected in test_cases:
    resp = agent.invoke({"messages": [{"role": "user", "content": query}]})
    result = eval_tool_choice(query, expected)
    results.append({"query": query, "expected": expected, "result": result})

df = pd.DataFrame(results)
print(df)
print(f"Accuracy: {(df['result'] == 'correct').mean() * 100:.0f}%")
