---
type: Concept
title: SearXNG Overview
description: How SearXNG works — fanning a query out to configured engines, merging and ranking results, categories, the privacy model, and its limits as a search backend for AI.
resource: https://docs.searxng.org
tags: [searxng, overview, metasearch, privacy]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: searxng-docs
    resource: "https://docs.searxng.org"
    title: "SearXNG documentation"
    author: "site:docs.searxng.org"
  - id: searxng-github
    resource: "https://github.com/searxng/searxng"
    title: "searxng/searxng on GitHub"
    author: "site:github.com"
---

# SearXNG — Overview

## How a query flows

1. A user or program sends a query to `/search`, optionally with categories, engines, language and time range.
2. SearXNG sends parallel requests to the enabled engines for those categories.
3. Results are de-duplicated, scored (engine weights, position, how many engines returned them) and merged.
4. The response is rendered as HTML, or returned as JSON, CSV or RSS if enabled.

## Engines and categories

Over 200 engines are grouped into categories such as *general*, *news*, *images*, *videos*, *science*, *it*, *files*, *music* and *social media*. Each engine can be enabled, disabled, weighted or given a timeout in `settings.yml`.

## Privacy model

* No user profiles or tracking cookies; queries are sent from the server, so engines see the server's IP, not yours.
* Results can be proxied (image proxy) so browsing stays private.
* A public instance shares one IP among many users, which is why engines sometimes rate-limit or block it.

## As a backend for AI

SearXNG returns *links and snippets*, not page contents. An agent typically searches with SearXNG, then fetches or scrapes the top pages with a tool like [Firecrawl](../../browsers/firecrawl/index.md), [Crawl4AI](../../browsers/crawl4ai/index.md) or a browser — see [Web scraping & search](../../concepts/web-scraping.md). Heavy automated use can get your server's IP blocked by upstream engines; keep volumes modest and enable only the engines you need.

## Related

[SearXNG index](index.md) · [Configuration](configuration.md) · [AI Integration](ai-integration.md)
