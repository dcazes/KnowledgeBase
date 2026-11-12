---
type: Software
title: Firecrawl
description: Web context API for AI agents — search, scrape, crawl, map, interact and extract the web into clean Markdown or structured JSON, with document parsing, an MCP server, CLI and SDKs. Open source (AGPL-3.0) and hosted.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, web-scraping, crawling, markdown, mcp, typescript]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: firecrawl-github
    resource: "https://github.com/firecrawl/firecrawl"
    title: "firecrawl/firecrawl on GitHub"
    author: "site:github.com"
  - id: firecrawl-docs
    resource: "https://docs.firecrawl.dev"
    title: "Firecrawl documentation"
    author: "site:docs.firecrawl.dev"
  - id: firecrawl-selfhost
    resource: "https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md"
    title: "Self-hosting Firecrawl"
    author: "site:github.com"
---

# Firecrawl

**Firecrawl** turns websites into LLM-ready data. Give it a URL and it returns clean Markdown, HTML, screenshots or schema-shaped JSON, handling JavaScript rendering, rate limits and (in the cloud) proxies. It also searches the web, crawls whole sites, maps URLs and lets an agent click through pages. It is one of the most-starred projects in AI tooling.

| | |
|---|---|
| Category | [Web scraping & search](../../concepts/web-scraping.md) |
| License | AGPL-3.0 (cloud adds proprietary features) |
| Language | TypeScript (API, workers); SDKs for Python (`firecrawl-py` 4.57), Node, others |
| Self-host release | v2.11.0 (2026-06-19); the hosted API is updated continuously |
| API | v2 — `/search`, `/scrape`, `/crawl`, `/map`, `/batch/scrape`, `/extract`, interact, parse, monitor |

## Contents

* [Overview](overview.md) — endpoints, formats, actions, open source vs cloud
* [API reference](api-reference.md) — v2 endpoints and key parameters
* [CLI](cli.md) — the `firecrawl` command
* [Self-hosting](self-hosting.md) — Compose stack, configuration, security
* [Subservices](subservices/index.md) — API/workers, Playwright, Redis, RabbitMQ, NuQ Postgres, FoundationDB
* [Snippets](snippets.md) — Python, Node, curl
* [AI Integration](ai-integration.md) — MCP server, agent frameworks, RAG pipelines

## Related

* Concepts: [Web scraping & search](../../concepts/web-scraping.md) · [Browser automation](../../concepts/browser-automation.md) · [Document parsing](../../concepts/document-parsing.md) · [MCP](../../concepts/mcp.md)
* Peers: [Crawl4AI](../crawl4ai/index.md), [browser-use](../browser-use/index.md), [Playwright MCP](../playwright-mcp/index.md); search backend [SearXNG](../../runtime/searxng/index.md)
* Comparison: [Browser & web alternatives](../alternatives.md)
