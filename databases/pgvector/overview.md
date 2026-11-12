---
type: Concept
title: pgvector Overview
description: pgvector concepts — vector, halfvec, bit and sparsevec types; L2, inner product, cosine, L1, Hamming and Jaccard operators; HNSW versus IVFFlat indexes; iterative index scans for filtered queries; and when Postgres is enough.
resource: https://github.com/pgvector/pgvector
tags: [pgvector, overview, hnsw, ivfflat]
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

# pgvector — Overview

| Feature | Detail |
|---|---|
| Types | `vector` (up to 16k dims stored, 2k indexed), `halfvec` (half precision, up to 4k indexed), `bit` (binary), `sparsevec` |
| Distance operators | `<->` L2, `<#>` negative inner product, `<=>` cosine, `<+>` L1, `<~>` Hamming, `<%>` Jaccard |
| Indexes | **HNSW** (better recall/speed, slower build) and **IVFFlat** (faster build, needs data first) |
| Filtering | `WHERE` clauses with iterative index scans (0.8+) so filtered queries still return enough rows |
| Exact search | Sequential scan when no index — perfect recall for small tables |

## When Postgres is enough

Up to tens of millions of vectors with moderate QPS, pgvector (often with `halfvec` or binary quantization) performs well and removes a separate system. Dedicated engines like [Qdrant](../qdrant/index.md) win on very large scale, advanced hybrid queries and multivectors. Full-text search in Postgres (`tsvector`) combines with pgvector for [hybrid search](../../concepts/rag.md).

## Related

[pgvector index](index.md) · [Snippets](snippets.md)
