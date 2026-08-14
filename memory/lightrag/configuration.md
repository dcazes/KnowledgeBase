---
type: HowTo
title: LightRAG Configuration
description: Configure LightRAG — working dir, LLM/embedding providers (Ollama/OpenAI/Claude), storage backends via env, chunking settings, query modes.
resource: https://lightrag.readthedocs.io/en/latest/
tags: [lightrag, configuration, env, ollama, storage]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: lightrag-docs-configuration
    resource: "https://lightrag.readthedocs.io/en/latest/"
    title: "LightRAG docs — configuration"
    author: "site:lightrag.readthedocs.io"
  - id: lightrag-github-env-example
    resource: "https://github.com/HKUDS/LightRAG"
    title: "LightRAG GitHub — .env.example"
    author: "site:github.com"
---

# Configuration

## Working directory

All state (graph JSON, vector DB, docs) lands in `WORKING_DIR` (default `./rag_storage`). Point at a persistent volume for deployments.

## Providers (env)

```env
LLM_BINDING_HOST=0.0.0.0
LLM_BINDING_PORT=9621
LLM_MODEL=gpt-4o-mini
LLM_API_KEY=sk-...
# or local via Ollama:
LLM_BINDING=ollama
LLM_MODEL=llama3.1
OLLAMA_HOST=http://localhost:11434
# embeddings:
EMBEDDING_BINDING=ollama
EMBEDDING_MODEL=nomic-embed-text
OLLAMA_EMBEDDING_HOST=http://localhost:11434
```

`LLM_BINDING` selects provider (`openai`, `ollama`, `anthropic`, `azure_openai`, `gemini`, …); `EMBEDDING_BINDING` similarly.

## Storage (env)

```env
KV_STORAGE=JsonKVStorage            # JsonKVStorage | RedisKVStorage
VECTOR_STORAGE=NanoVectorDBStorage  # NanoVectorDBStorage | MilvusStorage | PGVectorStorage | QdrantStorage
GRAPH_STORAGE=NetworkXStorage       # NetworkXStorage | Neo4JStorage | MemgraphStorage
```

Server env prefix `LIGHTRAG_` is not required for CLI/library usage; env is read directly.

## Chunking

```python
INSERT_BATCH_SIZE = 10          # docs per batch
MAX_PARALLEL_INSERT = 4
CHUNK_TOKEN_SIZE = 1200         # token budget per chunk
CHUNK_OVERLAP_TOKEN_SIZE = 100
```
(These live as module constants / server settings; for server, `LIGHTRAG_*` env or query params.)

## Query modes

`mode` in the query API: `naive` (keyword only), `local` (low-level), `global` (high-level), `hybrid` (default, both).
