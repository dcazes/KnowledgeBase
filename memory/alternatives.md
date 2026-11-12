---
type: Comparison
title: Memory & Knowledge Graph Alternatives
description: Side-by-side comparison of the agent-memory, GraphRAG and knowledge-graph tools in this vault — Mem0, Zep, Graphiti, Letta, Honcho, Hindsight, MemOS, Supermemory, Cognee, LightRAG, Microsoft GraphRAG and Graphify — with a decision guide.
resource: https://github.com/topics/agent-memory
tags: [memory, comparison, alternatives, agent-memory, graphrag, knowledge-graph]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: mem0
    resource: "https://github.com/mem0ai/mem0"
    title: "Mem0"
    author: "site:github.com"
  - id: graphiti
    resource: "https://github.com/getzep/graphiti"
    title: "Graphiti"
    author: "site:github.com"
  - id: zep
    resource: "https://www.getzep.com"
    title: "Zep"
    author: "site:getzep.com"
  - id: letta
    resource: "https://github.com/letta-ai/letta-code"
    title: "Letta Code"
    author: "site:github.com"
  - id: honcho
    resource: "https://github.com/plastic-labs/honcho"
    title: "Honcho"
    author: "site:github.com"
  - id: hindsight
    resource: "https://github.com/vectorize-io/hindsight"
    title: "Hindsight"
    author: "site:github.com"
  - id: memos
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemOS"
    author: "site:github.com"
  - id: supermemory
    resource: "https://github.com/supermemoryai/supermemory"
    title: "Supermemory"
    author: "site:github.com"
  - id: cognee
    resource: "https://github.com/topoteretes/cognee"
    title: "Cognee"
    author: "site:github.com"
  - id: lightrag
    resource: "https://github.com/HKUDS/LightRAG"
    title: "LightRAG"
    author: "site:github.com"
  - id: graphrag
    resource: "https://github.com/microsoft/graphrag"
    title: "Microsoft GraphRAG"
    author: "site:github.com"
  - id: graphify
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify"
    author: "site:github.com"
---

# Memory & Knowledge Graph Alternatives

Two related problems share this category:

* **[Agent memory](../concepts/agent-memory.md)** — remember users, sessions and the agent's own experience across conversations.
* **[GraphRAG](../concepts/graphrag.md) / [knowledge graphs](../concepts/knowledge-graphs.md)** — structure documents or code so retrieval can follow relationships.

## At a glance

| Tool | Core idea | Storage | Open source | Hosted option |
|---|---|---|---|---|
| [Mem0](mem0/index.md) | ADD-only fact extraction, hybrid search | Vector store (Qdrant, pgvector…) | Apache-2.0 | Mem0 Platform |
| [Graphiti](graphiti/index.md) | Bi-temporal context graph with provenance | Neo4j / FalkorDB / Neptune | Apache-2.0 | via Zep |
| [Zep](zep/index.md) | Governed context graphs for enterprises | Managed | Examples only | Yes (core product) |
| [Letta](letta/index.md) | Agent edits its own memory blocks; dreaming | Local or Letta Cloud | Apache-2.0 | Letta Cloud |
| [Honcho](honcho/index.md) | Reasoned peer representations (theory of mind) | Postgres + pgvector | AGPL-3.0 | api.honcho.dev |
| [Hindsight](hindsight/index.md) | Facts, experiences, observations, mental models; reflect | Postgres | MIT | Hindsight Cloud |
| [MemOS](memos/index.md) | Memory OS with cubes and a scheduler | Neo4j + Qdrant / SQLite | Apache-2.0 | MemOS Cloud |
| [Supermemory](supermemory/index.md) | Memory + RAG + profiles + connectors in one API | Managed / local binary | MIT | Yes |
| [Cognee](cognee/index.md) | remember/recall/improve/forget over graph + vectors | Kuzu/Neo4j + LanceDB/Qdrant… | Apache-2.0 | Cognee Cloud |
| [LightRAG](lightrag/index.md) | Dual-level graph + vector RAG, incremental | Files, Postgres, Neo4j, OpenSearch… | MIT | — |
| [Microsoft GraphRAG](graphrag/index.md) | Communities + summaries for global questions | Parquet | MIT (maintenance) | — |
| [Graphify](graphify/index.md) | Deterministic code/doc graph for coding agents | `graph.json` (+ Neo4j export) | Apache-2.0 | Graphify Cloud |
| [OpenConcho](openconcho/index.md) | UI for inspecting Honcho memory | — | MIT | — |

## Decision guide

| You need… | Start with |
|---|---|
| Simple per-user personalisation with any model | [Mem0](mem0/index.md) or [Supermemory](supermemory/index.md) |
| Facts that change over time, with history and provenance | [Graphiti](graphiti/index.md) (self-host) or [Zep](zep/index.md) (managed) |
| An agent that curates its own memory and improves | [Letta](letta/index.md), [Hindsight](hindsight/index.md) or [MemOS](memos/index.md) |
| Deep models of users and multi-agent perspectives | [Honcho](honcho/index.md) |
| Q&A over a growing document collection | [LightRAG](lightrag/index.md) or [Cognee](cognee/index.md) |
| Themes across a fixed corpus | [Microsoft GraphRAG](graphrag/index.md) |
| A coding agent that understands a repository | [Graphify](graphify/index.md) |
| Memory for Claude Code / Codex / OpenCode right now | Plugins from [Honcho](honcho/ai-integration.md), [Supermemory](supermemory/ai-integration.md), [Hindsight](hindsight/ai-integration.md), [Cognee](cognee/ai-integration.md), [Mem0](mem0/ai-integration.md) |

## Trends (late 2026)

* **Memory plugins for coding agents** are now standard: nearly every vendor ships Claude Code, Codex, Cursor, OpenCode, OpenClaw and Hermes integrations, plus [MCP](../concepts/mcp.md) servers and [skills](../concepts/agent-skills.md).
* **Hybrid retrieval** (semantic + BM25 + entity/graph) has replaced pure vector search almost everywhere.
* **Memory that learns** — reflection, dreaming, observations, skill crystallisation — is the new frontier beyond fact recall.
* **Benchmark inflation**: LoCoMo and LongMemEval scores above 90 are common; compare only under identical models and budgets ([Evals](../concepts/evals.md)).

## Related

[Agent memory](../concepts/agent-memory.md) · [GraphRAG](../concepts/graphrag.md) · [Databases alternatives](../databases/alternatives.md) · [AI landscape](../landscape.md)
