---
type: Reference
title: Graphiti
description: Temporal context graphs for AI agents (Zep/Neo4j) — tracks how facts change over time with provenance, episodes, and ontology; agent memory, not a static compiled graph.
resource: https://github.com/getzep/graphiti
tags: [graphiti, memory, graph, agents, neo4j]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: graphiti-github
    resource: "https://github.com/getzep/graphiti"
    title: "Graphiti GitHub"
    author: "site:github.com"
  - id: neo4j-blog-graphiti
    resource: "https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/"
    title: "Neo4j blog — Graphiti"
    author: "site:neo4j.com"
  - id: zep-graphiti
    resource: "https://www.getzep.com/platform/graphiti/"
    title: "Zep — Graphiti"
    author: "site:www.getzep.com"
  - id: paper-arxiv-2501-13956
    resource: "https://arxiv.org/abs/2501.13956"
    title: "Paper (arXiv 2501.13956)"
    author: "site:arxiv.org"
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

## Last verified

**2026-08-12** — Version pinned to **v0.29.3** (PyPI `graphiti-core`, 2026-07); not installed locally (no `programs/graphiti`). Prior content verified 2026-07-15 against upstream repo/docs.
