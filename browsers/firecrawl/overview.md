---
type: Concept
title: Firecrawl Overview
description: What Firecrawl does — search, scrape, interact, crawl, map, batch scrape, extract, parse and monitor; output formats; page actions; and differences between the open-source and cloud editions.
resource: https://docs.firecrawl.dev
tags: [firecrawl, overview, scraping, crawling, extraction]
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
---

# Firecrawl — Overview

## Endpoints

| Feature | What it does |
|---|---|
| **Search** | Web search that returns full page content for results, not just links |
| **Scrape** | One URL → Markdown, HTML, links, screenshot or JSON |
| **Interact** | After a scrape, drive the page with natural-language prompts or code (search boxes, clicks, pagination) |
| **Crawl** | Follow links across a site, with depth, include/exclude paths and limits |
| **Map** | Discover all URLs on a site quickly |
| **Batch scrape** | Thousands of URLs asynchronously |
| **Extract / JSON format** | Pull structured data that matches a JSON Schema or prompt — [structured output](../../concepts/structured-output.md) for the web |
| **Parse** | PDFs, DOCX and other documents → Markdown or JSON ([document parsing](../../concepts/document-parsing.md)) |
| **Agent** | Describe the data you need; Firecrawl searches and navigates to gather it |
| **Monitor** | Notifications when page content changes |

## Output formats

`markdown` (default, main content only by default), `html`, `rawHtml`, `links`, `screenshot`, `json` (with a schema), `summary` and change tracking.

## Actions

Before extraction a scrape can `click`, `scroll`, `write`, `press` keys and `wait`, which reaches content behind interactions without writing a browser script.

## Open source vs cloud

The AGPL-3.0 code runs the core API and workers. The cloud adds managed proxies and anti-bot handling, higher reliability, the Agent and Alexandria data providers, and other hosted-only features. Self-hosted Firecrawl renders JavaScript with its own Playwright service and uses [SearXNG](../../runtime/searxng/index.md) or other providers for search.

## Related

[Firecrawl index](index.md) · [API reference](api-reference.md) · [Web scraping & search](../../concepts/web-scraping.md)
