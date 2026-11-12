---
type: Playbook
title: Neo4j AI Integration
description: Neo4j in AI systems — backend for Graphiti, Cognee, LightRAG and MemOS, the neo4j-graphrag Python package, text-to-Cypher, vector plus graph retrieval, Neo4j MCP servers for agents, and loading Microsoft GraphRAG output.
resource: https://neo4j.com/docs/
tags: [neo4j, integration, graphrag, mcp, text2cypher]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: neo4j-docs
    resource: "https://neo4j.com/docs/"
    title: "Neo4j documentation"
    author: "site:neo4j.com"
  - id: mcp-neo4j
    resource: "https://github.com/neo4j-contrib/mcp-neo4j"
    title: "Neo4j MCP servers"
    author: "site:github.com"
---

# Neo4j — AI Integration

| Use | How |
|---|---|
| Temporal agent memory | [Graphiti](../../memory/graphiti/index.md) on Neo4j |
| Graph store for memory/RAG tools | [Cognee](../../memory/cognee/configuration.md), [LightRAG](../../memory/lightrag/configuration.md), [MemOS](../../memory/memos/configuration.md) |
| GraphRAG library | `neo4j-graphrag` (Python): KG construction from text, vector + graph retrievers, text-to-Cypher |
| Explore other graphs | Load [Microsoft GraphRAG](../../memory/graphrag/ai-integration.md) Parquet output or push [Graphify](../../memory/graphify/installation.md) graphs |
| Agents | Neo4j MCP servers (Cypher, memory, data modelling) for [Claude Code](../../agents/claude-code/index.md) and other [MCP](../../concepts/mcp.md) clients |

**Text-to-Cypher** lets an LLM answer structured questions; constrain it with a schema in the prompt and read-only credentials ([Agent security](../../concepts/agent-security.md)).

## Related

[Neo4j index](index.md) · [GraphRAG](../../concepts/graphrag.md)
