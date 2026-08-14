---
type: Reference
title: Graphiti vs Graphify
description: Explicit distinction between Graphiti (temporal context-graph agent memory, Neo4j) and Graphify (static confidence-tagged compiled graph) — both in this KB.
resource: https://github.com/getzep/graphiti
tags: [graphiti, graphify, comparison, temporal, static, knowledge-graph, distinction]
timestamp: 2026-07-09T05:05:00Z
---

# Two different "graph from data" tools

This KB covers **both** Graphiti and Graphify. They sound alike but solve different problems.

| Aspect | **Graphiti** | **Graphify** |
|--------|--------------|--------------|
| Purpose | **Temporal agent memory** | Static, compiled knowledge graph |
| Source | Live streams / interactions / docs | A folder of files |
| Temporal | ✅ validity windows, point-in-time queries | ❌ snapshot in time |
| Provenance | ✅ **Episodes** (raw source preserved) | partial (source files) |
| Confidence tags | ❌ | ✅ EXTRACTED / INFERRED / AMBIGUOUS |
| Backend | Neo4j / FalkorDB / Neptune / Kuzu | file/GraphML (MCP serve) |
| Client | Python `graphiti_core` | Hermes client (`graphify install --platform hermes`) |
| MCP | ✅ MCP server (Docker) | ✅ `python -m graphify.serve` |
| Update model | Incremental / real-time | Recompile the graph |
| Author | Zep / Neo4j | Graphify-Labs |

# When to use which

* **Graphiti** — you need memory that *changes over time* and you can query "what was true then." Best for agents operating on evolving data. Needs a graph DB (Neo4j).
* **Graphify** — you want a one-shot, confidence-tagged graph of a codebase/folder you can query or serve over MCP. Lighter; no DB required.

# They can coexist

Use **Graphify** to compile a static map of `programs/*` for quick lookup, and **Graphiti** to hold the *evolving* memory of agent interactions. Different layers, same "graph" idea.

# Citations

[1] [Graphiti](https://github.com/getzep/graphiti)
[2] [Graphify](/../../graphify/index.md)
[3] [Graphiti concepts](concepts.md)
