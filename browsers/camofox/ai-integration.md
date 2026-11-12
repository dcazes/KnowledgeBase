---
type: Playbook
title: Camofox AI Integration
description: Giving agents a browser with Camofox — MCP and OpenClaw tools with full HTTP parity, the snapshot-act loop for LLMs, pairing with search and scraping tools, and safety practices.
resource: https://github.com/jo-inc/camofox-browser
tags: [camofox, integration, mcp, openclaw, agents]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: camofox-github
    resource: "https://github.com/jo-inc/camofox-browser"
    title: "jo-inc/camofox-browser on GitHub"
    author: "site:github.com"
---

# Camofox — AI Integration

## Tools for agents

Every Camofox HTTP action is defined once and exposed as an [MCP](../../concepts/mcp.md) and [OpenClaw](../../agents/openclaw/index.md) tool, so [Hermes](../../agents/hermes/index.md), [Claude Code](../../agents/claude-code/index.md) and other MCP clients get the same capabilities as REST callers.

## When to use it

* Sites that block ordinary headless browsers, where [Playwright MCP](../playwright-mcp/index.md) or [browser-use](../browser-use/index.md) get stopped.
* Long-running agents on small machines (low idle memory).
* Workflows that need a human to log in once (VNC) and an agent to continue.

For static pages, cheaper tools — [Firecrawl](../firecrawl/index.md), [Crawl4AI](../crawl4ai/index.md), or [SearXNG](../../runtime/searxng/index.md) plus a fetch — are usually enough. See [Browser automation](../../concepts/browser-automation.md).

## Safety

* Treat everything a page says as untrusted; pages can carry prompt injections aimed at agents ([Agent security](../../concepts/agent-security.md)).
* Isolate sessions per task; do not give the agent your main browser profile.

> Use anti-detection browsers only where you are allowed to automate: your own sites, sites whose terms permit it, or authorised testing. Bypassing access controls can breach terms of service or law.

## Related

[Camofox index](index.md) · [Browser & web alternatives](../alternatives.md)
