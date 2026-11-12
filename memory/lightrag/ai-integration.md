---
type: Playbook
title: LightRAG AI Integration
description: Using LightRAG with chat UIs and agents — its Ollama-compatible endpoint for Open WebUI, REST and MCP access from agents, evaluation with Ragas and tracing with Langfuse.
resource: https://github.com/HKUDS/LightRAG
tags: [lightrag, integration, open-webui, mcp, ragas, langfuse]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: lightrag-github
    resource: "https://github.com/HKUDS/LightRAG"
    title: "HKUDS/LightRAG on GitHub"
    author: "site:github.com"
---

# LightRAG — AI Integration

## Chat UIs

`lightrag-server` emulates an Ollama chat model, so [Open WebUI](../../apps/openwebui/index.md) or any Ollama client can add it as a "model" and chat with your knowledge graph directly. Query-mode prefixes in the message (such as `/local` or `/mix`) choose the retrieval mode.

## Agents

* Call the REST `/query` endpoint as a tool from [LangGraph](../../agents/langgraph/index.md), [PydanticAI](../../agents/pydanticAI/index.md) or [CrewAI](../../agents/crewai/index.md).
* Community [MCP](../../concepts/mcp.md) servers wrap LightRAG for coding agents and desktop assistants.
* Use `local` for entity questions, `global` for thematic ones, `mix` as a general default.

## Evaluation and tracing

* LightRAG returns retrieved contexts with answers, which [Ragas](../../observability/ragas/index.md) uses for context precision and faithfulness metrics — see [Evals](../../concepts/evals.md).
* [Langfuse](../../observability/langfuse/index.md) tracing records extraction and query calls — see [LLM observability](../../concepts/llm-observability.md).

## When to choose LightRAG

* Document collections that grow over time, where [Microsoft GraphRAG](../graphrag/index.md)'s re-indexing is too costly.
* You want a ready WebUI with graph visualisation.
* For conversational memory rather than documents, prefer [Graphiti](../graphiti/index.md) or [Mem0](../mem0/index.md).

## Related

[LightRAG index](index.md) · [RAG](../../concepts/rag.md) · [Memory alternatives](../alternatives.md)
