---
type: Software
title: Playwright MCP
description: Microsoft's Model Context Protocol server for browser automation with Playwright — accessibility-tree snapshots instead of screenshots, deterministic element refs, and tools for navigation, forms, network, storage, tracing and more.
resource: https://github.com/microsoft/playwright-mcp
tags: [playwright-mcp, playwright, mcp, browser-automation, microsoft]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: playwright-mcp-github
    resource: "https://github.com/microsoft/playwright-mcp"
    title: "microsoft/playwright-mcp on GitHub"
    author: "site:github.com"
  - id: playwright
    resource: "https://playwright.dev"
    title: "Playwright"
    author: "site:playwright.dev"
  - id: playwright-cli
    resource: "https://github.com/microsoft/playwright-cli"
    title: "microsoft/playwright-cli"
    author: "site:github.com"
---

# Playwright MCP

**Playwright MCP** is the standard way to give an [MCP](../../concepts/mcp.md) client a browser. It drives Chromium, Firefox or WebKit through Playwright and returns structured **accessibility snapshots** with element refs, so models act deterministically without needing vision.

| | |
|---|---|
| Category | [Browser automation](../../concepts/browser-automation.md) · [MCP](../../concepts/mcp.md) |
| License | Apache-2.0 |
| Package | `@playwright/mcp` (npm), Node.js 18+ |
| Latest release | v0.0.85 (2026-11-09) |
| Clients | Claude Code/Desktop, VS Code, Cursor, Windsurf, Cline, Goose, Antigravity, and any MCP client |

## Contents

* [Overview](overview.md) — design, tools, MCP vs the Playwright CLI + skills
* [Installation](installation.md) — client configs, HTTP mode, extension mode
* [Snippets](snippets.md) — useful flags and configurations
* [AI Integration](ai-integration.md) — testing, research and agent use

## Related

* Concepts: [MCP](../../concepts/mcp.md) · [Browser automation](../../concepts/browser-automation.md) · [Agent skills](../../concepts/agent-skills.md)
* Peers: [browser-use](../browser-use/index.md), [Camofox](../camofox/index.md), [Firecrawl](../firecrawl/index.md)
* Comparison: [Browser & web alternatives](../alternatives.md)
