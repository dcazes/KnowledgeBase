---
type: Playbook
title: CloakBrowser AI Integration
description: Using CloakBrowser as the browser under AI agents and scrapers — plugging it into Playwright-based tools such as browser-use and Crawl4AI, composable launch helpers, and safety considerations.
resource: https://github.com/CloakHQ/CloakBrowser
tags: [cloakbrowser, integration, agents, browser-use, crawl4ai]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cloakbrowser-github
    resource: "https://github.com/CloakHQ/CloakBrowser"
    title: "CloakHQ/CloakBrowser on GitHub"
    author: "site:github.com"
---

# CloakBrowser — AI Integration

Because CloakBrowser *is* Playwright (or Puppeteer) underneath, any agent or scraper that accepts a Playwright browser, a Chromium executable path or a CDP endpoint can run on it:

* [browser-use](../browser-use/index.md) and [Crawl4AI](../crawl4ai/index.md) — point them at the CloakBrowser binary or an already-launched browser.
* Custom [PydanticAI](../../agents/pydanticAI/index.md) / [LangGraph](../../agents/langgraph/index.md) tools that wrap Playwright pages.
* JS helpers `buildLaunchOptions()` and `humanizeBrowser()` compose with your own Playwright setup.

It is a library, not a server: if you want an HTTP or MCP browser service for agents, see [Camofox](../camofox/index.md) or [Playwright MCP](../playwright-mcp/index.md).

> Use anti-detection browsers only where you are allowed to automate: your own sites, sites whose terms permit it, or authorised testing. Bypassing access controls can breach terms of service or law.

## Related

[CloakBrowser index](index.md) · [Browser automation](../../concepts/browser-automation.md) · [Agent security](../../concepts/agent-security.md)
