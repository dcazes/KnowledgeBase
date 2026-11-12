---
type: Software
title: LangGraph
description: Low-level orchestration framework from LangChain for stateful, long-running agents as graphs — durable execution with checkpointers, human-in-the-loop interrupts, short- and long-term memory, streaming, and deployment via LangSmith; Deep Agents builds on it.
resource: https://github.com/langchain-ai/langgraph
tags: [langgraph, langchain, agent-frameworks, multi-agent, python, durable-execution]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langgraph-github
    resource: "https://github.com/langchain-ai/langgraph"
    title: "langchain-ai/langgraph on GitHub"
    author: "site:github.com"
  - id: langgraph-docs
    resource: "https://docs.langchain.com/oss/python/langgraph/overview"
    title: "LangGraph documentation"
    author: "site:docs.langchain.com"
---

# LangGraph

**LangGraph** models an agent or workflow as a **graph**: nodes are functions (LLM calls, tools, your code), edges decide what runs next, and a typed **state** flows through. It trades convenience for control, which is why it is the most common choice for production agents that must pause for humans, survive failures and run for a long time.

| | |
|---|---|
| Category | [Agent frameworks](../../concepts/agent-frameworks.md) · [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md) |
| License | MIT |
| Language | Python (`langgraph` 1.2.20); JavaScript (LangGraph.js) |
| Latest | langgraph 1.2.20 (2026-11-05); CLI 0.4.43 |
| Ecosystem | LangChain (integrations), Deep Agents (high-level), LangSmith (tracing, evals, deployment) |

## Contents

* [Overview](overview.md) — graphs, state, checkpointers, interrupts, memory
* [Installation](installation.md) — packages, CLI, local server
* [Snippets](snippets.md) — prebuilt agent, custom graph, human-in-the-loop
* [AI Integration](ai-integration.md) — memory, MCP, observability, local models

## Related

* Concepts: [Agent frameworks](../../concepts/agent-frameworks.md) · [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md) · [Agent memory](../../concepts/agent-memory.md)
* Peers: [Pydantic AI](../pydanticAI/index.md), [CrewAI](../crewai/index.md), [Dify](../dify/index.md), [n8n](../../apps/n8n/index.md)
* Comparison: [Agents alternatives](../alternatives.md)
