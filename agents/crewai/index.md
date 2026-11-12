---
type: Software
title: CrewAI
description: Python framework for multi-agent automation — role-based agents collaborating in Crews, event-driven Flows for precise control, tools, memory and knowledge, independent of LangChain; commercial AMP suite for deployment and observability.
resource: https://github.com/crewAIInc/crewAI
tags: [crewai, multi-agent, agent-frameworks, python, flows]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: crewai-github
    resource: "https://github.com/crewAIInc/crewAI"
    title: "crewAIInc/crewAI on GitHub"
    author: "site:github.com"
  - id: crewai-docs
    resource: "https://docs.crewai.com"
    title: "CrewAI documentation"
    author: "site:docs.crewai.com"
---

# CrewAI

**CrewAI** organises agents like a team: each agent has a **role, goal and backstory**, tasks are assigned to agents, and a **Crew** runs them sequentially or under a manager agent. **Flows** add event-driven, deterministic control around crews and single LLM calls.

| | |
|---|---|
| Category | [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md) · [Agent frameworks](../../concepts/agent-frameworks.md) |
| License | MIT |
| Language | Python (`crewai`) |
| Latest release | 1.15.40 (2026-11-11) |
| Commercial | CrewAI AMP (control plane, tracing, governance) |

## Contents

* [Overview](overview.md) — agents, tasks, crews, processes, flows, memory
* [Installation](installation.md) — pip/uv, CLI project scaffolding
* [Snippets](snippets.md) — a crew in Python, a flow, YAML config
* [AI Integration](ai-integration.md) — models via LiteLLM, tools and MCP, memory, tracing

## Related

* Concepts: [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md) · [Agent frameworks](../../concepts/agent-frameworks.md)
* Peers: [LangGraph](../langgraph/index.md), [Pydantic AI](../pydanticAI/index.md), [Dify](../dify/index.md), [n8n](../../apps/n8n/index.md)
* Comparison: [Agents alternatives](../alternatives.md)
