---
type: Playbook
title: OpenClaw — Snippets & Cheat Sheet
description: Copy-paste setup and integration commands for OpenClaw (gateway, channels, MCP to your stack).
resource: https://docs.openclaw.ai/
tags: [openclaw, snippets, cheat-sheet, onboard, mcp, channels]
generated: { by: "human:daniel", at: "2026-07-09T03:15:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:15:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: installation
    resource: "installation.md"
    title: "Installation"
  - id: architecture
    resource: "architecture.md"
    title: "Architecture"
  - id: ai-integration
    resource: "ai-integration.md"
    title: "AI Integration"
---

# OpenClaw — Setup

```bash
openclaw onboard        # interactive: gateway → workspace → channels → skills
```

# Windows Hub

Install the native Hub for tray status, chat, node mode, and local MCP mode.

# Connect your stack via MCP (local MCP mode)

Point OpenClaw at:
* Graphify: `python -m graphify.serve`
* Firecrawl: `http://localhost:3002`
* SearXNG: `http://localhost:8080`

# Front an agent

Route channel messages to Hermes (`~/.hermes/`) or OpenCode (`.opencode.json`).

# Verify

```bash
openclaw status         # if available
# check gateway process / onboard logs
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Not found | not installed | install per docs |
| Channel down | token missing | re-run onboard for channel |
| MCP tools missing | server not running | start graphify/firecrawl/searxng |
