---
type: Concept
title: Hermes Agent Browser
description: Web capabilities in Hermes — search and page extraction tools, a cloud browser via the Nous tool gateway, local browser options, and MCP browser servers.
resource: https://hermes-agent.nousresearch.com/docs/user-guide/features/tools
tags: [hermes, browser, web, tools]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hermes-docs
    resource: "https://hermes-agent.nousresearch.com/docs/"
    title: "Hermes Agent documentation"
    author: "site:hermes-agent.nousresearch.com"
---

# Hermes Agent — Browser

Hermes reaches the web in layers (see [Browser automation](../../concepts/browser-automation.md)):

* **Web search and extract** tools for quick research, which can be backed by providers or a self-hosted [SearXNG](../../runtime/searxng/index.md) and [Firecrawl](../../browsers/firecrawl/index.md).
* **Browser tools** for interactive pages — a cloud browser through the Nous Portal tool gateway (Browser Use), or a local browser.
* **MCP browser servers** such as [Playwright MCP](../../browsers/playwright-mcp/index.md) or [Camofox](../../browsers/camofox/index.md).

Web content is untrusted: keep command approval on when the agent browses ([Agent security](../../concepts/agent-security.md)).

## Related

[Hermes index](index.md) · [Browser & web alternatives](../../browsers/alternatives.md)
