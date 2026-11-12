---
type: Software
title: Honcho
description: Reasoning-first memory infrastructure from Plastic Labs — stores messages from peers (users and agents) in sessions, reasons over them in the background, and serves peer representations, conclusions, session context and natural-language answers.
resource: https://github.com/plastic-labs/honcho
tags: [honcho, agent-memory, peers, theory-of-mind, mcp, python, typescript]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: honcho-github
    resource: "https://github.com/plastic-labs/honcho"
    title: "plastic-labs/honcho on GitHub"
    author: "site:github.com"
  - id: honcho-docs
    resource: "https://honcho.dev/docs/v3"
    title: "Honcho documentation (v3)"
    author: "site:honcho.dev"
  - id: honcho-evals
    resource: "https://honcho.dev/evals/"
    title: "Honcho evals"
    author: "site:honcho.dev"
---

# Honcho

**Honcho** models the *people and agents* an application talks to. You store messages on sessions; a background "deriver" reasons over them and builds a **representation** of each peer — what they know, prefer and believe. You then ask Honcho questions in natural language ("what learning style works for this student?") or pull prompt-ready context. Where most [agent memory](../../concepts/agent-memory.md) retrieves chunks, Honcho retrieves *conclusions*.

| | |
|---|---|
| Category | [Agent memory](../../concepts/agent-memory.md) |
| License | AGPL-3.0 |
| Server | Python 3.13+ FastAPI service; PostgreSQL + [pgvector](../../databases/pgvector/index.md); Redis optional |
| SDKs | Python `honcho-ai` 2.9.0 · TypeScript `@honcho-ai/sdk` |
| Latest release | v3.6.1 (2026-11-11) |
| Deployment | Managed (api.honcho.dev) · local via `honcho start` · self-hosted Docker or from source |
| UI | [OpenConcho](../openconcho/index.md) (community) |

## Contents

* [Overview](overview.md) — peers, sessions, scopes, conclusions, representations, dreaming
* [Installation](installation.md) — managed, CLI local stack, Docker, from source
* [Snippets](snippets.md) — Python and TypeScript store / reason / query / inject loop
* [AI Integration](ai-integration.md) — plugins for Claude Code, Codex, Cursor, OpenCode, OpenClaw, Hermes; MCP

## Related

* Concepts: [Agent memory](../../concepts/agent-memory.md) · [Context engineering](../../concepts/context-engineering.md) · [MCP](../../concepts/mcp.md)
* Peers: [Mem0](../mem0/index.md), [Zep](../zep/index.md), [Letta](../letta/index.md), [Hindsight](../hindsight/index.md), [Supermemory](../supermemory/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
