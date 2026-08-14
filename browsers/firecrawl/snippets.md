---
type: Playbook
title: Firecrawl — Snippets & Cheat Sheet
description: Copy-paste commands for deploying the stack, calling the v2 API, using the CLI/SDK, and wiring SearXNG + the :4000 AI proxy.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, snippets, cheat-sheet, api, cli, self-hosting]
generated: { by: "human:daniel", at: "2026-07-09T00:43:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:43:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: api-reference
    resource: "api-reference.md"
    title: "API Reference"
  - id: self-hosting
    resource: "self-hosting.md"
    title: "Self-Hosting"
  - id: cli-skills
    resource: "cli.md"
    title: "CLI & Skills"
---

# Firecrawl — Deploy the stack

```bash
cd programs/firecrawl/firecrawl
docker compose up -d              # all (api, playwright, redis, rabbitmq, nuq-postgres, fdb, searxng)
docker compose ps
docker compose logs -f api
```

# Verify API

```bash
curl -s http://127.0.0.1:3002/ | head -c 200
curl -X POST http://127.0.0.1:3002/v2/scrape -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","formats":["markdown"]}'
```

# v2 API quick calls (no key when USE_DB_AUTHENTICATION=false)

```bash
# Scrape
curl -X POST http://127.0.0.1:3002/v2/scrape -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","formats":["markdown","html"],"onlyMainContent":true}'

# Search (through SearXNG)
curl -X POST http://127.0.0.1:3002/v2/search -H 'Content-Type: application/json' \
  -d '{"query":"firecrawl","limit":5,"scrapeOptions":{"formats":["markdown"]}}'

# Map
curl -X POST http://127.0.0.1:3002/v2/map -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com"}'

# Crawl (async)
curl -X POST http://127.0.0.1:3002/v2/crawl -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","limit":50,"scrapeOptions":{"formats":["markdown"]}}'

# Extract (needs AI backend)
curl -X POST http://127.0.0.1:3002/v2/extract -H 'Content-Type: application/json' \
  -d '{"urls":["https://example.com"],"prompt":"company name and year","schema":{"company":"string","year":"number"}}'
```

# Python SDK

```python
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="")                       # empty for local no-auth
print(app.scrape_url("https://example.com", params={"formats":["markdown"]})["markdown"])
```

# CLI

```bash
export FIRECRAWL_API_URL=http://127.0.0.1:3002
firecrawl scrape https://example.com --formats markdown
firecrawl search "firecrawl graph" --limit 5
```

# Wire AI features to the :4000 proxy

```bash
export OPENAI_BASE_URL=http://localhost:4000/v1
export OPENAI_API_KEY=sk-any-nonempty
# now /extract and /agent work via the cloud failover proxy
```

# SearXNG search backend (already default in compose)

```bash
SEARXNG_ENDPOINT=http://searxng:8080     # compose default; verify:
docker exec firecrawl-api-1 env | grep SEARXNG_ENDPOINT
```

# Switch queue backend to FoundationDB (optional)

```bash
NUQ_BACKEND=fdb docker compose up -d api foundationdb foundationdb-init
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| API won't start | RabbitMQ unhealthy | `docker compose logs rabbitmq` |
| Search empty | SearXNG down | `docker compose up -d searxng` |
| Extract 403 | no AI key | set `OPENAI_BASE_URL` + key |
| Heavy build first run | `build:` images | let `up` compile api/playwright/nuq-postgres |
