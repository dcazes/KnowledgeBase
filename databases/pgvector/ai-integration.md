---
type: Playbook
title: pgvector AI Integration
description: pgvector in AI stacks — storage for Honcho, Hindsight, Mem0, LightRAG, Cognee, Open WebUI, AnythingLLM, Dify and n8n; framework vector-store classes; and keeping embeddings next to application data.
resource: https://github.com/pgvector/pgvector
tags: [pgvector, integration, rag, memory]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pgvector-github
    resource: "https://github.com/pgvector/pgvector"
    title: "pgvector/pgvector on GitHub"
    author: "site:github.com"
---

# pgvector — AI Integration

* **Requires it:** [Honcho](../../memory/honcho/installation.md), [Hindsight](../../memory/hindsight/configuration.md) (Postgres-based memory).
* **Supports it:** [Mem0](../../memory/mem0/configuration.md), [LightRAG](../../memory/lightrag/configuration.md) (with Apache AGE for graphs), [Cognee](../../memory/cognee/configuration.md), [Open WebUI](../../apps/openwebui/configuration.md), [AnythingLLM](../../apps/anythingllm/rag-embeddings.md), [Dify](../../agents/dify/architecture.md), [n8n](../../apps/n8n/ai-integration.md).
* **Frameworks:** LangChain `PGVector`, LlamaIndex `PGVectorStore`, plain SQL from [Pydantic AI](../../agents/pydanticAI/index.md) tools.
* **Why it matters for agents:** row-level security and joins let retrieval respect user permissions — important for multi-tenant [RAG](../../concepts/rag.md) and [agent memory](../../concepts/agent-memory.md).

## Related

[pgvector index](index.md) · [Vector databases](../../concepts/vector-databases.md)
