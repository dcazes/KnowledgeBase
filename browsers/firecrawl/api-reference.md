---
type: Reference
title: Firecrawl API Reference
description: Firecrawl v2 REST endpoints — search, scrape, crawl and crawl status, map, batch scrape, extract — with the most-used parameters and authentication.
resource: https://docs.firecrawl.dev/api-reference/introduction
tags: [firecrawl, api, rest, v2]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: firecrawl-docs
    resource: "https://docs.firecrawl.dev"
    title: "Firecrawl documentation"
    author: "site:docs.firecrawl.dev"
---

# Firecrawl — API Reference (v2)

Base URL: `https://api.firecrawl.dev/v2` (cloud) or `http://localhost:3002/v2` (self-hosted). Auth: `Authorization: Bearer fc-...` (self-hosted with `USE_DB_AUTHENTICATION=false` accepts any value).

| Method & path | Purpose | Key parameters |
|---|---|---|
| `POST /search` | Search + optional scrape of results | `query`, `limit`, `sources` (web, news, images), `scrapeOptions` |
| `POST /scrape` | Scrape one URL | `url`, `formats`, `onlyMainContent`, `actions`, `waitFor`, `location`, `maxAge` (cache) |
| `POST /crawl` | Start a crawl job | `url`, `limit`, `maxDiscoveryDepth`, `includePaths`, `excludePaths`, `scrapeOptions`, `webhook` |
| `GET /crawl/{id}` | Crawl status and results | paginated `next` |
| `POST /map` | List a site's URLs | `url`, `search`, `limit` |
| `POST /batch/scrape` | Scrape many URLs async | `urls`, `scrapeOptions` |
| `POST /extract` | Structured extraction across URLs | `urls`, `prompt`, `schema` |

`formats` may include objects such as `{"type": "json", "schema": {...}}` or `{"type": "screenshot", "fullPage": true}`.

## Related

[Firecrawl index](index.md) · [Snippets](snippets.md) · [CLI](cli.md)
