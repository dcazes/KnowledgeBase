---
type: Concept
title: Vector Databases
description: Vector databases and indexes — approximate nearest-neighbour search (HNSW, IVF), filtering, hybrid search, quantization and multi-tenancy — comparing dedicated engines, Postgres extensions, embedded stores and graph databases with vector indexes.
resource: https://qdrant.tech/documentation/
tags: [concept, vector-database, ann, hnsw, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: qdrant-docs
    resource: "https://qdrant.tech/documentation/"
    title: "Qdrant documentation"
    author: "site:qdrant.tech"
  - id: pgvector
    resource: "https://github.com/pgvector/pgvector"
    title: "pgvector"
    author: "site:github.com"
---

# Vector Databases

A **vector database** stores [embeddings](embeddings.md) with metadata and answers "find the nearest vectors to this one" quickly, usually with filters. It is the storage layer of most [RAG](rag.md) and [agent memory](agent-memory.md) systems.

## How search works

* **ANN indexes** trade a little recall for huge speed: **HNSW** graphs (most common), IVF partitions, DiskANN for SSD-resident data.
* **Distance:** cosine, dot product or Euclidean — match what the embedding model expects.
* **Filtering:** restrict by tenant, language, date. Good engines filter *during* traversal so results stay correct ([Qdrant](../databases/qdrant/overview.md), pgvector iterative scans).
* **Hybrid:** combine dense vectors with sparse/BM25 and fuse rankings (RRF).
* **Quantization:** scalar, product or binary compression to fit more vectors in RAM.

## Options in this vault

| Type | Examples |
|---|---|
| Dedicated engine | [Qdrant](../databases/qdrant/index.md) (also Milvus, Weaviate) |
| Postgres extension | [pgvector](../databases/pgvector/index.md) |
| Embedded | LanceDB ([AnythingLLM](../apps/anythingllm/rag-embeddings.md), [Cognee](../memory/cognee/configuration.md)), Chroma ([Open WebUI](../apps/openwebui/configuration.md) default), FAISS |
| Graph DB with vector index | [Neo4j](../databases/neo4j/index.md), [FalkorDB](../databases/falkordb/index.md) — useful for [GraphRAG](graphrag.md) |

## Choosing

Already on Postgres and under tens of millions of vectors → pgvector. Large scale, heavy filtering, multivectors → a dedicated engine. Prototype or desktop app → embedded. Need relationships too → graph DB or vector + graph pair. See [Databases alternatives](../databases/alternatives.md).

## Related

[Embeddings](embeddings.md) · [RAG](rag.md) · [Knowledge graphs](knowledge-graphs.md) · [Concepts index](index.md)
