---
type: Playbook
title: Cursor Snippets & Cheat Sheet
description: Practical Cursor snippets — quick-start, Agent mode usage, MCP JSON config, and a keyboard cheat sheet.
resource: https://docs.cursor.com/
tags: [cursor, snippets, mcp, cheat-sheet, agent, config]
generated: { by: "human:daniel", at: "2026-07-09T04:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: cursor-docs
    resource: "https://docs.cursor.com/"
    title: "Cursor Docs"
    author: "site:docs.cursor.com"
  - id: cursor-mcp-docs
    resource: "https://docs.cursor.com/context/mcp"
    title: "Cursor MCP Docs"
    author: "site:docs.cursor.com"
  - id: cursor
    resource: "https://cursor.com/"
    title: "Cursor"
    author: "site:cursor.com"
---

# Cursor Snippets & Cheat Sheet

## Quick start

1. Download and install from `https://cursor.com/download`.
2. Sign in to your Cursor account.
3. Verify:

   ```bash
   cursor --version
   ```

## Agent mode usage

- Open the Chat panel and switch to **Agent** mode.
- Describe a task in natural language (e.g. "Refactor `utils.ts` to use async/await and add tests").
- The Agent edits multiple files and may run terminal commands; review and accept its changes.

## MCP config snippet

Cursor reads MCP servers from its settings (JSON). Example wiring Graphify, Firecrawl, and SearXNG:

```json
{
  "mcpServers": {
    "graphify": {
      "url": "http://localhost:3000/mcp",
      "transport": "http"
    },
    "firecrawl": {
      "url": "http://localhost:8000/mcp",
      "transport": "http"
    },
    "searxng": {
      "url": "http://localhost:8080/mcp",
      "transport": "http"
    }
  }
}
```

> Adjust `url`/`transport` to match each server's actual endpoint. The exact field names follow Cursor's MCP settings schema — confirm against current docs.

## Keyboard cheat sheet

| Action | macOS | Linux / Windows |
|--------|-------|-----------------|
| Accept Tab completion | `Tab` | `Tab` |
| Inline edit (Cmd-K) | `Cmd-K` | `Ctrl-K` |
| Open Chat | `Cmd-L` | `Ctrl-L` |
| Toggle Agent mode | Chat panel toggle | Chat panel toggle |
| Command palette | `Cmd-Shift-P` | `Ctrl-Shift-P` |

## Related

- [AI Integration](ai-integration.md) — how MCP servers connect.
- [Graphify MCP server](../../memory/graphify/mcp-server.md)
- [OpenCode](../../agents/opencode/index.md) — terminal alternative.
