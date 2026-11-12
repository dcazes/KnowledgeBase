---
type: Concept
title: Pydantic AI Overview
description: Pydantic AI's building blocks — Agent, typed output, dependency injection with RunContext, tools and toolsets, capabilities from the Harness, multi-agent delegation, and how it compares with other frameworks.
resource: https://pydantic.dev/docs/ai/
tags: [pydantic-ai, overview, agents, typing]
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

# Pydantic AI — Overview

| Concept | What it does |
|---|---|
| `Agent` | Model + instructions + tools + output type; run with `run`, `run_sync`, `run_stream` |
| Output type | A Pydantic model, dataclass, union or plain type; responses are validated and retried on failure — [structured output](../../concepts/structured-output.md) |
| Dependencies | Typed objects (DB clients, user info) injected into tools and instructions via `RunContext` |
| Tools / toolsets | Python functions with typed parameters become [tools](../../concepts/tool-calling.md); toolsets group them, including [MCP](../../concepts/mcp.md) servers |
| Capabilities | Snap-on behaviours: web search, file system, shell, sub-agents, context management (`ClearToolResults`, `ToolOutputLimits`) |
| Harness | Ready-made capability bundles such as `Coder` for coding agents |

## Why teams pick it

* Type checking and IDE completion all the way through the agent.
* Every major provider plus local [OpenAI-compatible](../../concepts/openai-compatible-api.md) servers, with one interface.
* First-class testing (`TestModel`, `FunctionModel`), [evals](../../concepts/evals.md) and [observability](../../concepts/llm-observability.md) via OpenTelemetry/Logfire.

## Compared with others

[LangGraph](../langgraph/index.md) gives explicit graph control and durable state; [CrewAI](../crewai/index.md) gives role-based crews; Pydantic AI is the most "plain Python" of the three and includes its own graph library for state machines when needed. See [Agent frameworks](../../concepts/agent-frameworks.md).

## Related

[Pydantic AI index](index.md) · [Core concepts](pydantic_ai.md)
