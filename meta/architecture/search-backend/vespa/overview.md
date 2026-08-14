---
type: Software
title: Vespa — Overview
description: Self-hosted unified serving engine combining vector search, BM25, filtering, and ML ranking at billion-scale in one system.
resource: https://vespa.ai/
tags: [vespa, search, vector-db, hybrid, ranking, scale, self-hosted]
timestamp: 2026-07-09T06:00:00Z
---

# What Vespa is

Vespa is a **unified serving engine** for search and recommendation. Instead of stitching together a vector DB, a keyword index, a filter store, and a reranker, Vespa brings **vector search, keyword (BM25) search, structured filtering, and ML ranking (including on-the-fly model inference) into one distributed engine**. It's designed for **billion-scale** corpora with low latency.

# Why it fits a massive KB

* **One system, many signals** — semantic (vectors), lexical (BM25), metadata filters, and learned ranking all execute in the same query.
* **Scale** — sharded/distributed; proven at very large vector counts.
* **Self-hosted** — runs on your hardware (matches your local-first stack).
* **Ranking control** — tensor math and custom ranking expressions; can run inference at query time.

# How it relates to the architecture

```
Ingest (docs / code AST / images) → embed → Vespa (vector + BM25 + filter + rank)
                                        │
                                        ▼
                          graph layers (Graphiti memory / Graphify map) — auxiliary
                                        │
                                        ▼
                                  Agents (Hermes / OpenCode)
```

Vespa is the **retrieval core**; graphs sit on top for relationships/memory.

# Versus the alternatives

* **Weaviate** — easier start, module-based; Vespa is heavier but more unified at scale.
* **Qdrant/Milvus** — purer vector DBs; Vespa adds BM25 + ranking natively.
* **Graphify/Graphiti** — graphs, not search engines; complementary, not replacements.

# Citations

[1] [Vespa](https://vespa.ai/)
[2] [Vespa vs Weaviate](https://zilliz.com/comparison/vespa-vs-weaviate)
[3] [Architecture overview](/../../index.md)
