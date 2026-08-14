---
type: Reference
title: SearXNG — Search API
description: The programmatic /search endpoint (JSON/CSV/RSS) — parameters, response schema, and copy-paste curl + Python examples for the AI stack.
resource: https://docs.searxng.org/dev/search_api.html
tags: [searxng, api, json, csv, rss, programmatic, search-api]
generated: { by: "human:daniel", at: "2026-07-08T23:50:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-08T23:50:00Z" } ]
status: stable
stale_after: 2027-01-04
sources:
  - id: search-api
    resource: "https://docs.searxng.org/dev/search_api.html"
    title: "Search API"
    author: "site:docs.searxng.org"
  - id: local-settings-formats-programs-firecrawl-firecrawl-searxng-config-settings-yml
    resource: "/../../programs/firecrawl/firecrawl/searxng-config/settings.yml"
    title: "Local settings (formats) - programs/firecrawl/firecrawl/searxng-config/settings.yml"
  - id: deployment-installation-md
    resource: "installation.md"
    title: "Deployment - installation.md"
---

# Overview

SearXNG exposes its results over HTTP. The web UI hits `/search` as a normal page; programs request the same endpoint with `format=json` (or `csv`/`rss`) to get machine-readable output. This is how Firecrawl, AnythingLLM, Hermes, OpenCode, and custom scripts consume it.

Your instance: `http://127.0.0.1:8088/search` (container listens on `8080`; published on host `8088`).

> **403 rule:** the requested `format` must be listed in `search.formats` in `settings.yml`. Your instance enables `html`, `json`, `csv` — so `format=json` and `format=csv` work; `format=rss` will 403 (RSS not enabled). See [Configuration](configuration.md).

# HTTP method

* **GET** — parameters as URL query string (simplest for curl/scripts).
* **POST** — parameters as form data (`application/x-www-form-urlencoded`).

Both return identical results; choose based on client convenience.

# Query parameters

| Parameter | Required | Default | Values | Meaning |
|-----------|----------|---------|--------|---------|
| `q` | ✅ | — | string | The search query (supports [syntax](syntax.md): `!engine`, `site:`, quotes, `-term`). |
| `categories` | ❌ | all | comma list | Active categories, e.g. `general,code,news`. |
| `language` | ❌ | `auto` | lang code | `en`, `es`, `fr`, `de`, `ja`, … |
| `pageno` | ❌ | `1` | int | Result page number. |
| `time_range` | ❌ | — | `day`, `month`, `year` | Time filter (engines that support it). |
| `format` | ❌* | `html` | `json`, `csv`, `rss` | Output format. **Required for API use.** |
| `safesearch` | ❌ | from settings | `0`, `1`, `2` | Off / moderate / strict. |

\* `format` is optional for human HTML, but **mandatory** for programmatic use — and must be enabled in `settings.yml`.

# Response schema (JSON)

```json
{
  "query": "docker permissions",
  "number_of_results": 47,
  "results": [
    {
      "title": "Docker Container Permissions",
      "url": "https://example.com/docker-permissions",
      "content": "Understanding UID/GID alignment in containers...",
      "engine": "google",
      "category": "general",
      "score": 100,
      "publishedDate": null,
      "pretty_url": "https://example.com/docker-permissions"
    }
  ]
}
```

Key fields per result: `title`, `url`, `content` (snippet), `engine`, `category`, `score`. CSV output flattens the same into columns; RSS emits `<item>` entries.

# Examples

## cURL

```bash
# JSON
curl "http://127.0.0.1:8088/search?q=docker+permissions&format=json"

# Code category only, English
curl "http://127.0.0.1:8088/search?q=graphify+mcp&format=json&categories=code"

# Time-filtered news
curl "http://127.0.0.1:8088/search?q=AI+regulation&format=json&categories=news&time_range=day"

# POST form
curl -X POST "http://127.0.0.1:8088/search" -d "q=docker&format=json"
```

## Python (reusable helper)

```python
import requests

def searxng_search(query, categories=None, language="auto", max_results=10,
                    base="http://127.0.0.1:8088/search"):
    """Query SearXNG and return trimmed result dicts."""
    params = {"q": query, "format": "json", "language": language, "pageno": 1}
    if categories:
        params["categories"] = ",".join(categories)
    r = requests.get(base, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    return {
        "query": data.get("query"),
        "total": data.get("number_of_results"),
        "results": [
            {
                "title": x.get("title"),
                "url": x.get("url"),
                "content": x.get("content", "")[:300],
                "engine": x.get("engine"),
                "category": x.get("category"),
            }
            for x in data.get("results", [])[:max_results]
        ],
    }

if __name__ == "__main__":
    out = searxng_search("docker UID 1000", categories=["general", "code"], max_results=5)
    for i, r in enumerate(out["results"], 1):
        print(f"{i}. {r['title']} ({r['engine']})\n   {r['url']}\n")
```

## Inspect which engines answered

```bash
curl -s "http://127.0.0.1:8088/search?q=test&format=json" \
  | python3 -c "import sys,json; print(set(r['engine'] for r in json.load(sys.stdin)['results']))"
```

# Programmatic use cases in this stack

* **Firecrawl** — `SEARXNG_ENDPOINT=http://searxng:8080` (on the `backend` network) lets Firecrawl use SearXNG for search-backed scraping. See [AI Integration](ai-integration.md).
* **AnythingLLM / Hermes / OpenCode** — call `/search?format=json` directly for grounded web lookups.
* **Graphify** — pipe result URLs into `graphify add <url>` to grow the knowledge graph.

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `403 Forbidden` | `format` not enabled in `settings.yml` | Add it under `search.formats` (json/csv already on for you) |
| Empty `results` | All engines disabled / no egress | Check `/preferences`; test outbound connectivity |
| Slow (>5 s) | Too many engines queried | Narrow `categories` |
| CAPTCHA from Google | Over-querying | Disable Google in config; rely on DDG/Bing |
