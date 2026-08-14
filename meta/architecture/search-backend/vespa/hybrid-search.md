---
type: Reference
title: Vespa — Hybrid Search
description: Vespa's combination of dense vector search, BM25 keyword search, structured filtering, and ML ranking in a single query.
resource: https://docs.vespa.ai/
tags: [vespa, hybrid-search, vector, bm25, filtering, ranking, tensor]
timestamp: 2026-07-09T06:01:00Z
---

# Hybrid retrieval in Vespa

Vespa executes **multiple retrieval signals in one ranked query**:

1. **Dense vector search** — nearest-neighbor over embedding fields (text/code/image vectors).
2. **BM25 / lexical** — classic keyword matching over text fields (great for exact terms, code identifiers).
3. **Structured filtering** — `where` clauses on metadata (doc type, date, program, tags).
4. **ML ranking** — ranking expressions / tensor math; can run an inference model at query time to rerank.

# Why hybrid matters for this KB

* **Text docs** — lexical BM25 catches exact terms; vectors catch semantic meaning.
* **Code** — BM25 is strong on symbol/identifier names; vectors catch intent. Combine both.
* **Images** — vector (ColPali/VLM) is the primary signal; metadata filters scope results.

# Example shape (conceptual)

```
query: "how does Vespa rank at scale"
  ├─ nn(vector_field, query_embedding)        # semantic
  ├─ bm25(content) ~ "rank" "scale"            # lexical
  ├─ filter: doc_type = architecture           # structured
  └─ rank: ML model over [vector_score, bm25]  # learned ranking
```

# Citations

[1] [Vespa docs — hybrid](https://docs.vespa.ai/documentation/ranking.html)
[2] [Vespa vector database](https://vespa.ai/vector-database/)
[3] [Hybrid search overview](/../../search-backend/vespa-vs-weaviate.md)
