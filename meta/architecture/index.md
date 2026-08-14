---
type: Reference
title: Architecture
description: Meta-documentation for scaling this knowledge base's search across text, code, and images — search backend (Vespa vs Weaviate), agent memory (Graphiti vs Mem0), and the agentic system blueprint.
resource: https://vespa.ai/
tags: [architecture, search, memory, graph, knowledge-base]
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
  - id: graphiti
    resource: "https://github.com/getzep/graphiti"
    title: "Graphiti"
    author: "site:github.com"
  - id: mem0
    resource: "https://mem0.ai/"
    title: "Mem0"
    author: "site:mem0.ai"
---

# Architecture

Meta-documentation for how to make this knowledge base **searchable at scale** across **text, code, and images**. Rather than lock into one tool, this folder organizes technologies into *sections* of competing approaches, each with a comparison file so you can weigh trade-offs as the KB grows.

## Sections

* [Search Backend](search-backend/index.md) - the retrieval engine under the KB (Vespa vs Weaviate)
* [Memory](memory/memory-comparison.md) - agent memory / temporal knowledge (Graphiti vs Mem0)
* [Agentic System Blueprint](agentic-system-blueprint.md) - one-stop-shop plan for your ideal stack (Hermes-centric)
* [Agent Stack (prototype)](/../../agent-stack/index.md) - all-in-one docker-compose + .env code prototype (flattened to top-level `agent-stack/`)

## Last verified

**2026-08-12** — removed stale program copies (Graphiti/Mem0/MemOS) that duplicated top-level folders; memory comparison repointed to `memory/memory-comparison.md`.

## Design principle

A graph (Graphify/Graphiti) is for **relationships**, not fuzzy search. For a massive, mixed-modality KB, put a proper **search backend** (vector + keyword + filtering) underneath, and keep graphs as an *auxiliary* memory/relationship layer.

```
Ingest (docs / code AST / images)
   │  embed
   ▼
Search backend (Vespa | Weaviate)   ← primary retrieval
   │
   ▼
Optional graph layer (Graphiti memory / Graphify map)
   │
   ▼
Agents (Hermes / OpenCode) query the backend
```

## Scope of this folder

* **Search backend:** Vespa + Weaviate (focus).
* **Memory:** Graphiti vs Mem0.

Other engines (Qdrant, Milvus, pgvector, LanceDB) and parsers (Docling/Marker) are deferred — see each section's comparison for why these two were chosen first.
