---
type: Reference
title: Search Backend
description: The retrieval engine under the knowledge base — compares Vespa (unified vector+BM25+ML ranking at billion-scale) vs Weaviate (hybrid search, modules, easy schema) for scaling text/code/image search.
resource: https://vespa.ai/
tags: [search, vector-db, hybrid-search, architecture]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: vespa
    resource: "https://vespa.ai/"
    title: "Vespa"
    author: "site:vespa.ai"
  - id: weaviate
    resource: "https://weaviate.io/"
    title: "Weaviate"
    author: "site:weaviate.io"
---

# Search Backend

The **retrieval engine** underneath the knowledge base — the system that actually answers "find me the chunk about X" across text, code, and images at scale. This section compares competing engines so you can pick (or swap) as the KB grows.

## Competing technologies

* [Vespa](vespa/index.md) - unified vector + BM25 + filtering + ML ranking at billion-scale in one engine
* [Weaviate](weaviate/index.md) - hybrid search, multi-vector, code/image modules, easy schema

## Comparison

See [search-backend comparison](vespa-vs-weaviate.md) for the head-to-head (when to pick which, scale, modality, ops cost).

## Why a search backend (not just a graph)

Graphs (Graphify/Graphiti) model *relationships*; they don't do fuzzy/semantic/keyword recall over millions of chunks. The search backend is the **primary retrieval** layer; graphs are auxiliary.

## Scope

This section focuses on **Vespa** and **Weaviate** (both self-hostable, both hybrid + multimodal-capable). Qdrant/Milvus/pgvector/LanceDB are deferred.
