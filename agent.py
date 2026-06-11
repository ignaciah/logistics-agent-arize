```python
import os
from phoenix.otel import register
from openinference.instrumentation.langchain import LangChainInstrumentor
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()

# Tracing
tracer_provider = register(project_name="logistics-agent", auto_instrument=True)
LangChainInstrumentor().instrument()

# Tools
@tool
def get_order(order_id: str) -> str:
    """Retrieve order status and tracking."""
    mock = {
        "12345": "shipped, track at https://track.example/12345",
        "12346": "delivered",
        "12347": "processing"
    }
    return f"Order {order_id}: {mock.get(order_id, 'not found')}"

@tool
def create_return(order_id: str, reason: str) -> str:
    """Create a return label."""
    return f"Return approved for {order_id}. Reason: {reason}. RMA: RMA-{order_id}"

@tool
def escalate_to_human(user_id: str, issue: str) -> str:
    """Escalate to human support."""
    return f"Ticket created for user {user_id}: {issue}"

# Agent
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [get_order, create_return, escalate_to_human]
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = create_agent(
    llm,
    tools,
    memory=memory,
    system_prompt="You are a logistics agent. Use tools. Be concise."
)

if __name__ == "__main__":
    print("Agent ready. Type 'quit' to exit.")
    while True:
        q = input("\nUser: ")
        if q.lower() == "quit":
            break
        resp = agent.invoke({"messages": [{"role": "user", "content": q}]})
        print(f"Agent: {resp['messages'][-1].content}")
