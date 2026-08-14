---
type: Reference
title: Vespa
description: Unified serving engine combining vector search, BM25, structured filtering, and ML ranking in one self-hosted system at billion-scale — the candidate primary search backend for the multi-modal KB.
resource: https://vespa.ai/
tags: [vespa, vector-db, hybrid-search, search, ranking]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: vespa
    resource: "https://vespa.ai/"
    title: "Vespa"
    author: "site:vespa.ai"
  - id: vespa-vector-database
    resource: "https://vespa.ai/vector-database/"
    title: "Vespa vector database"
    author: "site:vespa.ai"
  - id: search-backend-comparison
    resource: "/../../search-backend/vespa-vs-weaviate.md"
    title: "Search backend comparison"
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
