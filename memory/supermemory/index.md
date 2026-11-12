---
type: Software
title: Supermemory
description: Memory and context layer for AI — automatic fact extraction with contradiction handling and forgetting, user profiles, hybrid RAG + memory search, connectors (Drive, Gmail, Notion, GitHub), multi-modal extractors, plugins and MCP. Hosted API or a single local binary.
resource: https://github.com/supermemoryai/supermemory
tags: [supermemory, agent-memory, rag, mcp, user-profiles, typescript]
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

# Supermemory

**Supermemory** bundles memory, [RAG](../../concepts/rag.md), user profiles and data connectors behind one API, so an app or assistant gets "what this user cares about" plus relevant documents in a single call. It also ships memory plugins for coding agents and a hosted [MCP](../../concepts/mcp.md) server, and in 2026 added **Supermemory Local** — one binary that runs the engine on your machine.

| | |
|---|---|
| Category | [Agent memory](../../concepts/agent-memory.md) · [RAG](../../concepts/rag.md) |
| License | MIT (engine, plugins, MCP server) |
| SDKs | `supermemory` on npm (5.1.2) and PyPI (5.0.1) |
| Latest server release | server-v0.0.9 (2026-10-12) |
| Deployment | Hosted API · Supermemory Local (single binary, Ollama for offline) |

## Contents

* [Overview](overview.md) — memory, profiles, hybrid search, connectors, extractors
* [Installation](installation.md) — hosted, local binary, SDKs
* [Configuration](configuration.md) — container tags, connectors, local models
* [Snippets](snippets.md) — add, profile, search, MCP config
* [AI Integration](ai-integration.md) — plugins for Claude Code, Cursor, Codex, OpenCode, OpenClaw, Hermes

## Related

* Concepts: [Agent memory](../../concepts/agent-memory.md) · [RAG](../../concepts/rag.md) · [Document parsing](../../concepts/document-parsing.md) · [MCP](../../concepts/mcp.md)
* Peers: [Mem0](../mem0/index.md), [Zep](../zep/index.md), [Honcho](../honcho/index.md), [Hindsight](../hindsight/index.md), [MemOS](../memos/index.md); local-first RAG apps [SurfSense](../../browsers/surfsense/index.md), [AnythingLLM](../../apps/anythingllm/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
