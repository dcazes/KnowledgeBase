---
type: Software
title: pgvector
description: Open-source vector similarity search for PostgreSQL — vector, halfvec, bit and sparsevec types, HNSW and IVFFlat indexes, exact and approximate search, iterative index scans for filtered queries — so embeddings live next to relational data.
resource: https://github.com/pgvector/pgvector
tags: [pgvector, postgres, vector-database, sql, rag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pgvector-github
    resource: "https://github.com/pgvector/pgvector"
    title: "pgvector/pgvector on GitHub"
    author: "site:github.com"
---

# pgvector

**pgvector** adds vector columns and nearest-neighbour search to PostgreSQL. If you already run Postgres, it is often the simplest [vector database](../../concepts/vector-databases.md): embeddings, metadata, permissions and transactions in one place, queried with SQL. Many tools in this vault support it, and [Honcho](../../memory/honcho/index.md) and [Hindsight](../../memory/hindsight/index.md) require Postgres with vectors.

| | |
|---|---|
| Category | [Vector databases](../../concepts/vector-databases.md) |
| License | PostgreSQL License |
| Language | C (Postgres extension) |
| Latest | v0.8.7 (tag) |
| Availability | Most managed Postgres services (AWS RDS/Aurora, Supabase, Neon, Azure, GCP) |

## Contents

* [Overview](overview.md) — types, operators, indexes, filtering
* [Installation](installation.md) — packages, Docker image, managed services
* [Snippets](snippets.md) — SQL for tables, indexes, queries, hybrid search
* [AI Integration](ai-integration.md) — tools and frameworks that use it

## Related

* Concepts: [Vector databases](../../concepts/vector-databases.md) · [Embeddings](../../concepts/embeddings.md) · [RAG](../../concepts/rag.md)
* Peers: [Qdrant](../qdrant/index.md); graph in Postgres via Apache AGE ([LightRAG](../../memory/lightrag/configuration.md))
* Comparison: [Databases alternatives](../alternatives.md)
