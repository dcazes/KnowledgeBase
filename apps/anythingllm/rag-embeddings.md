---
type: Concept
title: AnythingLLM RAG & Embeddings
description: How AnythingLLM ingests documents and websites, which embedders and vector databases it supports (LanceDB default; pgvector, Qdrant, Chroma, Weaviate, Milvus, Pinecone and others), and tuning retrieval.
resource: https://docs.anythingllm.com
tags: [anythingllm, rag, embeddings, vector-databases]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: anythingllm-docs
    resource: "https://docs.anythingllm.com"
    title: "AnythingLLM documentation"
    author: "site:docs.anythingllm.com"
  - id: anythingllm-github
    resource: "https://github.com/Mintplex-Labs/anything-llm"
    title: "Mintplex-Labs/anything-llm on GitHub"
    author: "site:github.com"
---

# AnythingLLM — RAG & Embeddings

## Ingestion

Upload PDFs, Office files, text and code, or use data connectors (websites, GitHub repos, YouTube transcripts, Confluence and others). Documents are parsed, chunked and embedded once, then attached to workspaces.

## Embedders

Built-in local embedder (default), Ollama, LM Studio, LocalAI, OpenAI, Azure, Cohere, Voyage and other providers. Choose before embedding large collections — changing it means re-embedding ([Embeddings](../../concepts/embeddings.md)).

## Vector stores

| Store | Notes |
|---|---|
| LanceDB | Default, embedded, zero setup |
| [pgvector](../../databases/pgvector/index.md) | Postgres extension |
| [Qdrant](../../databases/qdrant/index.md) | Dedicated vector DB |
| Chroma, Weaviate, Milvus/Zilliz, Pinecone, Astra DB | Other options |

See [Vector databases](../../concepts/vector-databases.md).

## Tuning

Adjust chunk size and overlap, similarity threshold and top-N per workspace; pin critical documents to include them in full context; use query mode for strict answers.

## Related

[AnythingLLM index](index.md) · [RAG](../../concepts/rag.md)
