---
type: Concept
title: Browser Automation for AI
description: How AI agents use browsers — accessibility snapshots versus screenshots, element refs, CDP and Playwright, MCP browser servers, autonomous browser agents, stealth and anti-detection, authentication, and safety.
resource: https://playwright.dev
tags: [concept, browser-automation, agents, playwright, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: playwright
    resource: "https://playwright.dev"
    title: "Playwright"
    author: "site:playwright.dev"
  - id: playwright-mcp
    resource: "https://github.com/microsoft/playwright-mcp"
    title: "Playwright MCP"
    author: "site:github.com"
---

# Browser Automation for AI

When an API does not exist, agents use the web the way people do — through a browser. The challenge is turning a visual, dynamic page into something a model can read cheaply and act on reliably.

## Perception

| Method | Trade-off |
|---|---|
| Raw HTML | Huge and noisy |
| **Accessibility snapshot with refs** | Compact, structured, deterministic — [Playwright MCP](../browsers/playwright-mcp/overview.md), [Camofox](../browsers/camofox/overview.md) |
| Screenshots + vision (computer use) | Works on anything visual; slower and costlier |
| Clean Markdown | For reading only — [Firecrawl](../browsers/firecrawl/index.md), [Crawl4AI](../browsers/crawl4ai/index.md) |

## Control

* **Playwright / CDP** underneath almost everything.
* **MCP servers** give any client a browser: [Playwright MCP](../browsers/playwright-mcp/index.md), [Camofox](../browsers/camofox/index.md).
* **Autonomous agents** pursue a goal: [browser-use](../browsers/browser-use/index.md) (code-as-action over CDP).
* **Stealth browsers** for sites hostile to automation, where permitted: [Camofox](../browsers/camofox/anti-detection.md) (Firefox), [CloakBrowser](../browsers/cloakbrowser/index.md) (Chromium).

## Authentication

Prefer saved storage state or a human logging in once (Camofox VNC, Playwright `--storage-state`) over giving passwords to the model; use domain-scoped secrets ([browser-use](../browsers/browser-use/overview.md)).

## Safety

Pages can contain prompt injection; a browser agent with your session can buy, send or delete. Isolate profiles, allow-list domains, confirm irreversible actions ([Agent security](agent-security.md)). Respect site terms and robots rules.

## Related

[Web scraping & search](web-scraping.md) · [Browser & web alternatives](../browsers/alternatives.md) · [Concepts index](index.md)
