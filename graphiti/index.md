---
type: Reference
title: Graphiti
description: Temporal context graphs for AI agents (Zep/Neo4j) — tracks how facts change over time with provenance, episodes, and ontology; agent memory, not a static compiled graph.
resource: https://github.com/getzep/graphiti
tags: [graphiti, memory, graph, agents, neo4j]
timestamp: 2026-08-12T00:00:00Z
---

# Graphiti

A framework for building and querying **temporal context graphs** for AI agents — by Zep/Neo4j. Unlike static knowledge graphs, Graphiti tracks **how facts change over time**, keeps **provenance** (every fact traces to a raw *episode*), and supports both prescribed and learned ontologies. It's agent **memory**, not a one-shot compiled graph. Distinct from **Graphify** (a static, confidence-tagged graph compiled from a folder) — see [Graphiti vs Graphify](vs-graphify.md).

## Contents

* [Overview](overview.md) - what Graphiti is, why temporal
* [Installation](installation.md) - `pip install graphiti-core` (v0.29.3), Neo4j, env
* [Concepts](concepts.md) - context graph: entities, edges, episodes, ontology, validity windows
* [Backends](backends.md) - Neo4j, FalkorDB, Neptune, Kuzu
* [MCP Server](mcp-server.md) - MCP server (Docker) for Claude/Cursor
* [Graphiti vs Graphify](vs-graphify.md) - explicit distinction
* [AI Integration](ai-integration.md) - agent memory, your stack, :4000 proxy
* [Alternatives](alternatives.md) - GraphRAG, Zep, Graphify, Mem0
* [Snippets](snippets.md) - cheat sheet

## Instance facts (this machine)

* **Not installed** — no `programs/graphiti` launcher found; document from upstream. PyPI `graphiti-core` **v0.29.3** (2026-07).
* **Role here (intended):** temporal agent memory backend; could back Hermes/OpenCode memory; MCP server for agents.
* **Backends available:** Neo4j (would need a container); Graphiti itself is Python (`graphiti-core`).

# Citations

[1] [Graphiti GitHub](https://github.com/getzep/graphiti)
[2] [Neo4j blog — Graphiti](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/)
[3] [Zep — Graphiti](https://www.getzep.com/platform/graphiti/)
[4] [Paper (arXiv 2501.13956)](https://arxiv.org/abs/2501.13956)

## Last verified

**2026-08-12** — Version pinned to **v0.29.3** (PyPI `graphiti-core`, 2026-07); not installed locally (no `programs/graphiti`). Prior content verified 2026-07-15 against upstream repo/docs.
