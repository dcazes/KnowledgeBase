---
type: Reference
title: Graphify MCP Server
description: Serving a Graphify graph to MCP clients — the mcp extra's stdio server, how MCP access differs from the installed CLI skill, and query logging.
resource: https://github.com/Graphify-Labs/graphify
tags: [graphify, mcp, mcp-server]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphify-github
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify-Labs/graphify on GitHub"
    author: "site:github.com"
  - id: mcp-spec
    resource: "https://modelcontextprotocol.io"
    title: "Model Context Protocol"
    author: "site:modelcontextprotocol.io"
---

# Graphify — MCP Server

Install with the `mcp` extra (`uv tool install "graphifyy[mcp]"`) to run a stdio [MCP](../../concepts/mcp.md) server over a graph. MCP clients then call the server's tools (such as `query_graph`) instead of running CLI commands.

## Skill vs MCP

| Route | How the assistant queries |
|---|---|
| `graphify install` (skill) | Runs `graphify query` / `path` / `explain` locally against `graphify-out/` |
| MCP connection | Calls the tools the connected server lists; no local CLI needed |

`graphify install` does **not** set up an MCP connection; configure that in your client separately. A Docker MCP Toolkit + SQLite option is documented in the repo.

## When to prefer MCP

* The client cannot run shell commands, or you want the graph served from one machine to several clients.
* You want the same graph available to [Claude Code](../../agents/claude-code/index.md), [Cursor](../../editors/cursor/index.md) and [Hermes](../../agents/hermes/index.md) at once.

MCP `query_graph` calls are logged like CLI queries.

## Related

[Graphify index](index.md) · [MCP](../../concepts/mcp.md) · [AI Integration](ai-integration.md)
