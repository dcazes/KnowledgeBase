---
type: Concept
title: LangGraph Overview
description: LangGraph concepts — StateGraph, nodes, edges and conditional routing, reducers, checkpointers for durable execution and time travel, interrupts for human-in-the-loop, stores for long-term memory, streaming modes, subgraphs and Deep Agents.
resource: https://docs.langchain.com/oss/python/langgraph/overview
tags: [langgraph, overview, stategraph, checkpointer, interrupts]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langgraph-docs
    resource: "https://docs.langchain.com/oss/python/langgraph/overview"
    title: "LangGraph documentation"
    author: "site:docs.langchain.com"
---

# LangGraph — Overview

| Concept | Meaning |
|---|---|
| `StateGraph` | A graph over a typed state (TypedDict/Pydantic); reducers define how updates merge (e.g. append messages) |
| Nodes | Functions that read state and return updates |
| Edges | Fixed or conditional transitions; cycles allowed — the agent loop is a cycle |
| Checkpointer | Persists state after every step (memory, SQLite, Postgres) → **durable execution**, resume after crashes, time travel |
| Interrupts | Pause the graph for human approval or input, then resume — human-in-the-loop |
| Store | Cross-thread **long-term memory** with optional semantic search |
| Streaming | Stream tokens, state updates or custom events |
| Subgraphs | Compose graphs; build supervisor and swarm multi-agent patterns |

Inspired by Google's Pregel and Apache Beam: execution proceeds in "super-steps" where parallel nodes run then merge state.

## Deep Agents

A higher-level package on LangGraph for agents that plan, keep a virtual file system, and spawn sub-agents — similar in spirit to the harnesses behind [Claude Code](../claude-code/index.md).

## When to choose LangGraph

You need explicit control over steps, reliable resumption, approvals, or complex multi-agent topologies. For quick role-based crews see [CrewAI](../crewai/index.md); for typed single agents see [Pydantic AI](../pydanticAI/index.md).

## Related

[LangGraph index](index.md) · [Snippets](snippets.md) · [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md)
