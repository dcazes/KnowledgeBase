---
type: Reference
title: Firecrawl Playwright Service
description: Firecrawl's Playwright microservice — headless Chromium rendering for JavaScript-heavy pages and page actions, configuration, and alternatives.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, playwright, browser, subservice]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: firecrawl-selfhost
    resource: "https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md"
    title: "Self-hosting Firecrawl"
    author: "site:github.com"
  - id: playwright
    resource: "https://playwright.dev"
    title: "Playwright"
    author: "site:playwright.dev"
---

# Firecrawl — Playwright Service

A small HTTP service wrapping Playwright and headless Chromium. Workers call it (`PLAYWRIGHT_MICROSERVICE_URL`, typically `http://playwright-service:3000/scrape`) when a page needs JavaScript rendering or when a scrape includes actions such as click, scroll or wait.

* Rendering is the most memory-hungry part of the stack; size its container accordingly.
* Self-hosted rendering has no stealth features — heavily protected sites may block it. Anti-detection browsers such as [Camofox](../../camofox/index.md) and [CloakBrowser](../../cloakbrowser/index.md) target that problem; the cloud edition uses managed proxies.

See [Browser automation](../../../concepts/browser-automation.md).

## Related

[Subservices](index.md) · [Playwright MCP](../../playwright-mcp/index.md)
