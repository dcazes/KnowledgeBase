---
type: Playbook
title: SearXNG AI Integration
description: Using SearXNG as the web-search tool for AI — Open WebUI web search, Firecrawl's search backend, SurfSense and AnythingLLM, agent tools and MCP servers, and the search-then-scrape pattern.
resource: https://docs.searxng.org
tags: [searxng, integration, open-webui, firecrawl, mcp, agents]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: searxng-docs
    resource: "https://docs.searxng.org"
    title: "SearXNG documentation"
    author: "site:docs.searxng.org"
---

# SearXNG — AI Integration

## Where it plugs in

| Tool | Setting |
|---|---|
| [Open WebUI](../../apps/openwebui/index.md) | Web search engine `searxng`, query URL `http://searxng:8080/search?q=<query>` |
| [Firecrawl](../../browsers/firecrawl/index.md) | `SEARXNG_ENDPOINT` makes `/search` use SearXNG instead of a paid provider |
| [SurfSense](../../browsers/surfsense/index.md) | Bundles SearXNG as its web-search connector |
| [AnythingLLM](../../apps/anythingllm/index.md), [Dify](../../agents/dify/index.md), [n8n](../../apps/n8n/index.md) | SearXNG search tool / node |
| [Hermes](../../agents/hermes/index.md), coding agents | Community SearXNG [MCP](../../concepts/mcp.md) servers or a small HTTP tool |

## Search, then read

Snippets alone rarely answer a question. The common agent loop:

1. `web_search(query)` via SearXNG → top URLs.
2. Fetch and clean pages with [Firecrawl](../../browsers/firecrawl/index.md), [Crawl4AI](../../browsers/crawl4ai/index.md) or a browser tool.
3. Put the cleaned text into context (a small, on-the-fly [RAG](../../concepts/rag.md)).
4. Cite URLs in the answer.

## Tips

* Enable the JSON format, disable the limiter for private instances, shorten timeouts.
* Restrict categories for specialised agents (e.g. `science` for research, `it` for coding).
* Treat page content as untrusted input — web pages can contain prompt injections ([Agent security](../../concepts/agent-security.md)).

## Related

[SearXNG index](index.md) · [Web scraping & search](../../concepts/web-scraping.md)
