---
type: Concept
title: Graphiti Overview
description: What Graphiti's temporal context graphs are, the problems they solve compared with chunk-based RAG, and how Graphiti differs from Microsoft GraphRAG and from Zep.
resource: https://github.com/getzep/graphiti
tags: [graphiti, overview, temporal, graphrag, knowledge-graph]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphiti-github
    resource: "https://github.com/getzep/graphiti"
    title: "getzep/graphiti on GitHub"
    author: "site:github.com"
  - id: zep-paper
    resource: "https://arxiv.org/abs/2501.13956"
    title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
    author: "Rasmussen et al., arXiv 2501.13956"
---

# Graphiti — Overview

Classic [RAG](../../concepts/rag.md) retrieves document chunks; it has no notion that a fact can stop being true. Graphiti targets agents that work on **changing** data — conversations, tickets, CRM records — where "what is true now" and "what was true in March" are different questions.

## What a context graph holds

| Component | Stores |
|---|---|
| Entities (nodes) | People, products, policies, concepts — with summaries that evolve |
| Facts (edges) | Entity → relationship → entity triplets, each with a validity window |
| Episodes | The raw data as ingested; every derived fact links back here (provenance) |
| Custom types | Entity and edge types you define as [Pydantic](../../tools/pydantic/index.md) models |

See [Concepts](concepts.md) for details.

## Key properties

* **Bi-temporal facts.** Each edge records when it was true in the world and when the system learned it. New contradicting information *invalidates* old facts instead of deleting them, so history stays queryable.
* **Incremental construction.** Episodes are integrated as they arrive; there is no batch re-index of the whole corpus.
* **Hybrid retrieval.** Semantic embeddings + BM25 keyword search + graph traversal, with rerankers such as reciprocal rank fusion or graph-distance from a centre node. Queries do not need an LLM summarisation step, so latency is typically sub-second.
* **Prescribed or learned ontology.** Define types up front, or let structure emerge and add types later.

## Graphiti vs Microsoft GraphRAG

| | [GraphRAG](../graphrag/index.md) | Graphiti |
|---|---|---|
| Primary use | Summarising a static document corpus | Evolving, temporal knowledge |
| Updates | Batch indexing | Continuous, incremental |
| Structure | Entity clusters + community summaries | Entities, temporal facts, episodes, communities |
| Retrieval | LLM summarisation over communities | Hybrid search, no LLM at query time |
| Contradictions | Resolved in summaries | Automatic fact invalidation with history |

Both are forms of [GraphRAG](../../concepts/graphrag.md) in the broad sense; they suit different data.

## Graphiti vs Zep

Graphiti is a **framework**: you bring the graph database, LLM and embedder, and you build ingestion, tenancy and access control. [Zep](../zep/index.md) is the managed context platform built on Graphiti, with its own graph store, users/threads, dashboards and SLAs. The architecture is described in the Zep paper (arXiv 2501.13956).

## Caveats

* Ingestion makes several LLM calls per episode and works best with models that support [structured output](../../concepts/structured-output.md). Small local models can produce malformed extractions.
* `SEMAPHORE_LIMIT` (default 10) caps concurrency to avoid provider 429s; raise it for faster ingestion if your provider allows.

## Related

[Graphiti index](index.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md) · [GraphRAG](../../concepts/graphrag.md) · [Memory alternatives](../alternatives.md)
