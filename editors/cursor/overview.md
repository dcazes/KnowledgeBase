---
type: Concept
title: Cursor Overview
description: How Cursor works — codebase indexing with embeddings, the agent loop with tools and terminal, rules and AGENTS.md for project context, cloud agents, and privacy mode.
resource: https://cursor.com/docs
tags: [cursor, overview, indexing, agent]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cursor-docs
    resource: "https://cursor.com/docs"
    title: "Cursor documentation"
    author: "site:cursor.com"
---

# Cursor — Overview

* **Codebase indexing.** Cursor chunks and embeds your repository so the agent can semantically search it — [RAG](../../concepts/rag.md) over code, in contrast to [Graphify](../../memory/graphify/index.md)'s graph approach. Privacy mode keeps code from being stored by providers.
* **Agent.** Plans, searches, edits multiple files, runs terminal commands (with approval settings), reads lints and iterates. Ask and plan modes are read-only.
* **Project context.** Rules files (`.cursor/rules/*.mdc`) and `AGENTS.md` steer behaviour; memories persist preferences — see [Context engineering](../../concepts/context-engineering.md).
* **Cloud (background) agents.** Run tasks remotely in parallel on a branch, then hand back a PR; also triggerable from Slack, GitHub and mobile.
* **Extensibility.** [MCP](../../concepts/mcp.md) servers, plugins from the Cursor Marketplace (e.g. [Honcho](../../memory/honcho/ai-integration.md) memory), and a Cursor CLI for terminal use.

## Related

[Cursor index](index.md) · [Features](features.md)
