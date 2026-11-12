---
type: Reference
title: LangGraph Snippets
description: LangGraph snippets — a prebuilt tool-calling agent, a custom StateGraph with conditional edges, Postgres checkpointing, and a human approval interrupt.
resource: https://docs.langchain.com/oss/python/langgraph/overview
tags: [langgraph, snippets, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langgraph-docs
    resource: "https://docs.langchain.com/oss/python/langgraph/overview"
    title: "LangGraph documentation"
    author: "site:docs.langchain.com"
---

# LangGraph — Snippets

## Prebuilt agent

```python
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get the weather for a city."""
    return f"Sunny in {city}"

agent = create_agent("openai:gpt-5-mini", tools=[get_weather])
agent.invoke({"messages": [{"role": "user", "content": "Weather in Lisbon?"}]})
```

## Custom graph

```python
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]
    approved: bool

def draft(state):  return {"messages": [("assistant", "Draft reply...")]}
def review(state): return {"approved": True}

g = StateGraph(State)
g.add_node("draft", draft); g.add_node("review", review)
g.add_edge(START, "draft"); g.add_edge("draft", "review")
g.add_conditional_edges("review", lambda s: END if s["approved"] else "draft")
app = g.compile()
```

## Durable state and human approval

```python
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.types import interrupt, Command

def send_email(state):
    ok = interrupt({"question": "Send this email?", "draft": state["messages"][-1]})
    return {"approved": ok}

with PostgresSaver.from_conn_string("postgresql://...") as saver:
    app = g.compile(checkpointer=saver)
    cfg = {"configurable": {"thread_id": "t1"}}
    app.invoke({"messages": []}, cfg)          # pauses at interrupt
    app.invoke(Command(resume=True), cfg)      # resume after the human says yes
```

## Related

[LangGraph index](index.md) · [Overview](overview.md)
