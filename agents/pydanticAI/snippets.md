---
type: CheatSheet
title: PydanticAI Snippets
description: PydanticAI cheat sheet — agent definition, structured output, tools, RunContext deps, streaming, local Ollama models.
resource: https://pydantic.dev/docs/ai/
tags: [pydantic, ai, snippets, cheat-sheet]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: pydanticai-docs
    resource: "https://pydantic.dev/docs/ai/"
    title: "PydanticAI docs"
    author: "site:pydantic.dev"
---

# Pydantic AI — Snippets

## Minimal agent

```python
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o-mini", instructions="Say hello.")
print(agent.run_sync("hi").output)
```

## Structured output (typed)

```python
from pydantic import BaseModel
from pydantic_ai import Agent

class Response(BaseModel):
    reply: str
    confidence: float

agent = Agent("openai:gpt-4o-mini", result_type=Response)
out = agent.run_sync("weather?").output
print(out.reply, out.confidence)
```

## Tool

```python
@agent.tool
async def get_weather(city: str) -> str:
    """Look up weather for a city."""
    return f"sunny in {city}"
```

## Dependencies

```python
from pydantic_ai import RunContext

@agent.tool
async def lookup(ctx: RunContext[MyDeps], q: str) -> str:
    return ctx.deps.api.call(q)

res = await agent.run("search", deps=MyDeps())
```

## Local model (Ollama)

```python
agent = Agent("ollama:gemma3:12b")
```

## Streaming

```python
async with agent.run_stream("story") as stream:
    async for chunk in stream:
        print(chunk, end="")
```

## Cost/usage

```python
result = agent.run_sync("hi")
print(result.cost())   # request tokens, model, etc.
```
