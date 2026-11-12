---
type: Reference
title: Qdrant Snippets
description: Qdrant Python snippets — create a collection, upsert points with payloads, filtered search, and a hybrid dense + sparse query with RRF fusion.
resource: https://qdrant.tech/documentation/
tags: [qdrant, snippets, python, cheat-sheet]
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

# Qdrant — Snippets

```python
from qdrant_client import QdrantClient, models

c = QdrantClient("http://localhost:6333", api_key="change-me")
c.create_collection("docs",
    vectors_config={"dense": models.VectorParams(size=768, distance=models.Distance.COSINE)},
    sparse_vectors_config={"sparse": models.SparseVectorParams()})
c.create_payload_index("docs", "lang", models.PayloadSchemaType.KEYWORD)

c.upsert("docs", points=[models.PointStruct(id=1, vector={"dense": emb}, payload={"lang": "en", "text": "..."})])

hits = c.query_points("docs", query=q_emb, using="dense", limit=5,
    query_filter=models.Filter(must=[models.FieldCondition(key="lang", match=models.MatchValue(value="en"))]))

hybrid = c.query_points("docs",
    prefetch=[models.Prefetch(query=q_emb, using="dense", limit=20),
              models.Prefetch(query=models.SparseVector(indices=idx, values=vals), using="sparse", limit=20)],
    query=models.FusionQuery(fusion=models.Fusion.RRF), limit=5)
```

`emb`, `q_emb`, `idx`, `vals` come from your [embedding](../../concepts/embeddings.md) models.

## Related

[Qdrant index](index.md) · [Overview](overview.md)
