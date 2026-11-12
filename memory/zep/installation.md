---
type: Playbook
title: Zep Installation
description: Get started with Zep Cloud — create a project and API key, install the Python, TypeScript or Go SDK, connect over MCP, and add the coding-agent plugins.
resource: https://help.getzep.com
tags: [zep, installation, sdk, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: zep-docs
    resource: "https://help.getzep.com"
    title: "Zep documentation"
    author: "site:help.getzep.com"
  - id: zep-github
    resource: "https://github.com/getzep/zep"
    title: "getzep/zep — examples and integrations"
    author: "site:github.com"
---

# Zep — Installation

Zep is a hosted service, so "installing" means creating a project and adding an SDK.

1. Sign up at getzep.com and create a project; copy its API key into `ZEP_API_KEY`.
2. Install an SDK:

```bash
pip install zep-cloud                    # Python
npm install @getzep/zep-cloud            # TypeScript / JavaScript
go get github.com/getzep/zep-go/v4       # Go
```

3. Optionally bulk-load existing data with `zep-ingest` (in the `getzep/zep` repo), which handles Slack exports, documents, email, JSON/CSV and fact triples.

## MCP and plugins

* Agents can connect to Zep through its [MCP](../../concepts/mcp.md) server instead of an SDK.
* **Build with Zep** — a plugin that teaches [Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md) and [Cursor](../../editors/cursor/index.md) how to build on Zep.
* **Zep Memory** — a plugin giving Claude Desktop and ChatGPT persistent memory backed by Zep.

## Self-hosting

There is no maintained self-hosted Zep server. To run the same approach on your own infrastructure, use [Graphiti](../graphiti/installation.md) with [Neo4j](../../databases/neo4j/index.md) or [FalkorDB](../../databases/falkordb/index.md).

## Related

[Zep index](index.md) · [Snippets](snippets.md) · [Graphiti installation](../graphiti/installation.md)
