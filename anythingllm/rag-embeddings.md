---
type: Reference
title: AnythingLLM — RAG & Embeddings
description: AnythingLLM's retrieval pipeline, vector database options, and embedding model choices (incl. local nomic-embed-text).
resource: https://docs.anythingllm.com/embedder-configuration
tags: [anythingllm, rag, embeddings, vector-db, lancedb, ingestion]
timestamp: 2026-07-09T02:33:00Z
---

# Ingestion pipeline

```
Document (pdf/docx/md/url/code)
   │  parse + chunk
   ▼
Embedding model  →  vectors
   │
   ▼
Vector store (LanceDB default)
   │  query → top-k chunks
   ▼
LLM context
```

# Vector databases

| Store | Notes |
|-------|-------|
| **LanceDB** | Default; embedded, serverless; hybrid (vector + keyword); great for <1M docs |
| Chroma | Python-native, popular |
| Pinecone | Managed cloud |
| Weaviate | GraphQL, Kubernetes-native |
| Qdrant | Rust, high performance |

LanceDB needs no separate service — ideal for local-first use.

# Embedding models

**Local (recommended for privacy/no cost):**
* `nomic-ai/nomic-embed-text` (8k context, high quality) — often via Ollama.
* `sentence-transformers/all-MiniLM-L6-v2` (fast, small).
* `BAAI/bge-large-en-v1.5` (best quality, larger).

**Cloud:**
* OpenAI `text-embedding-3-large` / `-small`.
* Google `text-embedding-004`.

> On this machine, if you run Ollama, `nomic-embed-text` is the natural local choice. Without Ollama, point embeddings at an OpenAI-compatible endpoint (e.g. your `:4000` proxy, if it exposes embeddings).

# Configuration

In UI: **Settings → Embedding** (pick model + provider) and **Settings → Vector Database** (pick store). Re-ingest a workspace after changing embedding models (dimensions differ).

# Tips

* Match embedding model to your vector store's expected dimensions.
* Chunk size affects recall — smaller = finer, more calls.
* Hybrid search (LanceDB) improves keyword-heavy queries.

# Citations

[1] [Embedder config](https://docs.anythingllm.com/embedder-configuration)
[2] [Vector DB options](https://docs.anythingllm.com/vector-databases)
[3] [RAG notes (prior, grounding)](/../../kb/anythingllm/embeddings.md)
