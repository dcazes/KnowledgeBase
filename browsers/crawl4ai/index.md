---
type: Software
title: Crawl4AI
description: Open-source, LLM-friendly web crawler and scraper in Python — async Playwright crawling to clean Markdown, CSS/XPath and LLM-based structured extraction, deep crawling, sessions and hooks, plus a Docker server and a hosted cloud API with MCP.
resource: https://github.com/unclecode/crawl4ai
tags: [crawl4ai, web-scraping, crawling, markdown, python, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: crawl4ai-github
    resource: "https://github.com/unclecode/crawl4ai"
    title: "unclecode/crawl4ai on GitHub"
    author: "site:github.com"
  - id: crawl4ai-docs
    resource: "https://docs.crawl4ai.com"
    title: "Crawl4AI documentation"
    author: "site:docs.crawl4ai.com"
---

# Crawl4AI

**Crawl4AI** is a Python crawler built for feeding LLMs: point it at URLs and get clean, fit-for-context Markdown or structured JSON. It is the most popular fully open-source alternative to [Firecrawl](../firecrawl/index.md), and since 2026 also offers a hosted cloud API.

| | |
|---|---|
| Category | [Web scraping & search](../../concepts/web-scraping.md) |
| License | Apache-2.0 (library and self-hosted server) |
| Language | Python (`crawl4ai`) |
| Latest release | v0.9.5 (2026-10-14) |
| Modes | Library · Docker server · Crawl4AI Cloud (`api.crawl4ai.com`, hosted MCP) |

## Contents

* [Overview](overview.md) — features and how it compares with Firecrawl
* [Installation](installation.md) — pip, browser setup, Docker, cloud
* [Snippets](snippets.md) — crawl, extract, deep crawl
* [AI Integration](ai-integration.md) — RAG ingestion, agents, MCP

## Related

* Concepts: [Web scraping & search](../../concepts/web-scraping.md) · [RAG](../../concepts/rag.md) · [Structured output](../../concepts/structured-output.md)
* Peers: [Firecrawl](../firecrawl/index.md), [browser-use](../browser-use/index.md), [Playwright MCP](../playwright-mcp/index.md); stealth browsers [CloakBrowser](../cloakbrowser/index.md)
* Comparison: [Browser & web alternatives](../alternatives.md)
