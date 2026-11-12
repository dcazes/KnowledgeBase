---
type: Software
title: Hindsight
description: Agent memory system from Vectorize focused on agents that learn — memory banks of world facts, experiences, observations and mental models, with retain / recall / reflect operations, four-way hybrid retrieval and built-in MCP.
resource: https://github.com/vectorize-io/hindsight
tags: [hindsight, agent-memory, vectorize, mcp, python, postgres]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hindsight-github
    resource: "https://github.com/vectorize-io/hindsight"
    title: "vectorize-io/hindsight on GitHub"
    author: "site:github.com"
  - id: hindsight-docs
    resource: "https://hindsight.vectorize.io"
    title: "Hindsight documentation"
    author: "site:hindsight.vectorize.io"
  - id: hindsight-paper
    resource: "https://arxiv.org/abs/2512.12818"
    title: "Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects"
    author: "arXiv 2512.12818"
  - id: hindsight-benchmarks
    resource: "https://benchmarks.hindsight.vectorize.io"
    title: "Hindsight benchmark results"
    author: "site:benchmarks.hindsight.vectorize.io"
---

# Hindsight

**Hindsight** is an agent memory server built around the idea that agents should *learn* from what they experience, not just recall chat history. Memories live in **banks**, are organised into human-memory-like types, and are retrieved with four strategies in parallel. It reports state-of-the-art LongMemEval results, independently reproduced by Virginia Tech researchers.

| | |
|---|---|
| Category | [Agent memory](../../concepts/agent-memory.md) |
| License | MIT |
| Language | Python server (`hindsight-api`); clients for Python, Node.js, Go, CLI |
| Latest release | v1.2.1 (2026-11-10) |
| Deployment | Docker (API `:8888`, UI `:9999`) · pip · Helm · embedded Python · Hindsight Cloud |
| Storage | PostgreSQL (embedded `pg0` or external); Oracle AI Database for enterprise |

## Contents

* [Overview](overview.md) — memory types, retain/recall/reflect, observations, mental models
* [Installation](installation.md) — Docker, external Postgres, pip, Helm, embedded
* [Configuration](configuration.md) — LLM providers, storage, Hindsight models
* [Snippets](snippets.md) — clients, LLM wrapper, MCP endpoint
* [AI Integration](ai-integration.md) — coding agents, frameworks, no-code tools

## Related

* Concepts: [Agent memory](../../concepts/agent-memory.md) · [RAG](../../concepts/rag.md) · [MCP](../../concepts/mcp.md) · [Evals](../../concepts/evals.md)
* Peers: [Mem0](../mem0/index.md), [Zep](../zep/index.md), [Letta](../letta/index.md), [Honcho](../honcho/index.md), [Supermemory](../supermemory/index.md), [MemOS](../memos/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
