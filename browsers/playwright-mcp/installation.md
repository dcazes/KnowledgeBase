---
type: Playbook
title: Playwright MCP Installation
description: Add Playwright MCP to Claude Code, VS Code, Cursor and other clients with the standard npx config, run it as an HTTP server, or attach to your own Chrome via the browser extension.
resource: https://github.com/microsoft/playwright-mcp
tags: [playwright-mcp, installation, mcp-config]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: playwright-mcp-github
    resource: "https://github.com/microsoft/playwright-mcp"
    title: "microsoft/playwright-mcp on GitHub"
    author: "site:github.com"
---

# Playwright MCP — Installation

## Standard config (most clients)

```json
{ "mcpServers": { "playwright": { "command": "npx", "args": ["@playwright/mcp@latest"] } } }
```

```bash
claude mcp add playwright npx @playwright/mcp@latest        # Claude Code
```

VS Code, Cursor, Windsurf, Cline, Goose and Antigravity use the same command in their own config formats.

## HTTP mode

```bash
npx @playwright/mcp@latest --port 8931 --headless
```

Clients then connect over HTTP to that port. Bind to localhost or a private network; `--allowed-hosts` restricts which hosts may connect.

## Use your real browser

`--extension` connects to a running Chrome or Edge through the "Playwright Extension", reusing your logged-in sessions — convenient, but the agent then acts as you.

## Related

[Playwright MCP index](index.md) · [Snippets](snippets.md)
