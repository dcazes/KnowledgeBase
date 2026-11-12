---
type: Playbook
title: FalkorDB AI Integration
description: FalkorDB in AI stacks — default backend of the Graphiti MCP server, supported by Graphiti, Cognee and others, the FalkorDB GraphRAG SDK, and per-user graphs for agent memory.
resource: https://docs.falkordb.com
tags: [falkordb, integration, graphiti, graphrag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: falkordb-docs
    resource: "https://docs.falkordb.com"
    title: "FalkorDB documentation"
    author: "site:docs.falkordb.com"
---

# FalkorDB — AI Integration

* **[Graphiti](../../memory/graphiti/backends.md):** `graphiti-core[falkordb]`; default store for the [Graphiti MCP server](../../memory/graphiti/mcp-server.md).
* **[Cognee](../../memory/cognee/configuration.md)** via community adapters.
* **GraphRAG SDK:** FalkorDB's own library for ontology detection, graph construction from documents and question answering — see [GraphRAG](../../concepts/graphrag.md).
* **Agent memory:** one graph per user or agent keeps memories isolated and queries fast.

## Related

[FalkorDB index](index.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md)
