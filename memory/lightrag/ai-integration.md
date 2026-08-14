---
type: Concept
title: LightRAG AI Integration
description: Use LightRAG as a document-grounded RAG engine — Python API, REST server, wiring into Hermes/OpenCode/MCP, vs GraphRAG and Graphify.
resource: https://lightrag.readthedocs.io/en/latest/
tags: [lightrag, integration, rag, api, server, agents]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: lightrag-docs-examples
    resource: "https://lightrag.readthedocs.io/en/latest/"
    title: "LightRAG docs — examples"
    author: "site:lightrag.readthedocs.io"
  - id: lightrag-github
    resource: "https://github.com/HKUDS/LightRAG"
    title: "LightRAG GitHub"
    author: "site:github.com"
---

# LightRAG — AI Integration

## Python API (library mode)

```python
import asyncio
from lightrag import LightRAG, QueryParam
from lightrag.llm.ollama import ollama_model_complete, ollama_embed
from lightrag.utils import EmbeddingFunc

rag = LightRAG(
    working_dir="./rag_storage",
    llm_model_func=ollama_model_complete,
    llm_model_name="llama3.1",
    embedding_func=EmbeddingFunc(
        embedding_dim=768, max_token_size=8192,
        func=lambda texts: ollama_embed(texts, embed_model="nomic-embed-text", host="http://localhost:11434"),
    ),
)
await rag.ainsert(open("notes.md").read(), split_by_character=True)
result = await rag.aquery("What themes recur across the notes?", param=QueryParam(mode="hybrid"))
```

## REST server

```bash
docker compose up -d        # server on :9621
```

```bash
curl -X POST http://localhost:9621/documents/text -H "Content-Type: application/json" \
  -d '{"text": "The sky is blue on clear days."}'
curl -X POST "http://localhost:9621/query" -H "Content-Type: application/json" \
  -d '{"query": "What color is the sky?", "mode": "hybrid"}'
```

## Agent wiring

* Point Hermes/OpenCode tools at the `/query` endpoint (server mode) or use the library in-process.
* LightRAG's graph retrieval complements [Graphiti](../graphiti/index.md) (temporal agent memory) — LightRAG for corpus Q&A, Graphiti for fact provenance.
* Distinct from [Graphify](../graphify/index.md): Graphify compiles a static folder graph once (offline); LightRAG builds incrementally and retrieves at query time.
