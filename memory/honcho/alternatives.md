---
type: Comparison
title: Honcho Alternatives
description: Honcho vs Mem0, MemOS, Graphiti, Zep, LangMem — user modeling vs memory stores, fit for this stack.
resource: https://docs.honcho.dev
tags: [honcho, alternatives, memory, personas, comparison]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: honcho-docs
    resource: "https://docs.honcho.dev"
    title: "Honcho docs"
    author: "site:docs.honcho.dev"
  - id: honcho-github
    resource: "https://github.com/plastic-labs/honcho"
    title: "Honcho GitHub"
    author: "site:github.com"
---

# Alternatives

| Tool | Model | Strengths | Fit here |
|---|---|---|---|
| **Honcho** | user modeling: personas, state machine, insights/goals | answers "who is the user"; stateful UX | unique — none of the others model the user |
| **Mem0** ([here](../mem0/index.md)) | vector + graph user memory | per-user facts with simple API | memory store without user-model layer |
| **MemOS** ([here](../memos/index.md)) | memory OS, scheduling, KV | richest feature set, benchmarks | memory store; no persona modeling |
| **Graphiti** ([here](../graphiti/index.md)) | temporal context graph | fact provenance over time | fact history, not user model |
| **Zep** | temporal knowledge graph | hosted graph memory | cloud alternative to Graphiti |
| **LangMem** | LangGraph memory SDK | LangChain-native | only on LangChain |

## Choosing

* **Personalized agent UX (stateful, user-aware)** → Honcho (+ any store beneath).
* **Store user facts simply** → Mem0.
* **Full memory OS / MCP** → MemOS.
* **Auditable fact history** → Graphiti.
* **Combos**: Honcho for the user model, Graphiti for provenance, Mem0/MemOS for bulk storage.
