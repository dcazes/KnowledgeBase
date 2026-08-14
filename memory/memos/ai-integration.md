---
type: Reference
title: MemOS — AI Integration
description: How MemOS integrates as agent memory — MCP server for Hermes/OpenCode/Cursor, official Hermes & OpenClaw local plugins, and how it complements Graphiti.
resource: https://memos-docs.openmem.net/home/overview/
tags: [memos, integration, mcp, hermes, openclaw, opencode, memory, agents]
generated: { by: "human:daniel", at: "2026-07-16T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-16T00:00:00Z" } ]
status: stable
stale_after: 2027-01-12
sources:
  - id: memos-repo
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemOS repo"
    author: "site:github.com"
  - id: memos-hermes-plugin-news
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemOS Hermes plugin news"
    author: "site:github.com"
  - id: graphiti
    resource: "../graphiti/index.md"
    title: "Graphiti"
---

# MemOS as agent memory

MemOS exposes its memory over an **MCP server** (under `src/memos/api/`) and a REST API (`:8000`). Any MCP client can register it as a memory backend.

## Integration map

```text
Hermes / OpenCode / Cursor / Windsurf / OpenClaw
        │  MCP (or REST :8000)
        ▼
   MemOS  ── stores ──► textual / tree / preference / skill / KV / LoRA memory
        │
        ├─ vector DB (Qdrant / Milvus)
        └─ graph DB  (Neo4j / Postgres / Nebula)
```

## Hermes

* **Official Hermes Agent local plugin** (memos-local-plugin 2.0): hybrid retrieval (FTS5 + vector), smart dedup, tiered skill evolution, multi-agent collaboration, 100% local, zero cloud dependency.
* Register MemOS as an MCP server in Hermes skills/MCP config, or use the plugin for local-first memory.

## OpenClaw

* **Official OpenClaw plugin** — Cloud (hosted, ~72% lower token usage, multi-agent memory sharing) and **Local** (`v1.0.0`: on-device SQLite, hybrid search, task summarization, skill evolution, Memory Viewer dashboard).
* Upstream reports OpenClaw task completion rose **36.63% → 50.87%** with MemOS.

## OpenCode / Cursor / Windsurf

* Any MCP client can consume MemOS memory — add it as an `mcpServers` entry (OpenCode `.opencode.json`, Cursor/Windsurf MCP settings).

## How it relates to Graphiti

* **MemOS** = general / structured memory (textual, tree, preference, skill, parametric) — the "operating system" for memory.
* **Graphiti** = temporal context graph (time-aware episodes, provenance).
* They are complementary: MemOS for durable structured memory, Graphiti for evolving relational/episodic memory. Both can be wired into the same agent via MCP (see Agent Stack).

## Notes

* LLM/embedder for MemOS can be local (Ollama) — keep it off the public internet; put behind **Tailscale** like the rest of the stack ([Tailscale](../../runtime/tailscale/index.md)).
* Memory feedback loop: correct/supplement memories via natural-language feedback over the API.
