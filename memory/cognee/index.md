---
type: Software
title: Cognee
description: Open-source AI memory platform that turns text, code, conversations and agent sessions into a combined knowledge graph and vector store, with remember / recall / improve / forget operations, plugins for coding agents, MCP and a REST API.
resource: https://github.com/topoteretes/cognee
tags: [cognee, agent-memory, knowledge-graph, graphrag, python, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cognee-github
    resource: "https://github.com/topoteretes/cognee"
    title: "topoteretes/cognee on GitHub"
    author: "site:github.com"
  - id: cognee-docs
    resource: "https://docs.cognee.ai"
    title: "Cognee documentation"
    author: "site:docs.cognee.ai"
  - id: cognee-paper
    resource: "https://arxiv.org/abs/2505.24478"
    title: "Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning"
    author: "Markovic et al., arXiv 2505.24478"
---

# Cognee

**Cognee** builds connected memory for agents and teams: text becomes entities, relationships and searchable chunks; code becomes a graph of symbols and dependencies; agent sessions are distilled into lessons. Retrieval picks graph, vector or code context automatically. It targets both "give my agent memory across runs" and a shared "company brain".

| | |
|---|---|
| Category | [Agent memory](../../concepts/agent-memory.md) · [GraphRAG](../../concepts/graphrag.md) |
| License | Apache-2.0 |
| Language | Python 3.10–3.14 (`cognee`); TypeScript SDK; Rust (`cognee-rs`) |
| Latest release | v1.6.7 (2026-11-06) |
| Deployment | Library · Docker API (port 8000) + UI (3000) + MCP (8001) · Cognee Cloud |

## Contents

* [Overview](overview.md) — the four operations, sessions, graph + vector memory
* [Installation](installation.md) — pip/uv, no-LLM local mode, Docker Compose
* [Configuration](configuration.md) — LLM/embedding providers, storage backends, access control
* [Snippets](snippets.md) — Python and CLI examples
* [AI Integration](ai-integration.md) — Claude Code / Codex / OpenClaw plugins, MCP, migration from other memory systems

## Related

* Concepts: [Agent memory](../../concepts/agent-memory.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md) · [GraphRAG](../../concepts/graphrag.md) · [MCP](../../concepts/mcp.md)
* Peers: [Graphiti](../graphiti/index.md), [LightRAG](../lightrag/index.md), [Mem0](../mem0/index.md), [Microsoft GraphRAG](../graphrag/index.md), [Graphify](../graphify/index.md)
* Backends: [Neo4j](../../databases/neo4j/index.md), [FalkorDB](../../databases/falkordb/index.md), [Qdrant](../../databases/qdrant/index.md), [pgvector](../../databases/pgvector/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
