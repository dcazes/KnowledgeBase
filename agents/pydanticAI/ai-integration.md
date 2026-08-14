---
type: Concept
title: PydanticAI AI Integration
description: Integrate PydanticAI into this stack — typed output contracts, tools/MCP, local Ollama models, dependencies, structured agents alongside the Agent Stack.
resource: https://pydantic.dev/docs/ai/
tags: [pydantic, ai, integration, agents, mcp]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: pydanticai-docs
    resource: "https://pydantic.dev/docs/ai/"
    title: "PydanticAI docs"
    author: "site:pydantic.dev"
  - id: pydanticai-github
    resource: "https://github.com/pydantic/pydantic-ai"
    title: "PydanticAI GitHub"
    author: "site:github.com"
---

# Pydantic AI — AI Integration

PydanticAI is the structured-output agent framework to pair with [Pydantic](../../tools/pydantic/index.md) in this stack.

## Typed output contracts

```python
from pydantic import BaseModel, Field
from pydantic_ai import Agent

class UserOut(BaseModel):
    id: int = Field(..., gt=0)
    name: str
    role: Literal["admin", "editor", "viewer"] = "viewer"

agent = Agent("openai:gpt-4o-mini", result_type=UserOut)
out = agent.run_sync("create user alice").output
assert isinstance(out, UserOut)   # validated, typed
```

Same pattern as the local `pydantic_ai_template.py` (see [Pydantic → AI Integration](../../tools/pydantic/ai-integration.md)).

## Tools & MCP

* `@agent.tool` / `@agent.tool_plain` — typed function tools (args validated).
* **MCP toolset** (v2) — connect MCP servers as capabilities for external data/tools.

## Local models (offline)

Use `ollama:` providers for a fully-local agent (see [Ollama](../../runtime/ollama/index.md)) — e.g. `Agent("ollama:gemma3:12b")`. Complements the Agent Stack (LiteLLM :4000) and [MemOS](../../memory/memos/index.md) for memory.

## Fit here

* Not a running service — the library to build structured agents from Python.
* Schema reuse: define validation models once in Pydantic, reuse as agent result types.
