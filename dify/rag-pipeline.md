---
type: Reference
title: Dify — RAG Pipeline
description: How Dify ingests documents, chunks and embeds them, stores vectors, and retrieves context for generation.
resource: https://docs.dify.ai/guides/knowledge-base
tags: [dify, rag, retrieval, embedding, knowledge-base, indexing]
timestamp: 2026-07-09T00:53:00Z
---

# Pipeline stages

```
Document (PDF / PPT / DOCX / text / web)
   │
   ▼  Upload + parse (text extraction; PDF/PPT supported OOTB)
Cleaned text
   │
   ▼  Chunking (rules / recursive / semantic)
Chunks
   │
   ▼  Embedding (via configured model provider)
Vectors
   │
   ▼  Store in selected vector DB (weaviate/qdrant/pgvector/chroma/milvus)
        │
Query ──► embed ──► ANN search ──► top-k chunks ──► LLM context
```

# Key concepts

* **Knowledge Base** — a named collection of indexed documents.
* **Indexing modes** — Dify supports both **semantic (vector)** retrieval and **full-text** (and hybrid) depending on the vector store.
* **Chunking** — configurable strategy; affects recall. Smaller chunks = finer retrieval, more calls.
* **Embedding model** — chosen in model settings; must match the store's dimension.
* **Retrieval** — top-k chunks are injected into the prompt (or returned to a workflow).

# Using it

1. Create a Knowledge Base in the UI (or API).
2. Upload documents; Dify extracts text (PDF/PPT built-in).
3. Pick embedding model + chunk strategy; index.
4. Attach the KB to an App (Chatbot / Workflow) — retrieval becomes a node.

# Notes for this stack

* Dify's RAG is **self-contained** — it does not require your SearXNG or Firecrawl, but you *could* feed scraped content (via Firecrawl) into a KB.
* The vector store is selected at deploy time (see [Architecture](architecture.md)); switching later means re-indexing.
* Embeddings can use your `:4000` proxy if it exposes an embeddings endpoint (set the embedding model provider accordingly).

# Citations

[1] [Knowledge Base guide (docs)](https://docs.dify.ai/guides/knowledge-base)
[2] [Architecture — vector stores](architecture.md)
