---
type: Reference
title: Cognee Configuration
description: Configure Cognee's LLM and embedding providers (OpenAI by default, Ollama and others), graph, vector and relational storage backends, and access control via environment variables.
resource: https://docs.cognee.ai
tags: [cognee, configuration, ollama, neo4j, pgvector, env]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cognee-docs
    resource: "https://docs.cognee.ai"
    title: "Cognee documentation"
    author: "site:docs.cognee.ai"
  - id: cognee-env
    resource: "https://github.com/topoteretes/cognee/blob/main/.env.template"
    title: "Cognee .env.template"
    author: "site:github.com"
---

# Cognee — Configuration

Configuration is environment-driven; start from `.env.template` in the repository.

## Models

```bash
LLM_API_KEY=...                 # with only this set, Cognee uses OpenAI for the LLM and embeddings
LLM_PROVIDER=ollama             # or openai, anthropic, gemini, custom (OpenAI-compatible)
LLM_MODEL=qwen3:14b
LLM_ENDPOINT=http://localhost:11434/v1
EMBEDDING_PROVIDER=ollama
EMBEDDING_MODEL=nomic-embed-text
EMBEDDING_DIMENSIONS=768
```

Note that the upstream Kuzu project is no longer maintained; for long-lived deployments prefer Neo4j or another supported graph store.

The official guide covers fully local operation with [Ollama](../../runtime/ollama/index.md); any [OpenAI-compatible](../../concepts/openai-compatible-api.md) endpoint such as [vLLM](../../runtime/vllm/index.md) or [LiteLLM](../../runtime/litellm/index.md) also works.

## Storage

Cognee separates three stores, each pluggable:

| Store | Defaults | Alternatives |
|---|---|---|
| Graph | Kuzu, embedded (`GRAPH_DATABASE_PROVIDER=kuzu`) | [Neo4j](../../databases/neo4j/index.md), remote Kuzu, Turso; [FalkorDB](../../databases/falkordb/index.md), Neptune, Memgraph via adapters |
| Vector | LanceDB, embedded (`VECTOR_DB_PROVIDER=lancedb`) | [Qdrant](../../databases/qdrant/index.md), [pgvector](../../databases/pgvector/index.md), Weaviate, Milvus, Chroma |
| Relational | SQLite (`DB_PROVIDER=sqlite`) | PostgreSQL, Turso |

Embedded defaults need no services, which is why the library works out of the box. Community adapters live in `topoteretes/cognee-community`.

## Access control

`ENABLE_BACKEND_ACCESS_CONTROL` toggles multi-tenant mode with per-user datasets and permissions. Leave it on for shared deployments.

## Related

[Cognee index](index.md) · [Installation](installation.md) · [Vector databases](../../concepts/vector-databases.md)
