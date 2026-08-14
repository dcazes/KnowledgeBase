---
type: Reference
title: Graphiti — Concepts (Context Graph)
description: Graphiti's data model — entities, facts/relationships with temporal validity windows, episodes (provenance), and custom Pydantic ontology.
resource: https://github.com/getzep/graphiti#what-is-a-context-graph
tags: [graphiti, context-graph, entities, episodes, ontology, temporal, validity-window]
generated: { by: "human:daniel", at: "2026-07-09T05:02:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T05:02:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: what-is-a-context-graph-readme
    resource: "https://github.com/getzep/graphiti#what-is-a-context-graph"
    title: "What is a Context Graph (README)"
    author: "site:github.com"
  - id: neo4j-graphiti
    resource: "https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/"
    title: "Neo4j — Graphiti"
    author: "site:neo4j.com"
  - id: zep-graphiti
    resource: "https://www.getzep.com/platform/graphiti/"
    title: "Zep — Graphiti"
    author: "site:www.getzep.com"
---

# Graphiti — The context graph

A **context graph** is a temporal graph of entities, relationships, and facts — e.g. *"Kendra loves Adidas shoes (as of March 2026)."* Each fact has a **validity window**: when it became true, and when (if ever) it was superseded. Entities evolve over time with updated summaries. Everything traces back to **episodes** — the raw data that produced it.

# Components

| Component | What it stores |
|-----------|----------------|
| **Entities** (nodes) | People, products, policies, concepts — with summaries that evolve over time |
| **Facts / Relationships** (edges) | Triplets (Entity → Relationship → Entity) with **temporal validity windows** |
| **Episodes** (provenance) | Raw data as ingested — the ground-truth stream; every derived fact links back |
| **Custom Types** (ontology) | Developer-defined entity/edge types via **Pydantic** models |

# Temporality

* Every edge carries timestamps: when a fact became valid, when it stopped, when Graphiti learned it, when it learned it was no longer true.
* **Point-in-time queries** follow from the data model: "what was true on date X?"
* When new info contradicts an old fact, the old fact is **invalidated** (preserved as history) and removed from *current* state — not deleted.

# Ontology options

* **Prescribed** — define entity/edge types upfront via Pydantic.
* **Learned** — let structure emerge from data.
* **Hybrid** — custom ontology + Freeform for anything that doesn't fit; or restrict to only your ontology.

# Why episodes matter

Episodes keep the original text. Graphiti can return relevant episodes in search (BM25) and provides helpers to get the **source episode text** for any node/edge — enabling citations/quotations.
