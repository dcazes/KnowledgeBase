---
type: Concept
title: Supermemory AI Integration
description: Integrate Supermemory — browser extension capture, answering from personal memory, export/interop, vs the developer memory stack (Mem0/MemOS/Graphiti).
resource: https://supermemory.ai
tags: [supermemory, integration, extension, memory]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: supermemory
    resource: "https://supermemory.ai"
    title: "Supermemory"
    author: "site:supermemory.ai"
  - id: supermemory-developers
    resource: "https://supermemory.ai/developers"
    title: "Supermemory developers"
    author: "site:supermemory.ai"
---

# Supermemory — AI Integration

Supermemory is an **end-user product** rather than a developer library — integration surface is the app + extension, not an SDK.

## Capture paths

* **Browser extension** — the primary ingest: save the current page, selected text, or highlights into memory while browsing.
* **In-app snippets** — paste notes/questions directly.

## Query paths

* **Chat with your memory** — ask the assistant; answers cite saved items.
* **Semantic search** — find past content by meaning.

## Developer interop

* Public API keys and a developer API exist upstream (supermemory.ai/developers) for programmatic save/query — not exercised on this machine.
* Local data (PGlite + local embeddings) is not directly queryable by other tools without the app's API.

## vs the developer memory stack

| Layer | Supermemory | [Mem0](../mem0/index.md) / [MemOS](../memos/index.md) / [Graphiti](../graphiti/index.md) |
|---|---|---|
| Audience | end user | developers/agents |
| Ingest | browser/app | SDK/API |
| Interface | chat UI | Python/JS, REST, MCP |
| Use here | personal memory companion | agent stack memory |

Both can coexist: Supermemory for personal browsing memory, the agent stack for app-level memory.
