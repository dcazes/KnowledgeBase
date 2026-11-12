---
type: Concept
title: Qdrant Overview
description: Qdrant's data model and search features — collections, points and payloads, named vectors, HNSW with filterable payload indexes, sparse vectors for keyword-style search, multivectors for ColBERT-style late interaction, hybrid queries with RRF, quantization and sharding.
resource: https://qdrant.tech/documentation/concepts/
tags: [qdrant, overview, hnsw, sparse-vectors, quantization]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: qdrant-docs
    resource: "https://qdrant.tech/documentation/"
    title: "Qdrant documentation"
    author: "site:qdrant.tech"
---

# Qdrant — Overview

| Concept | Meaning |
|---|---|
| Collection | Named set of points with a vector configuration (size, distance: cosine, dot, Euclid, Manhattan) |
| Point | id + one or more vectors + JSON payload |
| Named vectors | Several vector spaces per point (e.g. text and image) |
| Payload index | Indexes on payload fields so filters stay fast inside HNSW traversal |
| Sparse vectors | BM25/SPLADE-style lexical signals for [hybrid search](../../concepts/rag.md) |
| Multivectors | Late-interaction models such as ColBERT and ColPali |
| Query API | Prefetch + fusion (RRF, DBSF), re-scoring and grouping in one request |
| Quantization | Scalar, product and binary quantization to cut memory 4–32× |
| Distributed | Sharding and replication; Qdrant Cloud managed option |

Filtering during graph traversal (rather than before or after) is Qdrant's signature design — it keeps filtered queries accurate and fast.

## Related

[Qdrant index](index.md) · [Vector databases](../../concepts/vector-databases.md)
