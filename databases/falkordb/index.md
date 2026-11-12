---
type: Software
title: FalkorDB
description: Low-latency property graph database built on sparse adjacency matrices and GraphBLAS linear algebra, speaking openCypher over the Redis protocol, with vector indexes, multi-tenant graphs and a browser UI — aimed at GraphRAG and agent memory.
resource: https://www.falkordb.com
tags: [falkordb, graph-database, graphblas, cypher, graphrag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: falkordb-github
    resource: "https://github.com/FalkorDB/FalkorDB"
    title: "FalkorDB/FalkorDB on GitHub"
    author: "site:github.com"
  - id: falkordb-docs
    resource: "https://docs.falkordb.com"
    title: "FalkorDB documentation"
    author: "site:docs.falkordb.com"
---

# FalkorDB

**FalkorDB** (successor to RedisGraph) represents graphs as sparse matrices and executes queries with linear algebra via GraphBLAS, giving very low query latency. It speaks openCypher, runs as a single container with a browser UI, and is the default graph store of the [Graphiti MCP server](../../memory/graphiti/mcp-server.md).

| | |
|---|---|
| Category | [Knowledge graphs](../../concepts/knowledge-graphs.md) · graph database |
| License | Server Side Public License (SSPLv1) |
| Language | C/Rust core on the Redis module API |
| Latest release | v6.0.4 (2026-11-05); Python client `falkordb` 1.8 |
| Ports | 6379 (Redis protocol), 3000 (Browser) |

## Contents

* [Overview](overview.md) — matrix representation, multi-graph, vectors
* [Installation](installation.md) — Docker, FalkorDBLite
* [Snippets](snippets.md) — Python client and Cypher
* [AI Integration](ai-integration.md) — Graphiti, Mem0 history, GraphRAG SDK

## Related

* Concepts: [Knowledge graphs](../../concepts/knowledge-graphs.md) · [GraphRAG](../../concepts/graphrag.md)
* Peers: [Neo4j](../neo4j/index.md); used by [Graphiti](../../memory/graphiti/backends.md), [Cognee](../../memory/cognee/configuration.md)
* Comparison: [Databases alternatives](../alternatives.md)
