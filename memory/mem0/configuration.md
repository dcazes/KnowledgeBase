---
type: Reference
title: Mem0 Configuration
description: Configure Mem0's LLM, embedder, vector store and reranker providers, including a fully local Ollama + Qdrant setup, and the search defaults introduced by the 2026 algorithm.
resource: https://docs.mem0.ai/open-source/configuration
tags: [mem0, configuration, ollama, qdrant, pgvector, embeddings]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: mem0-oss-configuration
    resource: "https://docs.mem0.ai/open-source/configuration"
    title: "Configure the OSS Stack"
    author: "site:docs.mem0.ai"
  - id: mem0-migration-v3
    resource: "https://docs.mem0.ai/migration/oss-v2-to-v3"
    title: "Open Source: Migrating to the New Memory Algorithm"
    author: "site:docs.mem0.ai"
---

# Mem0 — Configuration

Each component takes a `provider` and a provider-specific `config`. Keys are `snake_case` in Python and `camelCase` in TypeScript. Pass the dict to `Memory.from_config()`.

```python
from mem0 import Memory

config = {
    "llm":          {"provider": "openai", "config": {"model": "gpt-5-mini", "temperature": 0.1}},
    "embedder":     {"provider": "openai", "config": {"model": "text-embedding-3-small"}},
    "vector_store": {"provider": "qdrant", "config": {"host": "localhost", "port": 6333}},
    "reranker":     {"provider": "cohere", "config": {"model": "rerank-v3.5"}},   # optional
}
memory = Memory.from_config(config)
```

## Components

| Key | Purpose | Examples of providers |
|---|---|---|
| `llm` | Extracts facts on `add()` | OpenAI, Anthropic, Gemini, AWS Bedrock, Groq, [Ollama](../../runtime/ollama/index.md), [LiteLLM](../../runtime/litellm/index.md), any [OpenAI-compatible](../../concepts/openai-compatible-api.md) endpoint |
| `embedder` | Vectorises memories and queries | OpenAI, Ollama, Hugging Face / TEI, Gemini, Bedrock |
| `vector_store` | Stores memories | [Qdrant](../../databases/qdrant/index.md) (Python default), [pgvector](../../databases/pgvector/index.md), Chroma, Milvus, Pinecone, Weaviate, Redis/Valkey, Turbopuffer, FAISS |
| `reranker` | Optional second-stage ranking | Cohere, Hugging Face cross-encoders, LLM rerankers |

Graph stores are **no longer read** by the open-source library (see [Overview](overview.md#graph-memory-moved-to-the-platform)).

## Fully local setup

```python
config = {
    "llm":      {"provider": "ollama", "config": {"model": "qwen3:8b"}},
    "embedder": {"provider": "ollama", "config": {"model": "nomic-embed-text"}},
    "vector_store": {"provider": "qdrant",
                     "config": {"host": "localhost", "port": 6333, "embedding_model_dims": 768}},
}
```

Match `embedding_model_dims` to your embedding model (768 for `nomic-embed-text`). Mem0 recommends an embedder at least as strong as a ~600M-parameter Qwen embedding model for good hybrid search — see [Embeddings](../../concepts/embeddings.md).

## Prompt customisation

`custom_instructions` (Python) / `customInstructions` (TS) steers what gets extracted, e.g. "only store preferences and project facts, never credentials". It replaces the older `custom_fact_extraction_prompt`.

## Search defaults (2026 algorithm)

| Parameter | Default | Note |
|---|---|---|
| `top_k` | 20 | was 100 |
| `threshold` | 0.1 | must be in `[0, 1]`; `0.0` disables filtering |
| `rerank` | `False` | set `True` when a reranker is configured |

## Related

[Mem0 index](index.md) · [Installation](installation.md) · [Snippets](snippets.md) · [Vector databases](../../concepts/vector-databases.md)
