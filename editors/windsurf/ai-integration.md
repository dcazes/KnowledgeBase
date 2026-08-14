---
type: Reference
title: Windsurf — AI Integration
description: Connecting Windsurf (now Devin Desktop; agent = Devin Local, ex-Cascade) to your stack via MCP — Graphify, Firecrawl, SearXNG — and how it complements OpenCode/Hermes.
resource: https://docs.windsurf.com/
tags: [windsurf, mcp, cascade, integration, graphify, firecrawl, searxng]
timestamp: 2026-07-09T03:33:00Z
---

# MCP with Devin Local (ex-Cascade)

Windsurf (now Devin Desktop) supports **MCP servers**, so its agent (Devin Local, ex-Cascade) can call external tools. Register your stack's servers (exact config location: docs.windsurf.com; typically a settings/MCP JSON):

* **Graphify** — `python -m graphify.serve` (knowledge-graph queries).
* **Firecrawl** — web context API at `http://localhost:3002`.
* **SearXNG** — metasearch at `http://localhost:8080`.

Once registered, Devin Local can search the web, scrape, or query your graph as part of an edit plan.

# Relationship to other agents

| Tool | Style |
|------|-------|
| **Windsurf (Devin Local)** | agentic IDE, chat-driven edits |
| **OpenCode** | terminal-native interactive agent |
| **Hermes** | background/autonomous agent |
| **VSCode** | general editor + Copilot/MCP |

Use Windsurf for in-editor agentic coding; OpenCode for terminal control; Hermes for background automation.

# Notes

* MCP config syntax varies by Windsurf version — confirm in docs.windsurf.com.
* Web search for exact MCP setup was inconclusive; verify before relying on it.

# Citations

[1] [MCP / docs](https://docs.windsurf.com/)
[2] [Graphify MCP](/../../graphify/mcp-server.md)
[3] [OpenCode](/../../opencode/index.md)
[4] [Hermes](/../../hermes/index.md)
