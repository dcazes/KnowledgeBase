---
type: Concept
title: Agent2Agent Protocol (A2A)
description: The Agent2Agent protocol — an open standard for agents to discover each other through Agent Cards and exchange tasks, messages and artifacts over HTTP — how it complements MCP, the related Agent Client Protocol for editors, and support in frameworks and gateways.
resource: https://github.com/a2aproject/A2A
tags: [concept, a2a, protocol, multi-agent, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: a2a-github
    resource: "https://github.com/a2aproject/A2A"
    title: "a2aproject/A2A"
    author: "site:github.com"
  - id: a2a-spec
    resource: "https://a2a-protocol.org"
    title: "A2A protocol documentation"
    author: "site:a2a-protocol.org"
  - id: acp
    resource: "https://agentclientprotocol.com"
    title: "Agent Client Protocol"
    author: "site:agentclientprotocol.com"
---

# Agent2Agent Protocol (A2A)

**A2A** lets independent agents — built by different teams on different frameworks — work together. Introduced by Google in 2025 and now developed under the Linux Foundation, it reached **v1.0** in 2026 (SDK `a2a-sdk` 1.3).

## Core ideas

* **Agent Card** — a JSON document (served at a well-known URL) describing an agent's skills, endpoint and auth.
* **Tasks** — units of work with a lifecycle (submitted, working, input-required, completed…).
* **Messages and artifacts** — conversation turns and outputs (text, files, structured data).
* **Transport** — HTTP with JSON-RPC, streaming via server-sent events, push notifications for long tasks.

## A2A vs MCP

| | [MCP](mcp.md) | A2A |
|---|---|---|
| Connects | An agent to tools and data | An agent to another agent |
| Counterpart is | A deterministic tool server | An autonomous peer with its own reasoning |
| Typical use | "Call the browser tool" | "Ask the travel agent to book this" |

They are complementary: an agent may use MCP for its tools and A2A to delegate to other agents — see [Multi-agent orchestration](multi-agent-orchestration.md).

## Related protocols

* **Agent Client Protocol (ACP)** — from [Zed](../editors/zed/overview.md): connects editors to coding agents.
* **AG-UI** — agent-to-front-end event streaming (supported by [Pydantic AI](../agents/pydanticAI/pydantic_ai.md)).

## Support

[Pydantic AI](../agents/pydanticAI/pydantic_ai.md) can expose agents as A2A servers; [LiteLLM](../runtime/litellm/overview.md) has an `/a2a` endpoint; Google ADK, LangGraph and others offer adapters.

## Related

[MCP](mcp.md) · [Multi-agent orchestration](multi-agent-orchestration.md) · [Agent frameworks](agent-frameworks.md) · [Concepts index](index.md)
