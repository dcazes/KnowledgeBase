---
type: Reference
title: Cognee
description: Memory-engineering layer for AI — ECL pipeline (Extract/Cognify/Load) turning unstructured data into queryable knowledge graphs with semantic layers; Python library + API + frontend.
resource: https://github.com/topoteretes/cognee
tags: [cognee, memory, knowledge-graph, rag, pipeline]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: cognee-github
    resource: "https://github.com/topoteretes/cognee"
    title: "Cognee GitHub"
    author: "site:github.com"
  - id: cognee-docs
    resource: "https://docs.cognee.ai"
    title: "Cognee docs"
    author: "site:docs.cognee.ai"
  - id: cognee-on-pypi
    resource: "https://pypi.org/project/cognee/"
    title: "Cognee on PyPI"
    author: "site:pypi.org"
---

# Cognee

A **memory-engineering layer for AI** — ingests unstructured data (PDFs, docs, web, code) and runs the **ECL pipeline** (Extract → Cognify → Load) to build queryable knowledge graphs with semantic layers (concepts, entities, relations, communities). Sits between raw data and LLM agents, giving grounded, graph-aware memory.

Local checkout: `programs/cognee` (git, topoteretes, main, commit 2026-07-17) at **v1.4.0**; latest on PyPI is **v1.4.2** (`pip install cognee`). The checkout includes `docker-compose.yml` (API + Postgres + graph/vector backends) and a `cognee-frontend` — **not deployed** as of 2026-08-13 (no running containers).

## Contents

* [Overview](overview.md) — ECL pipeline, knowledge graph + semantic layers, retrieval modes
* [Installation](installation.md) — `pip install cognee` or Docker compose (+ frontend); verify
* [Configuration](configuration.md) — LLM/embedding providers, graph/vector/relational backends, data dir
* [AI Integration](ai-integration.md) — Python API (`add/cognify/search`), REST server, agent wiring, vs LightRAG/Graphiti
* [Snippets](snippets.md) — add data / cognify / search / prune cheat sheet
* [Alternatives](alternatives.md) — LightRAG, GraphRAG, Graphiti, Mem0 vs Cognee

## Related

* [LightRAG](../lightrag/index.md) — graph RAG; Cognee = full memory pipeline (extract→cognify→load)
* [Graphiti](../graphiti/index.md) — temporal agent memory; Cognee = corpus knowledge engineering
* [Mem0](../mem0/index.md) / [MemOS](../memos/index.md) — user memory vs corpus knowledge

## Last verified

**2026-08-13** — Local checkout `programs/cognee` v1.4.0 (PyPI latest v1.4.2); compose + frontend present; not deployed. Grounded on local checkout (recon 2026-08-12) + upstream docs.
