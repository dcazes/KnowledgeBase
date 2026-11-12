---
type: Reference
title: LightRAG Configuration
description: Key LightRAG .env settings — LLM and embedding bindings, role-specific models, reranker, storage backends (JSON, PostgreSQL, Neo4j, MongoDB, Redis, Milvus, Qdrant, OpenSearch) and chunking.
resource: https://github.com/HKUDS/LightRAG/blob/main/env.example
tags: [lightrag, configuration, env, storage, ollama]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: lightrag-github
    resource: "https://github.com/HKUDS/LightRAG"
    title: "HKUDS/LightRAG on GitHub"
    author: "site:github.com"
  - id: lightrag-env
    resource: "https://github.com/HKUDS/LightRAG/blob/main/env.example"
    title: "LightRAG env.example"
    author: "site:github.com"
---

# LightRAG — Configuration

`env.example` works out of the box with local file-based storage, no reranker and the built-in parser; only model settings need attention.

## Models

```bash
LLM_BINDING=openai                     # keep "openai" for any OpenAI-compatible API
LLM_BINDING_HOST=http://localhost:11434/v1
LLM_MODEL=qwen3:30b-a3b
LLM_BINDING_API_KEY=...
EMBEDDING_BINDING=openai
EMBEDDING_BINDING_HOST=http://localhost:11434/v1
EMBEDDING_MODEL=bge-m3
EMBEDDING_DIM=1024                     # must match the model; fix before the first upload
```

Native bindings also exist for Ollama, Azure OpenAI, Gemini and AWS Bedrock. With reasoning models, keep reasoning effort low for extraction — it is one call per chunk.

**Role-specific models:** EXTRACT, QUERY, KEYWORDS and VLM can each use a different model, e.g. a cheap model for extraction and a strong one for answers.

## Storage

LightRAG uses four storage roles — KV, vector, graph and document status — each with selectable backends:

| Backend | Roles |
|---|---|
| JSON / NanoVectorDB / NetworkX (default) | All four, file-based |
| PostgreSQL (+ [pgvector](../../databases/pgvector/index.md), Apache AGE) | All four |
| OpenSearch | All four |
| MongoDB | All four |
| [Neo4j](../../databases/neo4j/index.md), Memgraph | Graph |
| [Qdrant](../../databases/qdrant/index.md), Milvus, Faiss | Vector |
| Redis | KV, doc status |

## Retrieval

Configure a reranker (Cohere, Jina or a local model) to enable `mix` mode as the default. Pick a chunking strategy (`Fix`, `Recursive`, `Vector`, `Paragraph`) per your documents.

## Related

[LightRAG index](index.md) · [Installation](installation.md) · [Embeddings](../../concepts/embeddings.md) · [Vector databases](../../concepts/vector-databases.md)
