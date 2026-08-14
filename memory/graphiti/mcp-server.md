---
type: Reference
title: Graphiti — MCP Server
description: Graphiti's Model Context Protocol (MCP) server — deploy with Docker + Neo4j to give Claude/Cursor/MCP clients temporal context-graph memory.
resource: https://github.com/getzep/graphiti/tree/main/mcp_server
tags: [graphiti, mcp, mcp-server, claude, cursor, agent-memory, docker]
generated: { by: "human:daniel", at: "2026-07-09T05:04:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T05:04:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: mcp-server-repo
    resource: "https://github.com/getzep/graphiti/tree/main/mcp_server"
    title: "MCP server (repo)"
    author: "site:github.com"
  - id: graphiti-readme-mcp
    resource: "https://github.com/getzep/graphiti#mcp-server"
    title: "Graphiti README — MCP"
    author: "site:github.com"
  - id: graphify-mcp
    resource: "/../../graphify/mcp-server.md"
    title: "Graphify MCP"
---

# MCP server

The `mcp_server/` directory in the Graphiti repo contains a **Model Context Protocol (MCP) server** implementation. It lets AI assistants interact with Graphiti's context-graph capabilities over MCP — giving Claude, Cursor, and other MCP clients **temporal, provenance-aware memory**.

Per the README tip: *"Check out the new MCP server for Graphiti! Give Claude, Cursor, and other MCP clients powerful context graph-based memory with temporal awareness."*

# Deploy

The MCP server can be deployed with **Docker + Neo4j** for easy integration into an assistant workflow. (See `mcp_server/README.md` in the repo for exact compose/run steps.)

# Why it's useful here

Wire the Graphiti MCP server into your stack's agents:
* **Hermes** (`~/.hermes/`) — register as an MCP tool for temporal memory.
* **OpenCode** (`.opencode.json`) — add as an `mcpServers` entry.
* **Cursor / Windsurf** — MCP clients that can consume Graphiti memory.
* **Claude / any MCP client** — standard MCP.

This complements **Graphify's MCP** (static graph) with a *live, time-aware* layer.

# Relationship to Graphify MCP

| Server | Graph type | Use |
|--------|-----------|-----|
| **Graphify MCP** | static, confidence-tagged | compiled from a folder |
| **Graphiti MCP** | temporal, episode-backed | evolving agent memory |
