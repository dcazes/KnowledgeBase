---
type: Reference
title: Pydantic AI Snippets
description: Pydantic AI snippets — typed extraction, tools with dependency injection, MCP servers as toolsets, streaming, and a coding agent from the Harness.
resource: https://pydantic.dev/docs/ai/
tags: [pydantic-ai, snippets, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pydantic-ai-docs
    resource: "https://pydantic.dev/docs/ai/"
    title: "Pydantic AI documentation"
    author: "site:pydantic.dev"
  - id: pydantic-ai-github
    resource: "https://github.com/pydantic/pydantic-ai"
    title: "pydantic/pydantic-ai on GitHub"
    author: "site:github.com"
---

# Pydantic AI — Snippets

## Typed extraction

```python
from pydantic import BaseModel
from pydantic_ai import Agent

class Person(BaseModel):
    name: str
    age: int
    city: str

agent = Agent("openai:gpt-5-mini", output_type=Person)
print(agent.run_sync("Alice is 31 and lives in Lisbon").output)
```

## Tools with dependencies

```python
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext

@dataclass
class Deps:
    user_id: str

agent = Agent("anthropic:claude-sonnet-4-5", deps_type=Deps,
              instructions="Answer using the user's orders.")

@agent.tool
def recent_orders(ctx: RunContext[Deps], limit: int = 5) -> list[str]:
    """Return the user's most recent orders."""
    return fetch_orders(ctx.deps.user_id, limit)    # your code

agent.run_sync("What did I order last?", deps=Deps(user_id="u-42"))
```

## MCP server as a toolset

```python
from pydantic_ai.mcp import MCPServerStdio
browser = MCPServerStdio("npx", args=["@playwright/mcp@latest", "--headless"])
agent = Agent("openai:gpt-5-mini", toolsets=[browser])
```

## Streaming

```python
async with agent.run_stream("Summarise RAG in 3 bullets") as result:
    async for chunk in result.stream_text():
        print(chunk, end="")
```

## Coding agent from the Harness

```python
from pydantic_ai import Agent
from pydantic_ai_harness import Coder
Agent("anthropic:claude-sonnet-4-5", capabilities=[Coder()]).to_cli_sync()
```

## Related

[Pydantic AI index](index.md) · [Core concepts](pydantic_ai.md)
