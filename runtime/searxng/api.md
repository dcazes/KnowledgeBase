---
type: Reference
title: SearXNG API
description: The SearXNG /search endpoint for programmatic use — parameters, JSON response fields, pagination, and error cases.
resource: https://docs.searxng.org/dev/search_api.html
tags: [searxng, api, json, rest]
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

# SearXNG — API

`GET` or `POST /search` (requires `json` in `search.formats` — see [Configuration](configuration.md)).

| Parameter | Meaning |
|---|---|
| `q` | Query (required) |
| `format` | `json`, `csv`, `rss` (or HTML by default) |
| `categories` | Comma-separated, e.g. `general,science` |
| `engines` | Comma-separated engine names |
| `language` | e.g. `en`, `de`, `auto` |
| `pageno` | Page number, from 1 |
| `time_range` | `day`, `week`, `month`, `year` |
| `safesearch` | `0`, `1`, `2` |

## JSON response (abridged)

```json
{
  "query": "graph rag",
  "number_of_results": 0,
  "results": [
    {"title": "...", "url": "https://...", "content": "snippet...", "engine": "duckduckgo",
     "engines": ["duckduckgo", "brave"], "score": 3.2, "category": "general", "publishedDate": null}
  ],
  "answers": [], "infoboxes": [], "suggestions": ["graphrag microsoft"], "unresponsive_engines": []
}
```

`unresponsive_engines` lists engines that timed out or blocked the request — useful for monitoring.

## Errors

* **403** — JSON format not enabled.
* **429** — the limiter blocked the client; whitelist your app's IP or disable the limiter on private instances.

## Related

[SearXNG index](index.md) · [Snippets](snippets.md)
