---
type: Reference
title: OpenClaw — AI Integration
description: Using OpenClaw to front your agents (Hermes/OpenCode) and tools (Firecrawl, Graphify, SearXNG) via channels and MCP.
resource: https://docs.openclaw.ai/
tags: [openclaw, integration, agents, hermes, opencode, mcp, skills]
timestamp: 2026-07-09T03:13:00Z
---

# Fronting your agents

OpenClaw can receive a chat message from any channel and delegate the work to a **coding agent**:
* **Hermes** — background/autonomous agent runtime (`~/.hermes/`).
* **OpenCode** — terminal-native interactive coding agent (`.opencode.json`).

Pattern:
```
Telegram → OpenClaw gateway → Hermes/OpenCode → result → Telegram
```

# Tools via MCP

Enable local MCP mode and point OpenClaw at your stack's MCP servers:
* **Graphify** — `python -m graphify.serve` (knowledge graph queries).
* **Firecrawl** — web context API (`:3002`).
* **SearXNG** — metasearch (`:8080`).

The assistant then gains web search / scrape / graph-retrieval skills.

# Skills

Build custom skills for repetitive tasks (e.g. "summarize my vault", "scrape this URL via Firecrawl"). Skills keep automation reusable across all channels.

# Relationship to other stack pieces

| Layer | Tool |
|-------|------|
| Channel front-end | **OpenClaw** |
| Agent runtime | Hermes / OpenCode |
| App builder | Dify |
| Chat UI | OpenWebUI / AnythingLLM |
| Tools | Firecrawl, Graphify, SearXNG |

# Citations

[1] [Architecture](architecture.md)
[2] [Hermes](/../../hermes/index.md)
[3] [OpenCode](/../../opencode/index.md)
[4] [Graphify MCP](/../../graphify/mcp-server.md)
