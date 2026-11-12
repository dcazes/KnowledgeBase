---
type: Playbook
title: Graphiti AI Integration
description: How to use Graphiti as agent memory — ingest each turn as an episode, retrieve facts before responding, scope by group id, and expose it over MCP or as framework tools.
resource: https://github.com/getzep/graphiti
tags: [graphiti, agent-memory, integration, mcp, langgraph]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphiti-github
    resource: "https://github.com/getzep/graphiti"
    title: "getzep/graphiti on GitHub"
    author: "site:github.com"
  - id: zep-paper
    resource: "https://arxiv.org/abs/2501.13956"
    title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
    author: "Rasmussen et al., arXiv 2501.13956"
---

# Graphiti — AI Integration

## As agent memory

1. **Ingest** — after each turn (or batch of turns), `add_episode(... source=EpisodeType.message, group_id=user_id)`. Do it in the background: ingestion makes several LLM calls.
2. **Retrieve** — before responding, `search(query, group_ids=[user_id])` and put the returned facts, with their dates, into the prompt.
3. **Reason over time** — because facts carry validity windows, the agent can answer "what changed?" questions that flat [vector memory](../../concepts/vector-databases.md) cannot.

This is the pattern the Zep paper benchmarks on LongMemEval and Deep Memory Retrieval. Compared with [Mem0](../mem0/index.md)'s flat fact list, Graphiti costs more at ingestion and gives you relationships, provenance and history.

## Through MCP

The quickest way to give a coding agent or chat client graph memory is the [MCP server](mcp-server.md): `add_memory` after meaningful events, `search_memory_facts` / `search_nodes` before acting.

## In agent frameworks

* [LangGraph](../../agents/langgraph/index.md): add a retrieval node before the model and an ingestion node after it; keep `group_id` in graph state.
* [PydanticAI](../../agents/pydanticAI/index.md): register `search` as a typed tool; Graphiti's custom types are Pydantic models too.
* [CrewAI](../../agents/crewai/index.md) / [Letta](../letta/index.md): expose search as a tool for the memory-managing agent.

## Good practice

* One `group_id` per user or tenant; enforce the mapping in your service.
* Prefer models with reliable [structured output](../../concepts/structured-output.md) for ingestion; a smaller model is fine for embeddings and reranking.
* Treat ingested content as untrusted: it is sent to the LLM unfiltered ([Agent security](../../concepts/agent-security.md)).

## Related

[Graphiti index](index.md) · [Agent memory](../../concepts/agent-memory.md) · [Context engineering](../../concepts/context-engineering.md)
