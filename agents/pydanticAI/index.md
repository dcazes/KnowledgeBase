---
type: Software
title: Pydantic AI
description: Typed Python agent framework from the Pydantic team — model-agnostic agent loop with structured outputs, dependency injection, tools and toolsets, MCP and A2A, durable execution, Pydantic Evals, Logfire observability, and the Harness of snap-on capabilities for long-running agents.
resource: https://github.com/pydantic/pydantic-ai
tags: [pydantic-ai, agent-frameworks, python, structured-output, typing]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pydantic-ai-github
    resource: "https://github.com/pydantic/pydantic-ai"
    title: "pydantic/pydantic-ai on GitHub"
    author: "site:github.com"
  - id: pydantic-ai-docs
    resource: "https://pydantic.dev/docs/ai/"
    title: "Pydantic AI documentation"
    author: "site:pydantic.dev"
---

# Pydantic AI

**Pydantic AI** brings the "FastAPI feeling" to agents: you declare an agent with a model, typed dependencies and a typed output, register Python functions as tools, and get validated results back. It is model-agnostic, increasingly the foundation other projects build on ([browser-use](../../browsers/browser-use/index.md) 1.0 runs on it), and ships companion libraries for evals and long-running agents.

| | |
|---|---|
| Category | [Agent frameworks](../../concepts/agent-frameworks.md) |
| License | MIT |
| Language | Python (`pydantic-ai`, slim variant `pydantic-ai-slim`) |
| Latest release | v2.68.0 (2026-11-12) |
| Companions | Pydantic AI Harness (capabilities), Pydantic Evals, Pydantic Graph, Logfire |

## Contents

* [Overview](overview.md) — agents, outputs, deps, tools, capabilities
* [Core concepts](pydantic_ai.md) — the agent loop, toolsets, durable execution, graphs
* [Installation](installation.md) — slim installs and extras
* [Configuration](configuration.md) — models, providers, settings
* [Snippets](snippets.md) — typed extraction, tools, MCP, streaming
* [AI Integration](ai-integration.md) — MCP/A2A, Logfire, evals, local models

## Related

* Concepts: [Agent frameworks](../../concepts/agent-frameworks.md) · [Structured output](../../concepts/structured-output.md) · [Tool calling](../../concepts/tool-calling.md) · [Evals](../../concepts/evals.md)
* Built on: [Pydantic](../../tools/pydantic/index.md)
* Peers: [LangGraph](../langgraph/index.md), [CrewAI](../crewai/index.md), [Dify](../dify/index.md) (low-code)
* Comparison: [Agents alternatives](../alternatives.md)
