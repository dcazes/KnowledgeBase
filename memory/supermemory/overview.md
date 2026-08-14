---
type: Concept
title: Supermemory Overview
description: What Supermemory is — personal AI memory: capture browsing/snippets, local semantic storage, question answering from memory; local-first desktop app.
resource: https://supermemory.ai
tags: [supermemory, overview, memory, semantic-search]
timestamp: 2026-08-13T00:00:00Z
---

# Overview

Supermemory positions itself as "your AI second brain": everything you read/save becomes searchable memory, and the assistant answers questions grounded in that memory.

## Capture

* **Browser extension** — save pages, snippets, and highlights while browsing.
* **Manual notes / snippets** — paste text directly into the app.

## Storage & retrieval

* Saved content is embedded (the local app uses a local embedding model — `models/Xenova` on this machine) and stored in an embedded Postgres (`runtime/pglite`).
* **Semantic search** — natural-language queries retrieve relevant memory.
* **Q&A** — the assistant answers from your memory with citations to saved items.

## Local-first desktop app

The desktop app keeps data locally (encrypted env, local model + DB). The local `.supermemory/` directory on this machine matches this exactly (instance-id, api-key, auth-secret, pglite, ONNX runtimes) — evidence the app ran here in July 2026.

## Position

End-user memory product (like a personal Rewind) rather than a developer library — it competes with consumer memory apps, while [Mem0](../mem0/index.md)/[MemOS](../memos/index.md) target agent/developer memory.

# Citations

[1] [Supermemory](https://supermemory.ai)
[2] [Supermemory GitHub](https://github.com/supermemoryai/supermemory)
