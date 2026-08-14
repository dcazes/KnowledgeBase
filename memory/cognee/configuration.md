---
type: HowTo
title: Cognee Configuration
description: Configure Cognee — LLM/embedding providers via cognee.config or .env, graph/vector/relational backends, data dir, pipeline options.
resource: https://docs.cognee.ai
tags: [cognee, configuration, env, backends]
timestamp: 2026-08-13T00:00:00Z
---

# Configuration

## Provider config (Python or .env)

```python
import cognee
from cognee.infrastructure.databases.vector.embeddings import EmbeddingConfig

cognee.llm.set_llm_provider("openai", api_key="sk-...", model="gpt-4o")
cognee.llm.set_embedding_provider("openai", api_key="sk-...", model="text-embedding-3-small")
```

Or `.env`:

```env
LLM_PROVIDER=openai            # openai | anthropic | ollama | azure_openai | gemini
LLM_MODEL=gpt-4o
LLM_API_KEY=sk-...
EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=text-embedding-3-small
EMBEDDING_API_KEY=sk-...
```

Local via Ollama: `LLM_PROVIDER=ollama`, `LLM_MODEL=llama3.1`, `OLLAMA_API_BASE=http://localhost:11434`.

## Storage backends

```env
RELATIONAL_DB_PROVIDER=postgres     # postgres | sqlite
RELATIONAL_DB_HOST=localhost
RELATIONAL_DB_PORT=5432
RELATIONAL_DB_USER=cognee
RELATIONAL_DB_PASSWORD=cognee
RELATIONAL_DB_NAME=cognee
VECTOR_DB_PROVIDER=lancedb            # lancedb | qdrant | weaviate | milvus
GRAPH_DB_PROVIDER=networkx            # networkx | neo4j
```

## Data directory

`DATA_ROOT_DIR` (default `~/.cognee`) holds cached data, logs, and the embedded LanceDB.

## Pipeline options

`cognee.add(...)` accepts `dataset_name`, `chunk_size`, `overwrite`, and output flags; `cognify` supports `graph_model` / `include_metadata` / `cognify_pipeline` choices.

# Citations

[1] [Cognee docs — configuration](https://docs.cognee.ai)
[2] [Cognee GitHub — config](https://github.com/topoteretes/cognee)
