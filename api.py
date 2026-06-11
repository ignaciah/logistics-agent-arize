python
from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent
from phoenix.otel import register

app = FastAPI()
register(project_name="logistics-agent-api", auto_instrument=True)

class Query(BaseModel):
    query: str
    user_id: str

@app.post("/agent")
def run_agent(q: Query):
    resp = agent.invoke({"messages": [{"role": "user", "content": q.query}]})
    return {"answer": resp['messages'][-1].content}
