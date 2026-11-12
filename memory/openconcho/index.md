---
type: Software
title: OpenConcho
description: Community desktop and web UI for self-hosted Honcho — browse workspaces, peers, sessions, conclusions and dream passes, chat with memory context, and manage webhooks. Tauri desktop app, Docker image and Helm chart.
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, honcho, ui, agent-memory, tauri, react]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openconcho-github
    resource: "https://github.com/offendingcommit/openconcho"
    title: "offendingcommit/openconcho on GitHub"
    author: "site:github.com"
  - id: honcho-github
    resource: "https://github.com/plastic-labs/honcho"
    title: "plastic-labs/honcho on GitHub"
    author: "site:github.com"
---

# OpenConcho

**OpenConcho** is an unofficial, privacy-first front end for [Honcho](../honcho/index.md). It connects to your own Honcho instance and lets you see what the memory system has learned — peers, representations, conclusions, sessions and consolidation ("dream") passes — and chat through Honcho's memory-aware chat endpoint. Connection details stay in the browser.

| | |
|---|---|
| Category | [Agent memory](../../concepts/agent-memory.md) tooling |
| License | MIT |
| Stack | Tauri v2 desktop, React 19 + Vite, TanStack Router/Query, typed OpenAPI client |
| Latest release | v0.17.1 (2026-10-19) |
| Distribution | macOS/Linux/Windows binaries · Docker (`ghcr.io/offendingcommit/openconcho-web`) · Helm chart |

## Contents

* [Overview](overview.md) — features and how it talks to Honcho
* [Installation](installation.md) — binaries, web dev server, Docker, Helm
* [Configuration](configuration.md) — instances, auth, proxy allowlist
* [Snippets](snippets.md) — commands
* [AI Integration](ai-integration.md) — using it to debug agent memory

## Related

* [Honcho](../honcho/index.md) · [Agent memory](../../concepts/agent-memory.md) · [LLM observability](../../concepts/llm-observability.md)
* Comparison: [Memory alternatives](../alternatives.md)
