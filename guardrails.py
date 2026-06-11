python
from guardrails import Guard
from guardrails.hub import ToxicLanguage
from phoenix.otel import register
from agent import agent

tracer_provider = register(project_name="logistics-agent-guardrails", auto_instrument=True)
guard = Guard().use(ToxicLanguage(on_fail="fix"))

def safe_response(user_input: str) -> str:
    validated = guard.validate(user_input)
    if not validated.validation_passed:
        return "I cannot process that. Please rephrase."
    resp = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
    return guard.parse(resp['messages'][-1].content)
