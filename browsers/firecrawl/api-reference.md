---
type: Reference
title: Firecrawl — API Reference (v2)
description: The v2 HTTP endpoints — scrape, search, crawl, map, batch-scrape, extract, agent, parse — with request/response examples against the local :3002 instance.
resource: https://github.com/firecrawl/firecrawl/tree/main/apps/api/src/controllers/v2
tags: [firecrawl, api, v2, scrape, search, crawl, extract, reference]
generated: { by: "human:daniel", at: "2026-07-09T00:38:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:38:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: v2-controllers-github
    resource: "https://github.com/firecrawl/firecrawl/tree/main/apps/api/src/controllers/v2"
    title: "v2 controllers (GitHub)"
    author: "site:github.com"
  - id: routes-mount-index-ts
    resource: "https://github.com/firecrawl/firecrawl/blob/main/apps/api/src/index.ts"
    title: "Routes mount (index.ts)"
    author: "site:github.com"
---

# Firecrawl — Base URL

```
http://127.0.0.1:3002/v2      # your self-hosted api (host port 3002)
```

> Self-hosted by default has `USE_DB_AUTHENTICATION=false`, so **no API key is required** for local calls (unlike the hosted cloud which uses `fc-...` keys).

# Scrape — `POST /v2/scrape`

Convert one URL into clean output.

```bash
curl -X POST http://127.0.0.1:3002/v2/scrape \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","formats":["markdown","html"],"onlyMainContent":true}'
```

Response (trimmed):
```json
{ "success": true,
  "data": { "markdown": "...", "html": "...", "metadata": { "title": "..." , "sourceURL": "..." } } }
```

# Search — `POST /v2/search`

Search the web (backed by SearXNG here) and return result content.

```bash
curl -X POST http://127.0.0.1:3002/v2/search \
  -H 'Content-Type: application/json' \
  -d '{"query":"firecrawl knowledge graph","limit":5,"scrapeOptions":{"formats":["markdown"]}}'
```

# Crawl — `POST /v2/crawl`

Scrape all URLs of a site in one request (async; returns a job id).

```bash
curl -X POST http://127.0.0.1:3002/v2/crawl \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","limit":50,"scrapeOptions":{"formats":["markdown"]}}'
# poll: GET /v2/crawl/:id  or  /v2/crawl/:id (status)
```

# Map — `POST /v2/map`

Discover all URLs on a site instantly.

```bash
curl -X POST http://127.0.0.1:3002/v2/map \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com"}'
```

# Batch Scrape — `POST /v2/batch-scrape`

Scrape thousands of URLs asynchronously.

```bash
curl -X POST http://127.0.0.1:3002/v2/batch-scrape \
  -H 'Content-Type: application/json' \
  -d '{"urls":["https://a.com","https://b.com"],"scrapeOptions":{"formats":["markdown"]}}'
```

# Extract — `POST /v2/extract`

Structured field extraction (needs an AI backend: `OPENAI_API_KEY` or `OPENAI_BASE_URL`).

```bash
curl -X POST http://127.0.0.1:3002/v2/extract \
  -H 'Content-Type: application/json' \
  -d '{"urls":["https://example.com"],
       "prompt":"extract the company name and founding year",
       "schema":{"company": "string", "year": "number"}}'
```

# Agent — `POST /v2/agent`

Describe a goal; Firecrawl gathers the data autonomously.

```bash
curl -X POST http://127.0.0.1:3002/v2/agent \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"find the pricing tiers for firecrawl and summarize them"}'
```

# Parse — `POST /v2/parse`

Parse/upload a file (PDF/DOCX) into extracted content.

```bash
curl -X POST http://127.0.0.1:3002/v2/parse \
  -F 'file=@/path/to/doc.pdf'
```

# Other v2 controllers (catalog)

From `apps/api/src/controllers/v2/`: `scrape-browser`, `f-search`, `crawl-status`, `crawl-cancel`, `crawl-errors`, `crawl-ongoing`, `crawl-status-ws`, `batch-scrape`, `extract-status`, `agent-status`, `agent-cancel`, `browser`, `browser-replay`, `queue-status`, `token-usage`, `credit-usage`, `feedback`, `slack`, `monitor`, `concurrency-check`, `parse-upload`, `research-proxy`, `support-proxy`, `team-threat-protection`, plus v0/v1 routers.

# Status / health

```bash
curl -s http://127.0.0.1:3002/ | head -c 200     # info route
curl -s http://127.0.0.1:3002/v2/queue-status     # queue depth
```
