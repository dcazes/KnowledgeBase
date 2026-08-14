---
type: Concept
title: LightRAG Overview
description: How LightRAG works — incremental knowledge-graph construction from documents, dual-level (low/high) retrieval, query modes, storage.
resource: https://lightrag.readthedocs.io/en/latest/
tags: [lightrag, overview, rag, graph, retrieval]
timestamp: 2026-08-13T00:00:00Z
---

# Overview

LightRAG is **retrieval-augmented generation with an incremental knowledge graph**: it extracts entities and relations from documents into a graph at index time, then answers queries by combining graph traversal (high-level) with keyword/vector search (low-level). The result is answers that cite both specific passages and the overall themes of the corpus.

## Indexing pipeline

1. **Chunk** documents (configurable chunk size/token size).
2. **Entity + relation extraction** via LLM → nodes/edges with descriptions.
3. **Incremental graph upsert** — new documents merge into the existing graph (no full rebuild), unlike GraphRAG's batch global indexes.
4. Optional **deduplication** pass for near-duplicate entities.

## Dual-level retrieval

* **Low level** — keyword/embedding match on raw text (precise facts, quotes).
* **High level** — LLM-based entity/relation extraction from the query, matched against the graph (themes, connections).

Queries can run in four modes: `naive` (no graph), `local` (low-level), `global` (high-level), or `hybrid` (both, default).

## Storage

Backend via `KV_STORAGE` / `VECTOR_STORAGE` / `GRAPH_STORAGE` env vars:

| Layer | Options |
|---|---|
| KV | `JsonKVStorage` (default), `RedisKVStorage` |
| Vector | `NanoVectorDBStorage` (default, embedded), `MilvusStorage`, `PGVectorStorage`, `QdrantStorage` |
| Graph | `NetworkXStorage` (default), `Neo4JStorage`, `MemgraphStorage` |

## Server vs library

Same engine behind a FastAPI server (`lightrag-server`, Docker images `hkuds/lightrag`). Local checkout provides both; the compose files use SQLite/Redis + NanoVectorDB by default.

# Citations

[1] [LightRAG docs](https://lightrag.readthedocs.io/en/latest/)
[2] [LightRAG GitHub](https://github.com/HKUDS/LightRAG)
[3] [Paper (arXiv 2410.05779)](https://arxiv.org/abs/2410.05779)
