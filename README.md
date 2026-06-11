 Repository Structure

```
logistics-agent-arize/
├── .gitignore
├── README.md
├── requirements.txt
├── setup.sh                 (optional: environment setup script)
├── agent.py                 (core agent + tools + tracing)
├── guardrails.py
├── evaluate.py
├── api.py
├── tests/
│   ├── __init__.py
│   └── test_agent.py
├── examples/
│   └── sample_queries.txt
└── config/
    └── .env.example
```
markdown
# Logistics Agent with Arize Phoenix

Autonomous customer support agent for order status, returns, and escalation – with full observability and evaluation using Arize Phoenix.

## Quick Start

```bash
# Clone
git clone https://github.com/ignaciah/logistics-agent-arize.git
cd logistics-agent-arize

# Setup
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Launch Phoenix (terminal 1)
python -m phoenix.server.main serve

# Run agent (terminal 2)
python agent.py
```

Features

· 🔧 Tools: get_order, create_return, escalate_to_human
· 📊 Full tracing with Arize Phoenix (every LLM call, tool use, decision)
· 🛡️ Guardrails for toxicity and PII
· 📈 LLM-as-judge evaluation
· 🚀 FastAPI deployment

Environment

Copy config/.env.example to .env and add your GeminiAI key.

Monitor

Open http://localhost:6006 to see traces, evaluate runs, and debug failures.

License

MIT

