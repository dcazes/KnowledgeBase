---
type: Concept
title: Cognee Overview
description: How Cognee works — ECL pipeline (Extract, Cognify, Load), knowledge graph + semantic layers, retrieval/query modes, storage backends.
resource: https://docs.cognee.ai
tags: [cognee, overview, ecl, knowledge-graph]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: cognee-docs
    resource: "https://docs.cognee.ai"
    title: "Cognee docs"
    author: "site:docs.cognee.ai"
  - id: cognee-github
    resource: "https://github.com/topoteretes/cognee"
    title: "Cognee GitHub"
    author: "site:github.com"
---

# Overview

Cognee turns raw unstructured data into **grounded, queryable AI memory**: rather than vectorizing documents and hoping, it extracts a knowledge graph with semantic layers so queries can traverse relationships, not just match text.

## ECL pipeline

1. **Extract** — pull content from sources (files, PDFs, URLs, code, S3, search) and split into data points.
2. **Cognify** — LLM-based semantic processing: entity/relation extraction, concept mapping, graph construction with a knowledge ontology.
3. **Load** — persist the graph + vectors into configured backends (Postgres for relations, vector store for embeddings).

## Semantic layers

* **Entities & relations** — nodes/edges extracted from content.
* **Concepts / ontology** — higher-level categories linking entities (concept → entity mapping).
* **Communities** — clustered subgraphs for global/community-level queries.

## Retrieval

* `search(query, query_type=SEARCH_TYPE.SEMANTIC)` — embedding-based search over the graph.
* `search(query, query_type=SEARCH_TYPE.GRAPH_COMPLETION)` — graph-aware completion (traverse relationships + facts).
* Fact/claim retrieval with provenance back to source chunks.

## Storage backends

| Layer | Options |
|---|---|
| Relational (relations) | Postgres (default), SQLite |
| Vector | LanceDB (default), Qdrant, Weaviate, Milvus |
| LLM | OpenAI, Ollama, Anthropic, Azure, local |
| Embeddings | OpenAI, Ollama, HuggingFace |

The local checkout's `docker-compose.yml` wires Postgres + vector DB + the cognee API; `cognee-frontend` provides a UI.
