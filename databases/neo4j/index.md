---
type: Software
title: Neo4j
description: The most widely used graph database — labelled property graphs queried with Cypher (and GQL), native vector and full-text indexes, graph data science, and GenAI integrations; the main backend for Graphiti, a supported store for Cognee and LightRAG, and the reference for GraphRAG.
resource: https://neo4j.com
tags: [neo4j, graph-database, cypher, knowledge-graph, graphrag, java]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: neo4j-site
    resource: "https://neo4j.com"
    title: "Neo4j"
    author: "site:neo4j.com"
  - id: neo4j-docs
    resource: "https://neo4j.com/docs/"
    title: "Neo4j documentation"
    author: "site:neo4j.com"
  - id: neo4j-github
    resource: "https://github.com/neo4j/neo4j"
    title: "neo4j/neo4j on GitHub"
    author: "site:github.com"
  - id: mcp-neo4j
    resource: "https://github.com/neo4j-contrib/mcp-neo4j"
    title: "Neo4j MCP servers"
    author: "site:github.com"
---

# Neo4j

**Neo4j** stores data as nodes and relationships with properties and queries them with **Cypher**. Because a knowledge graph *is* a property graph, Neo4j became the default home for [GraphRAG](../../concepts/graphrag.md) and graph-based [agent memory](../../concepts/agent-memory.md): [Graphiti](../../memory/graphiti/index.md) builds on it, and its vector indexes let one database do both graph traversal and semantic search.

| | |
|---|---|
| Category | [Knowledge graphs](../../concepts/knowledge-graphs.md) · graph database |
| License | Community Edition GPL-3.0; Enterprise and AuraDB commercial |
| Language | Java |
| Latest | 2026.10.x (calendar versioning); Python driver `neo4j` 6.4 |
| Ports | 7474 (Browser/HTTP), 7687 (Bolt) |

## Contents

* [Overview](overview.md) — property graphs, Cypher, indexes, GDS
* [Installation](installation.md) — Docker, Desktop, Aura
* [Snippets](snippets.md) — Cypher and Python driver
* [AI Integration](ai-integration.md) — GraphRAG, vector search, MCP, memory tools

## Related

* Concepts: [Knowledge graphs](../../concepts/knowledge-graphs.md) · [GraphRAG](../../concepts/graphrag.md) · [Vector databases](../../concepts/vector-databases.md)
* Peers: [FalkorDB](../falkordb/index.md); used by [Graphiti](../../memory/graphiti/index.md), [Cognee](../../memory/cognee/index.md), [LightRAG](../../memory/lightrag/index.md), [MemOS](../../memory/memos/index.md), [Graphify](../../memory/graphify/installation.md)
* Comparison: [Databases alternatives](../alternatives.md)
