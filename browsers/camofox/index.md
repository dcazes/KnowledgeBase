---
type: Software
title: Camofox
description: REST browser server for AI agents built on Camoufox, a Firefox fork with C++-level fingerprint spoofing — accessibility snapshots with stable element refs, session isolation, cookies, proxies, VNC login, structured extraction, and MCP/OpenClaw tools.
resource: https://github.com/jo-inc/camofox-browser
tags: [camofox, camoufox, browser-automation, anti-detection, firefox, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: camofox-github
    resource: "https://github.com/jo-inc/camofox-browser"
    title: "jo-inc/camofox-browser on GitHub"
    author: "site:github.com"
  - id: camoufox-github
    resource: "https://github.com/daijro/camoufox"
    title: "daijro/camoufox on GitHub"
    author: "site:github.com"
  - id: camoufox-site
    resource: "https://camoufox.com"
    title: "Camoufox documentation"
    author: "site:camoufox.com"
---

# Camofox

**Camofox** (`camofox-browser`) wraps the **Camoufox** anti-detect Firefox in a REST API designed for agents. Instead of raw HTML it returns compact accessibility snapshots with stable element references (`e1`, `e2`…), so an LLM can read a page cheaply and click reliably. Every HTTP action is also exposed as an [MCP](../../concepts/mcp.md) / OpenClaw tool.

| | |
|---|---|
| Category | [Browser automation](../../concepts/browser-automation.md) |
| License | Camofox server: MIT · Camoufox browser: MPL-2.0 |
| Language | JavaScript (Node) server; Camoufox is a patched Firefox (C++) |
| Latest release | camofox-browser v1.19.0 (2026-11-10) · Camoufox v158.0.1-beta.41 |
| Default port | 9377 (OpenAPI at `/openapi.json`, docs at `/docs`) |

## Contents

* [Overview](overview.md) — architecture and feature set
* [Anti-detection](anti-detection.md) — how C++-level spoofing differs from stealth plugins
* [Installation](installation.md) — npx, source, Docker, OpenClaw plugin
* [Usage](usage.md) — tabs, snapshots, refs, macros, sessions
* [Snippets](snippets.md) — REST calls
* [AI Integration](ai-integration.md) — MCP tools, OpenClaw, agent loops

> Use anti-detection browsers only where you are allowed to automate: your own sites, sites whose terms permit it, or authorised testing. Bypassing access controls can breach terms of service or law.

## Related

* Concepts: [Browser automation](../../concepts/browser-automation.md) · [Web scraping & search](../../concepts/web-scraping.md) · [Agent security](../../concepts/agent-security.md)
* Peers: [CloakBrowser](../cloakbrowser/index.md) (Chromium equivalent), [browser-use](../browser-use/index.md), [Playwright MCP](../playwright-mcp/index.md), [Crawl4AI](../crawl4ai/index.md)
* Comparison: [Browser & web alternatives](../alternatives.md)
