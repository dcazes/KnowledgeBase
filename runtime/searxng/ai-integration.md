---
type: Reference
title: SearXNG — AI Integration
description: How the AI stack consumes SearXNG — Firecrawl via SEARXNG_ENDPOINT, AnythingLLM web-search skill, Hermes/OpenCode/Graphify, and custom Python scripts.
resource: https://docs.searxng.org/dev/search_api.html
tags: [searxng, integration, firecrawl, anythingllm, hermes, opencode, graphify, ai]
generated: { by: "human:daniel", at: "2026-07-08T23:58:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-08T23:58:00Z" } ]
status: stable
stale_after: 2027-01-04
sources:
  - id: search-api
    resource: "https://docs.searxng.org/dev/search_api.html"
    title: "Search API"
    author: "site:docs.searxng.org"
  - id: deployment-installation-md
    resource: "installation.md"
    title: "Deployment - installation.md"
  - id: api-contract-api-md
    resource: "api.md"
    title: "API contract - api.md"
---

# SearXNG — Integration overview

SearXNG is the web-search substrate for this machine's agent stack. Every consumer hits the same HTTP endpoint — `http://127.0.0.1:8088/search?format=json` from the host, or `http://searxng:8080/search?format=json` from inside the Docker `backend` network. See [API](api.md) for the parameter/response contract.

# 1. Firecrawl (native, in-network)

Firecrawl's `api` service already carries `SEARXNG_ENDPOINT`, which **defaults to `http://searxng:8080`** (resolved over the `backend` network). When Firecrawl needs search-backed scraping, it queries your SearXNG instance automatically — no code change needed.

```bash
# verify the wiring from the Firecrawl api container
docker exec firecrawl-api-1 env | grep SEARXNG_ENDPOINT
# expected: SEARXNG_ENDPOINT=http://searxng:8080
```

Optional overrides via Firecrawl's `.env`:
```bash
SEARXNG_ENDPOINT=http://searxng:8080
SEARXNG_ENGINES=google,bing,duckduckgo
SEARXNG_CATEGORIES=general,news
```

# 2. AnythingLLM (web-search skill)

AnythingLLM can call SearXNG as a generic web-search provider.

**Configure (Settings → Agents → Skills → Web Search):**
```
Provider:        Custom / Generic
API Endpoint:    http://127.0.0.1:8088/search
Query Parameter: q
Format:          json
Auth:            None
Max Results:     10
Timeout:         10s
```

**Custom skill (Python) — drop into AnythingLLM's skills dir:**
```python
import requests

def searxng_search(query, max_results=10, categories=""):
    """Search via local SearXNG. Returns trimmed result list."""
    params = {"q": query, "format": "json", "pageno": 1}
    if categories:
        params["categories"] = categories
    r = requests.get("http://127.0.0.1:8088/search", params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    return [
        {"title": x.get("title"), "url": x.get("url"),
         "content": x.get("content", "")[:300], "engine": x.get("engine")}
        for x in data.get("results", [])[:max_results]
    ]
```
Usage in chat: `@searxng_search query="docker UID 1000" categories="general,code"`.

# 3. Hermes (terminal / skill)

Hermes reaches SearXNG over HTTP from the host loopback.

**One-liner:**
```bash
curl -s "http://127.0.0.1:8088/search?q=docker+permissions&format=json"
```

**Reusable Python helper (mirrors [api.md](api.md)):**
```python
import requests

def searxng_search(query, categories=None, max_results=10,
                    base="http://127.0.0.1:8088/search"):
    params = {"q": query, "format": "json", "pageno": 1}
    if categories:
        params["categories"] = ",".join(categories)
    r = requests.get(base, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    return {"query": data.get("query"),
            "total": data.get("number_of_results"),
            "results": data.get("results", [])[:max_results]}
```

# 4. OpenCode (skill / script)

OpenCode can call the same endpoint from a project skill. JavaScript example:
```javascript
export async function searxngSearch(query, { categories = [], maxResults = 10 } = {}) {
  const params = new URLSearchParams({ q: query, format: "json", pageno: "1" });
  if (categories.length) params.append("categories", categories.join(","));
  const res = await fetch(`http://127.0.0.1:8088/search?${params}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const data = await res.json();
  return data.results.slice(0, maxResults).map(r => ({
    title: r.title, url: r.url, snippet: r.content, engine: r.engine,
  }));
}
```

# 5. Graphify (URL ingestion)

Pipe result URLs into Graphify to grow the knowledge graph:
```bash
QUERY="Graphify knowledge graph documentation"
urls=$(curl -s "http://127.0.0.1:8088/search?q=$QUERY&format=json" \
  | python3 -c "import sys,json; print('\n'.join(r['url'] for r in json.load(sys.stdin)['results'][:5]))")
for url in $urls; do
  graphify add "$url"
done
```

# 6. Custom Python scripts (standalone)

```python
#!/usr/bin/env python3
import sys, requests

def main():
    query = " ".join(sys.argv[1:]) or "docker permissions"
    r = requests.get("http://127.0.0.1:8088/search",
                     params={"q": query, "format": "json"}, timeout=10)
    r.raise_for_status()
    for i, x in enumerate(r.json().get("results", [])[:10], 1):
        print(f"{i}. {x['title']} ({x['engine']})\n   {x['url']}\n")

if __name__ == "__main__":
    main()
```

# Architecture

```
Host loopback / Docker backend network
            │
            ▼
     SearXNG  (:8088 / searxng:8080)
            ▲              ▲
   host consumers    in-network consumers
   ┌────────┐        ┌──────────────┐
   │Hermes  │        │ Firecrawl    │ (SEARXNG_ENDPOINT)
   │OpenCode│        │ api service  │
   │Graphify│        └──────────────┘
   │AnythingLLM (via 127.0.0.1:8088)
   └────────┘
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Firecrawl can't reach SearXNG | wrong network / endpoint | Confirm `searxng` on `backend`; `SEARXNG_ENDPOINT=http://searxng:8080` |
| 403 from API | `format` not enabled | Enable `json` in `search.formats` (already on) |
| Host tool gets connection refused | instance down | `docker compose up -d searxng` (see [installation](installation.md)) |
| Empty results | engines disabled | check `/preferences` |
