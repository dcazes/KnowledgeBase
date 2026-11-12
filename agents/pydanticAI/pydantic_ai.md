---
type: Concept
title: Pydantic AI Core Concepts
description: Deeper Pydantic AI concepts — the agent run loop and message history, output validation and retries, toolsets including MCP and deferred tools, durable execution integrations, Pydantic Graph, multi-agent patterns and the A2A/AG-UI interfaces.
resource: https://pydantic.dev/docs/ai/
tags: [pydantic-ai, concepts, agent-loop, durable-execution, graph]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pydantic-ai-docs
    resource: "https://pydantic.dev/docs/ai/"
    title: "Pydantic AI documentation"
    author: "site:pydantic.dev"
---

# Pydantic AI — Core Concepts

## The run loop

1. Build the request: instructions, message history, tool definitions, output schema.
2. Call the model.
3. If it calls tools, execute them (with dependencies from `RunContext`), append results, repeat.
4. When it returns output, validate against the output type; on validation failure, send the error back and retry.

`result.all_messages()` returns the history so you can continue a conversation or store it in [agent memory](../../concepts/agent-memory.md).

## Toolsets

Tools can come from functions, from [MCP](../../concepts/mcp.md) servers (stdio or HTTP), or be **deferred** — returned to your code for human approval or external execution before the run resumes (human-in-the-loop).

## Durable execution

Integrations with durable workflow engines (such as Temporal and DBOS) let long agent runs survive restarts — the same goal [LangGraph](../langgraph/index.md) addresses with checkpointers.

## Multi-agent patterns

* **Delegation:** a tool calls another agent.
* **Hand-off:** application code passes control between agents.
* **Pydantic Graph:** typed state machines for complex flows.

See [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md).

## Interfaces

Agents can be exposed as an [A2A](../../concepts/a2a.md) server, over the AG-UI protocol to front ends, or as a terminal chat with `clai` / `agent.to_cli_sync()`.

## Related

[Pydantic AI index](index.md) · [Snippets](snippets.md)
