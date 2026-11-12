---
type: Software
title: Graphiti
description: Open-source Python framework from Zep for building and querying temporal context graphs — bi-temporal facts with validity windows, episode provenance, custom ontologies and hybrid retrieval.
resource: https://github.com/getzep/graphiti
tags: [graphiti, zep, knowledge-graph, temporal, agent-memory, graphrag, python]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphiti-github
    resource: "https://github.com/getzep/graphiti"
    title: "getzep/graphiti on GitHub"
    author: "site:github.com"
  - id: graphiti-docs
    resource: "https://help.getzep.com/graphiti"
    title: "Graphiti documentation"
    author: "site:help.getzep.com"
  - id: zep-paper
    resource: "https://arxiv.org/abs/2501.13956"
    title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
    author: "Rasmussen et al., arXiv 2501.13956"
---

# Graphiti

**Graphiti** builds a *temporal context graph* from a stream of data: entities become nodes, facts become edges with a validity window (when they became true, when they were superseded), and every fact traces back to the raw **episode** it came from. Agents query it with hybrid search over meaning, keywords and graph structure. It is the open-source graph engine inside [Zep](../zep/index.md).

| | |
|---|---|
| Category | [Knowledge graphs](../../concepts/knowledge-graphs.md) · [Agent memory](../../concepts/agent-memory.md) |
| License | Apache-2.0 |
| Language | Python 3.10+ (`graphiti-core`) |
| Latest release | v0.31.2 (2026-10-20) |
| Graph backends | [Neo4j](../../databases/neo4j/index.md) 5.26, [FalkorDB](../../databases/falkordb/index.md), Amazon Neptune; Kuzu (deprecated) |

## Contents

* [Overview](overview.md) — what a context graph is, why temporal, Graphiti vs GraphRAG
* [Concepts](concepts.md) — episodes, entities, facts, sagas, communities, ontology
* [Backends](backends.md) — Neo4j, FalkorDB, Neptune, Kuzu deprecation
* [Installation](installation.md) — `graphiti-core` and extras, Docker Compose
* [MCP server](mcp-server.md) — reference MCP server and its tools
* [Snippets](snippets.md) — add episodes, search facts and nodes, local LLMs
* [AI Integration](ai-integration.md) — using Graphiti as agent memory
* [Graphiti vs Graphify](vs-graphify.md) — two different "graph from data" tools

## Related

* Concepts: [Knowledge graphs](../../concepts/knowledge-graphs.md) · [GraphRAG](../../concepts/graphrag.md) · [Agent memory](../../concepts/agent-memory.md) · [MCP](../../concepts/mcp.md)
* Peers: [Zep](../zep/index.md) (managed product built on Graphiti), [Microsoft GraphRAG](../graphrag/index.md), [LightRAG](../lightrag/index.md), [Cognee](../cognee/index.md), [Mem0](../mem0/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
