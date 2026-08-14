---
type: Reference
title: Vespa
description: Unified serving engine combining vector search, BM25, structured filtering, and ML ranking in one self-hosted system at billion-scale — the candidate primary search backend for the multi-modal KB.
resource: https://vespa.ai/
tags: [vespa, vector-db, hybrid-search, search, ranking]
timestamp: 2026-08-12T00:00:00Z
---

# Vespa

A **unified serving engine** that combines vector search, BM25/keyword search, structured filtering, and machine-learning ranking (even on-the-fly inference) in a **single self-hosted system** — built for billion-scale. For this KB it's the candidate **primary search backend** under the graph layers.

## Contents

* [Overview](overview.md) - what Vespa is, unified model
* [Hybrid Search](hybrid-search.md) - vector + BM25 + filtering + ranking
* [Scale & Multimodal](scale-multimodal.md) - billion-scale, text/code/image vectors
* [AI Integration](ai-integration.md) - feeding the KB, agents, graph layers

## Instance facts (this machine)

* **Not installed** — candidate architecture only; document from upstream.
* **Role here:** primary retrieval engine for the massive multi-modal KB (text + code + images).
* **Constraint:** must self-host (your stack is local-first).

# Citations

[1] [Vespa](https://vespa.ai/)
[2] [Vespa vector database](https://vespa.ai/vector-database/)
[3] [Search backend comparison](/../../search-backend/vespa-vs-weaviate.md)
