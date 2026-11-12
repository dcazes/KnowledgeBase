---
type: Concept
title: Supermemory Overview
description: What Supermemory does — fact extraction with temporal updates, contradictions and forgetting; static and dynamic user profiles; hybrid search across knowledge-base documents and memories; connectors and multi-modal extractors.
resource: https://supermemory.ai/docs
tags: [supermemory, overview, user-profiles, hybrid-search]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: supermemory-github
    resource: "https://github.com/supermemoryai/supermemory"
    title: "supermemoryai/supermemory on GitHub"
    author: "site:github.com"
  - id: supermemory-docs
    resource: "https://supermemory.ai/docs"
    title: "Supermemory documentation"
    author: "site:supermemory.ai"
---

# Supermemory — Overview

| Feature | What it does |
|---|---|
| Memory | Extracts facts from conversations; handles temporal changes, contradictions and automatic forgetting of expired information |
| User profiles | Auto-maintained context in two parts: **static** (stable facts) and **dynamic** (recent activity) — one call, ~50 ms |
| Hybrid search | RAG over uploaded documents and personal memory in one query |
| Connectors | Google Drive, Gmail, Notion, OneDrive, GitHub with webhook sync |
| Extractors | PDFs, images (OCR), video (transcription), code (AST-aware chunking) |

Everything lives in one memory structure and ontology, and data is partitioned by **container tags** (per user, project or client).

## Design stance

Supermemory hides the plumbing — no vector database to configure, no chunking strategy, no embedding pipeline — in exchange for less control than assembling your own stack from [Docling](../../ingestion/docling/index.md), [Qdrant](../../databases/qdrant/index.md) and [Mem0](../mem0/index.md). The team describes itself as a research lab and claims top results on LongMemEval, LoCoMo and ConvoMem; see [MemOS benchmarks](../memos/benchmarks.md) for how to read such claims.

## Related

[Supermemory index](index.md) · [Snippets](snippets.md) · [Agent memory](../../concepts/agent-memory.md)
