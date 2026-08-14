---
type: HowTo
title: Mem0 Configuration
description: Configure Mem0 — .env provider keys, config.json for vector_store / graph_store / embedder, scoping defaults, on_conflict behavior.
resource: https://docs.mem0.ai
tags: [mem0, configuration, env, vector-store, graph-store]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: mem0-docs-configuration
    resource: "https://docs.mem0.ai/components/llms"
    title: "Mem0 docs — configuration"
    author: "site:docs.mem0.ai"
  - id: mem0-github-config-json
    resource: "https://github.com/mem0ai/mem0"
    title: "Mem0 GitHub — config.json"
    author: "site:github.com"
---

# Configuration

## Environment keys (`.env`)

```env
OPENAI_API_KEY=sk-...        # or ANTHROPIC_API_KEY / GEMINI_API_KEY / OLLAMA_HOST
```

LLM provider is selected from `config.json` `llm.provider` (default `openai`). Locally, Ollama is the natural choice: `provider: "ollama"`, `model: "llama3.1"` (see [Ollama](../../runtime/ollama/index.md)).

## config.json

```json
{
  "llm": { "provider": "openai", "config": { "model": "gpt-4o" } },
  "embedder": { "provider": "openai", "config": { "model": "text-embedding-3-small" } },
  "vector_store": { "provider": "qdrant", "config": { "collection_name": "mem0", "embedding_model_dims": 1536 } },
  "graph_store": { "provider": "neo4j", "config": { "url": "bolt://localhost:7687", "username": "neo4j", "password": "..." } }
}
```

Notable options:

* `vector_store` — `qdrant` (default, auto-spawned embedded), `milvus`, `pinecone`, `weaviate`, `chroma`, `faiss`, `pgvector`.
* `graph_store` — `neo4j` or `falkordb`; enables entity/fact graph memory; `customize_graph` + `graph_llm` for graph-specific models.
* `on_conflict` — `"replace"` (default) or `"keep"` for overlapping memories.
* `version` — set `"v1.1"` in llm config to enable the newer "full memory" API variants.

## Defaults

* No `config.json` → embedded Qdrant (localhost) + OpenAI models + gpt-4o.
* `Memory.from_config()` reads `config.json` from CWD or `MEM0_CONFIG_PATH`.
