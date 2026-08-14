---
type: Reference
title: Supermemory
description: AI memory & knowledge companion (supermemory.ai) — saves browsing/snippets into a personal semantic memory with local-first data; app data present on this machine.
resource: https://supermemory.ai
tags: [supermemory, memory, knowledge, local-first, pglite]
timestamp: 2026-08-13T00:00:00Z
---

# Supermemory

An **AI memory / knowledge companion** (supermemory.ai) — captures web pages, snippets, and notes into a personal searchable memory, then answers questions from that memory. Its desktop app stores data locally (`pglite` Postgres + local ONNX embedding via Xenova, plus an encrypted env blob), which is exactly the layout found on this machine.

Local state: `programs/supermemory/.supermemory/` — **app data only, no source checkout** (verified 2026-08-12). Contains `api-key`, `auth-secret`, `instance-id`, `env.enc` (encrypted env), `models/Xenova` (local embeddings), `runtime/pglite` (embedded Postgres), `runtime/ort-web` + `ort-native` (ONNX runtimes), and a ~4.3 MB `data` blob. Timestamps 2026-07-19/20 → the app **was installed and run**, then not updated.

## Contents

* [Overview](overview.md) — what Supermemory is, memory capture (browser, snippets), semantic Q&A
* [Installation](installation.md) — desktop app install; what `.supermemory/` shows; no source checkout here
* [Configuration](configuration.md) — api-key / auth-secret / env.enc, local embedding models, pglite storage
* [AI Integration](ai-integration.md) — answering from memory, browser extension capture, vs local memory stack
* [Alternatives](alternatives.md) — Rewind, Rewind.ai, Mem0/MemOS, Recall, vs Supermemory

## Related

* [MemOS](../memos/index.md), [Mem0](../mem0/index.md) — developer-facing memory platforms; Supermemory is an end-user app
* [Obsidian](../obsidian/index.md) — personal knowledge base; Supermemory = AI-memory companion

# Citations

[1] [Supermemory](https://supermemory.ai)
[2] [Supermemory GitHub](https://github.com/supermemoryai/supermemory)

## Last verified

**2026-08-13** — Only `.supermemory/` data dir present (app ran 2026-07-19/20); no repo. Docs ground on local data layout + upstream.
