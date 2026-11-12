---
type: Playbook
title: vLLM AI Integration
description: Using vLLM as the serving layer for agents and RAG — OpenAI and Anthropic-compatible endpoints, prefix caching for agent loops, embeddings and rerankers, LoRA adapters, and fronting it with LiteLLM.
resource: https://docs.vllm.ai
tags: [vllm, integration, agents, rag, litellm]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: vllm-docs
    resource: "https://docs.vllm.ai"
    title: "vLLM documentation"
    author: "site:docs.vllm.ai"
---

# vLLM — AI Integration

## Why agents like vLLM

* **Prefix caching** makes repeated system prompts, tool schemas and long RAG contexts cheap across an agent's many calls.
* **Concurrency**: [multi-agent](../../concepts/multi-agent-orchestration.md) systems fire many parallel requests; continuous batching absorbs them.
* **Reliable structure**: grammar-constrained [structured output](../../concepts/structured-output.md) and parser-based [tool calling](../../concepts/tool-calling.md).

## Connecting tools

| Tool | How |
|---|---|
| [LiteLLM](../litellm/configuration.md) | `hosted_vllm/<model>` with `api_base` |
| [Open WebUI](../../apps/openwebui/index.md) | OpenAI connection to `http://vllm:8000/v1` |
| [Graphiti](../../memory/graphiti/snippets.md), [LightRAG](../../memory/lightrag/configuration.md), [Cognee](../../memory/cognee/configuration.md), [Mem0](../../memory/mem0/configuration.md) | OpenAI-compatible base URL |
| [LangGraph](../../agents/langgraph/index.md), [PydanticAI](../../agents/pydanticAI/index.md), [CrewAI](../../agents/crewai/index.md) | OpenAI provider with custom base URL |
| [Claude Code](../../agents/claude-code/index.md)-style clients | Anthropic Messages API endpoint |

## RAG stack on one box

Serve a chat model, an embedding model and a reranker with vLLM, store vectors in [Qdrant](../../databases/qdrant/index.md) or [pgvector](../../databases/pgvector/index.md), parse documents with [Docling](../../ingestion/docling/index.md) — a fully self-hosted [RAG](../../concepts/rag.md) pipeline.

## Related

[vLLM index](index.md) · [Local inference](../../concepts/local-inference.md) · [Runtime alternatives](../alternatives.md)
