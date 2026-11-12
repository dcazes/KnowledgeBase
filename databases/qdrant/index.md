---
type: Software
title: Qdrant
description: Open-source vector database and search engine written in Rust — HNSW indexing with payload filtering, dense, sparse and multi-vector (late-interaction) search, hybrid queries with fusion, quantization, and distributed deployment; the default store for many RAG and memory tools.
resource: https://github.com/qdrant/qdrant
tags: [qdrant, vector-database, rust, hybrid-search, rag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: qdrant-github
    resource: "https://github.com/qdrant/qdrant"
    title: "qdrant/qdrant on GitHub"
    author: "site:github.com"
  - id: qdrant-docs
    resource: "https://qdrant.tech/documentation/"
    title: "Qdrant documentation"
    author: "site:qdrant.tech"
---

# Qdrant

**Qdrant** stores vectors with JSON payloads and finds nearest neighbours fast, with filters applied *during* the search. It is the default or recommended vector store for [Mem0](../../memory/mem0/index.md), [MemOS](../../memory/memos/index.md) and many RAG stacks, and runs anywhere from an embedded Python mode to a distributed cluster.

| | |
|---|---|
| Category | [Vector databases](../../concepts/vector-databases.md) |
| License | Apache-2.0 |
| Language | Rust |
| Latest release | v1.20.0 (2026-10-22); `qdrant-client` 1.20.0 |
| Ports | 6333 (REST + Web UI at `/dashboard`), 6334 (gRPC) |

## Contents

* [Overview](overview.md) — collections, points, payloads, search types
* [Installation](installation.md) — Docker, embedded, cloud
* [Snippets](snippets.md) — create, upsert, filtered and hybrid search
* [AI Integration](ai-integration.md) — RAG, memory, frameworks

## Related

* Concepts: [Vector databases](../../concepts/vector-databases.md) · [Embeddings](../../concepts/embeddings.md) · [RAG](../../concepts/rag.md)
* Peers: [pgvector](../pgvector/index.md); graph stores [Neo4j](../neo4j/index.md), [FalkorDB](../falkordb/index.md)
* Comparison: [Databases alternatives](../alternatives.md)
