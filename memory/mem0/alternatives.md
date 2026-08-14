---
type: Comparison
title: Mem0 Alternatives
description: Mem0 vs MemOS, Graphiti, Zep, LangMem — when each memory approach fits; local vs cloud; how they differ for this agent stack.
resource: https://docs.mem0.ai
tags: [mem0, alternatives, memory, graphiti, memos, zep, comparison]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: mem0-docs-alternatives
    resource: "https://docs.mem0.ai"
    title: "Mem0 docs — alternatives"
    author: "site:docs.mem0.ai"
  - id: mem0-github
    resource: "https://github.com/mem0ai/mem0"
    title: "Mem0 GitHub"
    author: "site:github.com"
---

# Alternatives

| Tool | Model | Strengths | Fit here |
|---|---|---|---|
| **Mem0** | vector + graph, per-user scoping | simple API, multi-tenant user memory, OpenMemory UI, many backends | good default for per-user chat memory; **not deployed locally** (checkout only) |
| **MemOS** ([here](../memos/index.md)) | memory-OS, scheduling, KV/parametric | richest feature set, MCP server, benchmarks (LoCoMo 88.83) | the deployed-via-pip option on this machine |
| **Graphiti** ([here](../graphiti/index.md)) | temporal context graph | fact provenance, episodes, change tracking | best when memory must be auditable over time |
| **Zep** | temporal knowledge graph (cloud/OSS) | graph memory + fact extraction, hosted option | cloud-hosted alternative to Graphiti |
| **LangMem** | LangGraph memory | SDK for LangChain/LangGraph apps | only if already on LangChain |

## Choosing

* **Per-user chat memory, quick start** → Mem0 (library or OpenMemory).
* **Agent long-term memory with provenance** → Graphiti (or Zep).
* **Full-featured self-hosted memory OS** → MemOS (already documented as deployable here).
* **Graph vs scoped-keyword extraction matters** → Mem0's graph store (Neo4j) covers light graph needs; Graphiti is the heavy graph engine.

See the [memory comparison](../../meta/architecture/memory/memory-comparison.md) for the architecture-level view.
