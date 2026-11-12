---
type: Playbook
title: Zep AI Integration
description: Wiring Zep into agents — the add-messages / get-context loop, official framework integrations (LangGraph, CrewAI, PydanticAI, Google ADK, AutoGen, Mastra, Vercel AI SDK) and MCP access.
resource: https://github.com/getzep/zep
tags: [zep, integration, langgraph, crewai, pydantic-ai, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: zep-github
    resource: "https://github.com/getzep/zep"
    title: "getzep/zep — examples and integrations"
    author: "site:github.com"
  - id: zep-docs
    resource: "https://help.getzep.com"
    title: "Zep documentation"
    author: "site:help.getzep.com"
---

# Zep — AI Integration

## The memory loop

1. After each turn, `thread.add_messages(...)`.
2. Before the next model call, `thread.get_context(...)` and put the returned context block in the system prompt.

Zep returns a pre-assembled, token-budgeted context string, so the agent code stays small — the platform does the [context engineering](../../concepts/context-engineering.md).

## Framework integrations

Packages in `getzep/zep/integrations/`:

* **Python:** Google ADK, Microsoft Agent Framework, AutoGen, AG2, [CrewAI](../../agents/crewai/index.md), [LangGraph](../../agents/langgraph/index.md), LiveKit, [Pydantic AI](../../agents/pydanticAI/index.md), Strands Agents
* **TypeScript:** Google ADK, Mastra, Vercel AI SDK
* **Go:** Google ADK

Reference agents in the repo show retrieval-as-tools on PydanticAI and Google ADK, and the Agent Skills loop with LangGraph, ADK and the Claude Agent SDK.

## MCP

Any [MCP](../../concepts/mcp.md) client can reach Zep without SDK code, which is the simplest route for coding agents and desktop assistants.

## When Zep fits

* You want temporal graph memory without operating a graph database → **Zep**.
* You need everything self-hosted → [Graphiti](../graphiti/index.md).
* You want a simple open-source fact store → [Mem0](../mem0/index.md).

## Related

[Zep index](index.md) · [Agent memory](../../concepts/agent-memory.md) · [Agent frameworks](../../concepts/agent-frameworks.md)
