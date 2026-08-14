---
type: Reference
title: Hermes — AI Integration
description: How Hermes relates to OpenCode (interactive) and OpenClaw (front-end), and how it extends its stack via skills/MCP tools (SearXNG, Firecrawl, Graphify).
resource: https://hermes-agent.nousresearch.com
tags: [hermes, opencode, openclaw, searxng, firecrawl, graphify, mcp, integration]
generated: { by: "human:daniel", at: "2026-07-09T03:25:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:25:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: hermes-integration-setup-note-vault
    resource: "/../../vault/03%20-%20Reference/Hermes%20Setup.md"
    title: "Hermes integration — setup note (vault)"
  - id: hermes-nous-research
    resource: "https://hermes-agent.nousresearch.com"
    title: "Hermes (Nous Research)"
    author: "site:hermes-agent.nousresearch.com"
  - id: opencode
    resource: "/../../opencode/index.md"
    title: "OpenCode"
  - id: searxng
    resource: "/../../searxng/index.md"
    title: "SearXNG"
  - id: firecrawl
    resource: "/../../firecrawl/index.md"
    title: "Firecrawl"
  - id: graphify
    resource: "/../../graphify/index.md"
    title: "Graphify"
---

# Hermes in your AI stack

Hermes is the **autonomous / background** agent. It pairs with other tools rather than competing with them.

| Role | Tool | Relationship to Hermes |
|------|------|------------------------|
| Autonomous/background agent | **Hermes** | Runs scheduled & background tasks |
| Interactive coding agent | OpenCode | Interactive, you drive it; Hermes runs in background |
| Multi-channel front-end | OpenClaw | Fronts Hermes across channels |

## OpenCode (interactive vs background)

OpenCode is the **interactive** coding agent — you sit with it, issuing commands turn by turn. Hermes is the **background** counterpart: it executes autonomous tasks, scheduled via cron, without a live operator. They share a machine but not a runtime model.

* [OpenCode](/../../opencode/index.md)

## OpenClaw (fronts Hermes)

OpenClaw is a front-end that **fronts Hermes**, exposing it across multiple chat channels. It is not a separate agent brain — it routes to Hermes.

* [OpenClaw](/../../openclaw/index.md) *(if present in KB)*

# Stack tools via skills / MCP

Hermes reaches external tools through its **skills** and **MCP** integration. Notable stack tools wired in this setup:

| Tool | Role | KB |
|------|------|-----|
| SearXNG | Self-hosted metasearch | [SearXNG](/../../searxng/index.md) |
| Firecrawl | Web scraping / crawl API | [Firecrawl](/../../firecrawl/index.md) |
| Graphify | Knowledge-graph extraction | [Graphify](/../../graphify/index.md) |

These appear as callable tools/skills inside Hermes, extending its web and data capabilities beyond the built-in `web` toolset.

# Browser & desktop integration

Hermes also drives **Camofox** (anti-detect browser) and the Linux desktop via `computer_use` — see [Browser](browser.md).

# Verify

```bash
ls ~/.hermes/skills/        # confirm stack-tool skills are installed
hermes setup tools          # confirm relevant toolsets enabled
```
