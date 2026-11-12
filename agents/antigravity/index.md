---
type: Software
title: Antigravity
description: Google's agent-first development platform — the Antigravity 2.0 desktop app for orchestrating parallel autonomous agents and the Antigravity CLI (agy), sharing one agent engine on Gemini models with Managed Agents sandboxes; successor to Gemini CLI for consumer plans.
resource: https://antigravity.google
tags: [antigravity, google, gemini, coding-agents, agent-orchestration]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: antigravity-site
    resource: "https://antigravity.google/"
    title: "Antigravity — official site"
    author: "site:antigravity.google"
  - id: antigravity-2
    resource: "https://antigravity.google/product/antigravity-2"
    title: "Antigravity 2.0 product page"
    author: "site:antigravity.google"
  - id: agy-github
    resource: "https://github.com/google-antigravity/antigravity-cli"
    title: "google-antigravity/antigravity-cli"
    author: "site:github.com"
  - id: gemini-cli-transition
    resource: "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
    title: "Transitioning Gemini CLI to Antigravity CLI"
    author: "site:developers.googleblog.com"
  - id: io-2026
    resource: "https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/"
    title: "Google I/O 2026 developer highlights"
    author: "site:blog.google"
---

# Antigravity

**Antigravity** is Google's platform for working *through* agents rather than alongside them. **Antigravity 2.0** (desktop app, launched around Google I/O 2026) lets you run several autonomous agents in parallel across projects and review their work; **Antigravity CLI** (`agy`) brings the same engine to the terminal. It replaced Gemini CLI and Gemini Code Assist for Google AI Pro/Ultra and free individual users in June 2026.

| | |
|---|---|
| Category | [Coding agents](../../concepts/coding-agents.md) · [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md) |
| License | Proprietary (free and paid Google plans) |
| Latest | Antigravity CLI 1.5.7 (2026-11-12) |
| Models | Gemini (default Gemini 3.5 Flash at 2.0 launch) |
| Surfaces | Desktop app (2.0) · CLI (`agy`) · Managed Agents in the Gemini API |

## Contents

* [Overview](overview.md) — agent-first model, desktop vs CLI, Gemini CLI transition
* [Agents](agents.md) — orchestration, Managed Agents, sandboxes, trust
* [Installation](installation.md) — desktop app and CLI
* [Snippets](snippets.md) — CLI usage
* [AI Integration](ai-integration.md) — how it relates to other agents and tools

## Related

* Concepts: [Coding agents](../../concepts/coding-agents.md) · [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md) · [Agent security](../../concepts/agent-security.md)
* Peers: [Claude Code](../claude-code/index.md), [Codex](../codex/index.md), [OpenCode](../opencode/index.md); editors [Cursor](../../editors/cursor/index.md), [Windsurf](../../editors/windsurf/index.md)
* Comparison: [Agents alternatives](../alternatives.md)
