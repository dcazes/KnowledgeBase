---
type: Reference
title: Cursor AI Integration
description: How Cursor connects to AI models and external tools via MCP, and how it relates to the rest of the local AI stack.
resource: https://docs.cursor.com/context/mcp
tags: [cursor, mcp, ai, integration, graphify, firecrawl, searxng]
generated: { by: "human:daniel", at: "2026-07-09T04:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: cursor-mcp-docs
    resource: "https://docs.cursor.com/context/mcp"
    title: "Cursor MCP Docs"
    author: "site:docs.cursor.com"
  - id: cursor-docs
    resource: "https://docs.cursor.com/"
    title: "Cursor Docs"
    author: "site:docs.cursor.com"
  - id: cursor
    resource: "https://cursor.com/"
    title: "Cursor"
    author: "site:cursor.com"
---

# Cursor AI Integration

Cursor is an AI client: it sends context to cloud models and renders their responses as edits, chat, and actions. Beyond the built-in models, it can reach external tools through the Model Context Protocol (MCP).

## Model Context Protocol (MCP)

Cursor supports MCP servers, letting the editor (and Agent mode) call external tools — web search, databases, custom APIs — as part of a prompt. Configure servers in Cursor's MCP settings; each server exposes tools the Agent can invoke.

Example servers that fit this stack:

- **Graphify** — the project's MCP server for graph/query tooling ([Graphify MCP server](../../memory/graphify/mcp-server.md)).
- **Firecrawl** — web scraping / crawl-to-markdown.
- **SearXNG** — self-hosted metasearch.

## Relationship to other stack agents/editors

| Component | Role | Talks to Cursor via |
|-----------|------|---------------------|
| Graphify | MCP server | MCP tools |
| Firecrawl | MCP server | MCP tools |
| SearXNG | MCP server | MCP tools |
| OpenCode | Terminal coding agent | Separate; not MCP-linked ([OpenCode](../../agents/opencode/index.md)) |
| Hermes | Assistant/agent runtime | Separate; orchestrates this KB ([Hermes](../../agents/hermes/index.md)) |
| VSCode | Base editor | Heritage; Cursor is a fork ([VSCode](../vscode/index.md)) |
| Windsurf | Competing AI editor | Separate; "Cascade" agent ([Windsurf](../windsurf/index.md)) |

## Usage pattern

1. Add an MCP server in Cursor settings (JSON config — see [Snippets](snippets.md)).
2. In Agent or Chat, reference the tool; Cursor invokes the MCP server and feeds results back into the model context.
3. The model acts on the tool output (edits, answers, or further tool calls).

> **Note:** MCP config shape and available server fields should be confirmed against the current Cursor docs at write time.
