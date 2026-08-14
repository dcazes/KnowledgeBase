---
type: HowTo
title: PydanticAI Configuration
description: Configure PydanticAI agents — model selection, Agent(...) args (instructions/result_type/tools), deps via RunContext, environment/provider keys, v2 capabilities.
resource: https://pydantic.dev/docs/ai/
tags: [pydantic, ai, configuration, agents, models]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: pydanticai-docs-agents
    resource: "https://pydantic.dev/docs/ai/agents/"
    title: "PydanticAI docs — agents"
    author: "site:pydantic.dev"
  - id: pydanticai-docs-models
    resource: "https://pydantic.dev/docs/ai/models/"
    title: "PydanticAI docs — models"
    author: "site:pydantic.dev"
---

# Configuration

## Model selection

```python
from pydantic_ai import Agent

Agent("openai:gpt-4o-mini")            # OpenAI (OPENAI_API_KEY env)
Agent("anthropic:claude-opus-4-7")     # Anthropic (ANTHROPIC_API_KEY env)
Agent("ollama:gemma3:12b")             # local — Ollama at http://localhost:11434
Agent("gemini-1.5-flash")              # Gemini
```

v2 uses Responses-API-style model names (`openai-chat:`, `openai:` …). Provider keys come from standard env vars.

## Agent(...) options

```python
agent = Agent(
    "openai:gpt-4o-mini",
    system_prompt="You are a helpful assistant.",
    result_type=MyModel,        # structured output contract
    deps_type=MyDeps,           # typed run context
    tools=[...],                # or @agent.tool decorators
)
```

## Dependencies (RunContext)

```python
from dataclasses import dataclass
from pydantic_ai import Agent, RunContext

@dataclass
class Deps:
    api_key: str

@agent.tool
async def get_data(ctx: RunContext[Deps], query: str) -> str:
    return f"key={ctx.deps.api_key} q={query}"

result = await agent.run("query the data", deps=Deps(api_key="..."))
```

## v2 capabilities (optional, loaded on demand)

```python
from pydantic_ai.capabilities import Thinking, WebSearch, Capability
from pydantic_ai.mcp import MCPToolset

agent = Agent(
    "anthropic:claude-opus-4-7",
    capabilities=[
        Thinking(effort="high"),
        WebSearch(),
        Capability(id="github", toolset=MCPToolset("https://mcp.example.com/github"), defer_loading=True),
    ],
)
```

## Env for local models

Set `OLLAMA_HOST` (default `http://localhost:11434`) when using `ollama:` providers; see [Ollama](../../runtime/ollama/index.md).
