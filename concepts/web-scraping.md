---
type: Concept
title: Web Scraping & Search for AI
description: Getting web content into LLMs — search APIs and metasearch, scraping to Markdown, crawling sites, structured extraction, JavaScript rendering, the search-then-read agent loop, and responsible scraping.
resource: https://docs.searxng.org
tags: [concept, web-scraping, search, crawling, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: searxng
    resource: "https://docs.searxng.org"
    title: "SearXNG documentation"
    author: "site:docs.searxng.org"
  - id: firecrawl
    resource: "https://docs.firecrawl.dev"
    title: "Firecrawl documentation"
    author: "site:docs.firecrawl.dev"
---

# Web Scraping & Search for AI

Models need fresh information from the web. That splits into **search** (which pages?) and **extraction** (what do they say?), usually combined in a loop.

## Search

* Self-hosted metasearch: [SearXNG](../runtime/searxng/index.md) — private, free, JSON API.
* Search that also returns page content: [Firecrawl](../browsers/firecrawl/index.md) `/search`, Crawl4AI Cloud `/search`.
* Hosted AI search APIs: Brave, Tavily, Exa, Serper, provider-native web search tools.

## Extraction

| Need | Tool |
|---|---|
| One page → clean Markdown | [Firecrawl](../browsers/firecrawl/index.md), [Crawl4AI](../browsers/crawl4ai/index.md), Jina Reader |
| Whole site | Firecrawl crawl/map, Crawl4AI deep crawl |
| Structured fields | JSON-schema extraction ([Structured output](structured-output.md)) |
| Interaction needed | [Browser automation](browser-automation.md) |
| Documents linked from pages | [Docling](../ingestion/docling/index.md), [MarkItDown](../ingestion/markitdown/index.md) |

## The search-then-read loop

1. Search → candidate URLs.
2. Fetch and clean the top results.
3. Put relevant passages in context (on-the-fly [RAG](rag.md)) and cite them.
4. Repeat with refined queries if needed — "deep research".

## Responsible scraping

Respect robots rules and terms of service, rate-limit, cache, and avoid personal data. Treat all fetched content as untrusted input ([Agent security](agent-security.md)).

## Related

[Browser automation](browser-automation.md) · [Browser & web alternatives](../browsers/alternatives.md) · [Concepts index](index.md)
