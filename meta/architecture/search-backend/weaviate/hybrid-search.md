---
type: Reference
title: Weaviate — Hybrid Search
description: Weaviate's combination of dense vector, sparse/BM25 keyword, and reranker modules in a single query.
resource: https://weaviate.io/developers/weaviate/search/hybrid
tags: [weaviate, hybrid-search, dense, sparse, bm25, reranker, modules]
timestamp: 2026-07-09T06:05:00Z
---

# Hybrid retrieval in Weaviate

Weaviate supports **hybrid search** natively: it blends a **dense** (vector) and a **sparse/BM25** (keyword) score, then can apply a **reranker module**.

```python
# conceptual
results = collection.query.hybrid(
    query="how does Vespa rank at scale",
    alpha=0.5,                 # 0=sparse, 1=dense
    rerank="reranker-cohere"   # optional module
)
```

# Why hybrid matters here

* **Text** — vectors catch meaning; BM25 catches exact terms.
* **Code** — BM25 strong on identifiers; vectors catch intent. Combine.
* **Images** — vector is primary; metadata filters scope.

# Rerankers

`reranker-*` modules (Cohere, etc.) improve precision post-retrieval. If strict local, prefer a local reranker or skip and rely on hybrid alpha tuning.

# Citations

[1] [Hybrid search docs](https://weaviate.io/developers/weaviate/search/hybrid)
[2] [Weaviate modules](https://weaviate.io/developers/weaviate/modules)
[3] [Search comparison](/../../search-backend/vespa-vs-weaviate.md)
