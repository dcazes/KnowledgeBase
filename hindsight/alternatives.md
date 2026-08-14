---
type: Comparison
title: Hindsight Alternatives
description: Hindsight vs Graphiti, Mem0, MemOS, Zep, LangMem — learning-based agent memory vs storage/recall systems; fit for this stack.
resource: https://hindsight.vectorize.io
tags: [hindsight, alternatives, memory, comparison]
timestamp: 2026-08-13T00:00:00Z
---

# Alternatives

| Tool | Model | Strengths | Fit here |
|---|---|---|---|
| **Hindsight** | learning passes (agents learn over time) | SOTA LongMemEval, behavior improvement | strongest for agents that must improve; not deployed |
| **Graphiti** ([here](../graphiti/index.md)) | temporal context graph | fact provenance, episodes | auditable fact history |
| **Mem0** ([here](../mem0/index.md)) | vector + graph user memory | simple per-user API | quick user-fact memory |
| **MemOS** ([here](../memos/index.md)) | memory OS, scheduling | richest feature set, MCP | full-featured memory platform |
| **Zep** | temporal knowledge graph | hosted graph memory | cloud option |
| **LangMem** | LangGraph memory | LangChain-native | only on LangChain |

## Choosing

* **Agents that learn and improve** → Hindsight (learning passes) — the unique offering.
* **Fact memory with provenance** → Graphiti.
* **Per-user facts, simple API** → Mem0.
* **Full memory OS with MCP** → MemOS.
* **Combo**: Hindsight (learning) + Graphiti (provenance) is a strong pairing; see the [memory comparison](../architecture/memory/memory-comparison.md).

# Citations

[1] [Hindsight docs](https://hindsight.vectorize.io)
[2] [Hindsight GitHub](https://github.com/vectorize-io/hindsight)
