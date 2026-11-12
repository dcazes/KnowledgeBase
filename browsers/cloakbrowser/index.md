---
type: Software
title: CloakBrowser
description: Stealth Chromium build with fingerprint patches in the C++ source, shipped as a drop-in replacement for Playwright and Puppeteer in Python, JavaScript and .NET — human-like input, proxy and GeoIP matching, WebRTC IP spoofing. Binary requires a (free) licence key.
resource: https://github.com/CloakHQ/CloakBrowser
tags: [cloakbrowser, chromium, browser-automation, anti-detection, playwright, puppeteer]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cloakbrowser-github
    resource: "https://github.com/CloakHQ/CloakBrowser"
    title: "CloakHQ/CloakBrowser on GitHub"
    author: "site:github.com"
  - id: cloakbrowser-site
    resource: "https://cloakbrowser.dev"
    title: "CloakBrowser website"
    author: "site:cloakbrowser.dev"
---

# CloakBrowser

**CloakBrowser** is a real Chromium binary with fingerprint surfaces modified at the source level (87 patches as of v0.7.2), wrapped so existing Playwright or Puppeteer code switches to it by changing one import. It is the Chromium counterpart to [Camofox](../camofox/index.md)'s Firefox approach.

| | |
|---|---|
| Category | [Browser automation](../../concepts/browser-automation.md) |
| License | Wrappers: MIT · Chromium build: distributed by CloakHQ, launch requires a licence key (free tier by email; Pro tier) |
| Packages | `cloakbrowser` on PyPI (0.7.2) and npm; `CloakBrowser` on NuGet |
| Latest | v0.7.2 — Chromium 156.0.8078.47.1 (2026-11) |
| Platforms | Linux x64/ARM64, Windows x64, macOS (Apple Silicon and Intel) |

## Contents

* [Overview](overview.md) — patches, humanize, proxies, licensing
* [Installation](installation.md) — pip, npm, .NET, Docker test
* [Usage](usage.md) — launch options and site-specific tips
* [Snippets](snippets.md) — Python, JavaScript, Puppeteer
* [AI Integration](ai-integration.md) — using it under browser agents and scrapers

> Use anti-detection browsers only where you are allowed to automate: your own sites, sites whose terms permit it, or authorised testing. Bypassing access controls can breach terms of service or law.

## Related

* Concepts: [Browser automation](../../concepts/browser-automation.md) · [Agent security](../../concepts/agent-security.md)
* Peers: [Camofox](../camofox/index.md), [browser-use](../browser-use/index.md), [Crawl4AI](../crawl4ai/index.md), [Playwright MCP](../playwright-mcp/index.md)
* Comparison: [Browser & web alternatives](../alternatives.md)
