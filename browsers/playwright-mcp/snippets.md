---
type: Reference
title: Playwright MCP Snippets
description: Playwright MCP configuration snippets — headless and isolated profiles, browser and device selection, origin allow/block lists, proxies, saved storage state, extra capabilities, and output directories.
resource: https://github.com/microsoft/playwright-mcp
tags: [playwright-mcp, snippets, flags, cheat-sheet]
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

# Playwright MCP — Snippets

```json
{ "mcpServers": { "playwright": { "command": "npx", "args": [
  "@playwright/mcp@latest",
  "--headless",
  "--isolated",
  "--browser", "chromium",
  "--allowed-origins", "https://docs.example.com;https://github.com",
  "--storage-state", "./auth.json",
  "--caps", "pdf,devtools",
  "--output-dir", "./mcp-output"
] } } }
```

| Flag | Purpose |
|---|---|
| `--headless` | Headed by default; headless for servers and CI |
| `--isolated` | Keep the profile in memory only |
| `--user-data-dir` | Persistent profile directory |
| `--browser`, `--device`, `--viewport-size` | Engine and emulation |
| `--allowed-origins`, `--blocked-origins` | Limit what the browser may request (not a security boundary on its own) |
| `--proxy-server` | Route traffic through a proxy |
| `--storage-state` | Start logged in from a saved state file |
| `--secrets` | Values the model can reference without seeing |
| `--caps vision,pdf,devtools` | Extra tool groups |
| `--cdp-endpoint` | Attach to an existing Chromium (e.g. [CloakBrowser](../cloakbrowser/index.md)) |
| `--idle-timeout` | Close the browser after inactivity |

## Related

[Playwright MCP index](index.md) · [Installation](installation.md)
