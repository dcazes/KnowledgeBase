---
type: Reference
title: OpenClaw — Architecture
description: OpenClaw's building blocks — gateway, workspace, channel plugins, skills, and connected coding agents.
resource: https://docs.openclaw.ai/
tags: [openclaw, architecture, gateway, channels, skills, agents, mcp]
generated: { by: "human:daniel", at: "2026-07-09T03:12:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:12:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: docs-architecture-what-is-openclaw
    resource: "https://docs.openclaw.ai/"
    title: "Docs — architecture/what is OpenClaw"
    author: "site:docs.openclaw.ai"
  - id: overview
    resource: "overview.md"
    title: "Overview"
---

# OpenClaw — Building blocks

* **Gateway** — the core server that runs OpenClaw and bridges everything.
* **Workspace** — the assistant's working directory (state, config, skills).
* **Channels** — plugins that connect chat platforms. Each channel carries messages in/out:
  Discord, Google Chat, iMessage, Matrix, MS Teams, Signal, Slack, Telegram, WhatsApp, Zalo, and 30+ more.
* **Skills** — reusable automation packages the community builds (the assistant's capabilities).
* **Coding agents** — OpenClaw can hand tasks to connected AI coding agents.

# Data flow

```
chat app (Discord/Telegram/…)
   │  channel plugin
   ▼
Gateway ── workspace + skills
   │
   ├─ LLM (Claude / GPT / local)
   └─ coding agents (Hermes / OpenCode)
          │
          └─ your tools via MCP (Graphify, Firecrawl, SearXNG)
```

# Why a gateway model

A single assistant fronts many chat surfaces; you configure channels + skills once, and every connected app gets the same capabilities. This is the "command center for agents" pattern.

# MCP

OpenClaw supports **local MCP mode** (notably in the Windows Hub) so it can expose/consume MCP tools — letting it call your stack's services (Firecrawl, Graphify, SearXNG) as tools.
