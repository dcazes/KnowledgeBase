---
type: Concept
title: Pydantic AI Integration
description: Use Pydantic schemas as agent contracts — PydanticAI typed output, the local template (pydantic_ai_template.py), JSON Schema for LLM tools.
resource: https://docs.pydantic.dev
tags: [pydantic, integration, pydanticai, agents]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: pydantic-docs
    resource: "https://docs.pydantic.dev"
    title: "Pydantic docs"
    author: "site:docs.pydantic.dev"
  - id: pydanticai-docs
    resource: "https://ai.pydantic.dev"
    title: "PydanticAI docs"
    author: "site:ai.pydantic.dev"
---

# AI Integration

Pydantic's superpower in this stack: **schemas as contracts** for LLM/agent I/O.

## Typed agent output (PydanticAI)

```python
from pydantic import BaseModel, Field
from pydantic_ai import Agent

class AgentResponse(BaseModel):
    reply: str
    created_user: "User | None" = None

agent = Agent('google:gemini-2.5-flash', result_type=AgentResponse)
result = agent.run_sync("create user Alice")
print(result.output.created_user.name)   # typed, validated
```

## Local template

`programs/pydantic/pydantic_ai_template.py` (present, verified 2026-08-12) demonstrates:

1. Reusing an exact Pydantic validation schema (`User` with `extra="forbid"`, patterns, Literals).
2. An `AgentResponse` model that forces the agent's reply shape.
3. Wiring into a PydanticAI agent (Gemini in the template).

The venv (`programs/pydantic/.venv`, pydantic 2.13.4) is ready for running it.

## JSON Schema interop

`User.model_json_schema()` exports a JSON Schema usable by any LLM function-calling / structured-output API — the same trick tools like LiteLLM and the agent stack use to constrain tool args.

## In this stack

* Foundation of [PydanticAI](../../agents/pydanticAI/index.md) (v2.28.0).
* Used implicitly by FastAPI, LiteLLM, Firecrawl SDK, AnythingLLM configs, etc.
