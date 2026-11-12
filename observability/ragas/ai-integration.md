---
type: Playbook
title: Ragas AI Integration
description: Using Ragas across the stack — evaluating LightRAG, Dify or custom RAG pipelines, logging scores to Langfuse, running in CI alongside promptfoo, and evaluating agents built with LangGraph or Pydantic AI.
resource: https://docs.ragas.io
tags: [ragas, integration, langfuse, lightrag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ragas-docs
    resource: "https://docs.ragas.io"
    title: "Ragas documentation"
    author: "site:docs.ragas.io"
---

# Ragas — AI Integration

* **RAG systems:** [LightRAG](../../memory/lightrag/ai-integration.md) returns retrieved contexts specifically for Ragas; also [Dify](../../agents/dify/rag-pipeline.md), [Open WebUI](../../apps/openwebui/rag.md) or your own [Qdrant](../../databases/qdrant/index.md)/[pgvector](../../databases/pgvector/index.md) pipeline.
* **Observability:** push scores to [Langfuse](../langfuse/ai-integration.md) traces to watch quality in production.
* **CI:** run a fixed evaluation set on every change; [promptfoo](../promptfoo/index.md) suits assertion-style checks, Ragas suits RAG quality metrics.
* **Agents:** agent and tool-call metrics for [LangGraph](../../agents/langgraph/index.md) and [Pydantic AI](../../agents/pydanticAI/index.md) traces.

## Related

[Ragas index](index.md) · [Evals](../../concepts/evals.md)
