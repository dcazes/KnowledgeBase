---
type: Concept
title: SurfSense AI Integration
description: Use SurfSense — chat Q&A from personal knowledge, MCP server for agents (Hermes/OpenCode), API, vs other personal/agent memory.
resource: https://github.com/modsetter/surfsense
tags: [surfsense, integration, mcp, chat, agents]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: surfsense-github-mcp
    resource: "https://github.com/modsetter/surfsense/tree/main/mcp"
    title: "SurfSense GitHub — mcp"
    author: "site:github.com"
  - id: surfsense-docs
    resource: "https://docs.modsetter.com/surfsense"
    title: "SurfSense docs"
    author: "site:docs.modsetter.com"
---

# AI Integration

SurfSense exposes its personal knowledge graph two ways: an **AI chat** (frontend) and an **MCP server** (agent access).

## Chat (frontend :3000)

Ask natural-language questions; answers are grounded in scraped Reddit/YouTube/docs memory stored in the Zero graph.

## MCP server

The checkout ships `mcp/` (SurfSense MCP server — package + `surfsense_mcp` module, `manifest.json`, README). Agents (Hermes/OpenCode/Cursor) connect to query the same knowledge:

```
# MCP config for the agent stack
# - command/tool: surfsense MCP server (from mcp/ package)
# - exposes tools to search personal knowledge and trigger captures
```

## API

Backend (FastAPI, 8000-8001) exposes REST endpoints for search/capture; the UI and MCP both sit on it.

## In this stack

* SurfSense is the **personal knowledge layer** (browsing/scraped content).
* Agent-stack memory ([Mem0](../../memory/mem0/index.md), [MemOS](../../memory/memos/index.md), [Graphiti](../../memory/graphiti/index.md)) covers **agent/user memory** — complementary.
* MCP integration means Hermes/OpenCode can answer from personal web history via SurfSense tools, mirroring how [Graphify](../../memory/graphify/index.md) MCP exposes folder graphs.
