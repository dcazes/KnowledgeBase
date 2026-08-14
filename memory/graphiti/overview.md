---
type: Software
title: Graphiti — Overview
description: Open-source framework (Zep/Neo4j) for building and querying temporal context graphs for AI agent memory — facts with validity windows, episode provenance, incremental updates.
resource: https://github.com/getzep/graphiti
tags: [graphiti, knowledge-graph, temporal, agent-memory, neo4j, zep, context-graph]
generated: { by: "human:daniel", at: "2026-07-09T05:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T05:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: graphiti-github
    resource: "https://github.com/getzep/graphiti"
    title: "Graphiti GitHub"
    author: "site:github.com"
  - id: neo4j-graphiti
    resource: "https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/"
    title: "Neo4j — Graphiti"
    author: "site:neo4j.com"
  - id: graphiti-vs-graphrag-readme
    resource: "https://github.com/getzep/graphiti#graphiti-vs-graphrag"
    title: "Graphiti vs GraphRAG (README)"
    author: "site:github.com"
  - id: paper-arxiv-2501-13956
    resource: "https://arxiv.org/abs/2501.13956"
    title: "Paper (arXiv 2501.13956)"
    author: "site:arxiv.org"
---

# What Graphiti is

Graphiti is a framework for building and querying **temporal context graphs** for AI agents. Unlike static knowledge graphs, its context graphs track **how facts change over time**, maintain **provenance** to source data, and support both prescribed and learned ontologies — purpose-built for agents on evolving, real-world data.

Per the official README: *"Unlike static knowledge graphs, Graphiti's context graphs track how facts change over time… making them purpose-built for agents operating on evolving, real-world data."*

# Why it matters

* **Temporal fact management** — facts have validity windows; when info changes, old facts are *invalidated, not deleted*. Query what's true now or what was true at any time.
* **Episodes & provenance** — every entity/relationship traces back to the **episode** (raw data) that produced it. Full lineage.
* **Incremental construction** — new data integrates immediately; no batch recomputation. Real-time as agents interact.
* **Hybrid retrieval** — semantic embeddings + keyword (BM25) + graph traversal, typically **sub-second**, with **no LLM-in-the-loop reranking**.
* **Custom ontology** — define entity/edge types via Pydantic models, or let structure emerge (learned), or mix both.

# Graphiti vs GraphRAG (key contrast)

| | GraphRAG | Graphiti |
|--|----------|----------|
| Data | Batch/static | Continuous/incremental |
| Time | Basic timestamps | Bi-temporal, auto-invalidation |
| Queries | LLM summarization | Hybrid search, sub-second |
| Custom types | No | Yes (Pydantic) |

# How it differs from Graphify (in this KB)

Graphify (see `/../../graphify/index.md`) compiles a **static, confidence-tagged** graph from a folder (EXTRACTED/INFERRED/AMBIGUOUS tags, Hermes client, MCP serve). Graphiti is a **live temporal memory engine** with episode provenance and validity windows, backed by Neo4j/FalkorDB. Different tools, similar "graph from data" goal. See [Graphiti vs Graphify](vs-graphify.md).

# How it fits your stack

| Layer | Tool |
|-------|------|
| Static compiled graph | Graphify |
| Temporal agent memory | **Graphiti** |
| Agent runtime | Hermes / OpenCode |
| Chat/RAG | OpenWebUI / AnythingLLM |

Graphiti can serve as the **memory** substrate for your agents; its MCP server exposes that memory to Claude/Cursor/your stack.
