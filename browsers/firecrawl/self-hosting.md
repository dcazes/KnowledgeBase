---
type: Playbook
title: Firecrawl — Self-Hosting
description: How to run the Firecrawl stack from the local compose, configure .env, wire SearXNG as the search backend, and the known self-host limitations.
resource: https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md
tags: [firecrawl, self-hosting, docker, compose, searxng, deployment]
generated: { by: "human:daniel", at: "2026-07-09T00:40:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:40:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: self-host-md
    resource: "https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md"
    title: "SELF_HOST.md"
    author: "site:github.com"
  - id: local-compose
    resource: "/../../programs/firecrawl/firecrawl/docker-compose.yaml"
    title: "Local compose"
---

# Firecrawl — Prerequisites

* Docker + Docker Compose.
* (Optional) An AI backend for `/extract` and `/agent`: `OPENAI_API_KEY` or `OPENAI_BASE_URL` (e.g. your `:4000` proxy).

# Deploy

The stack lives at `programs/firecrawl/firecrawl/docker-compose.yaml` (includes our added `searxng` service):

```bash
cd programs/firecrawl/firecrawl
docker compose up -d            # all services
docker compose up -d searxng    # just SearXNG (if already have Firecrawl)
docker compose ps
docker compose logs -f api
```

The `api` waits for `rabbitmq` healthy, then starts.

# Environment (`.env`)

Key variables (from `SELF_HOST.md` + the compose `x-common-env`):

```bash
# Required
PORT=3002
HOST=0.0.0.0
USE_DB_AUTHENTICATION=false      # no Supabase auth locally

# AI features (optional)
OPENAI_API_KEY=                 # or set OPENAI_BASE_URL to your :4000 proxy
OPENAI_BASE_URL=http://localhost:4000/v1
MODEL_NAME=...
MODEL_EMBEDDING_NAME=...

# Proxy (optional)
PROXY_SERVER=
PROXY_USERNAME=
PROXY_PASSWORD=

# Search backend — use your SearXNG
SEARXNG_ENDPOINT=http://searxng:8080
SEARXNG_ENGINES=
SEARXNG_CATEGORIES=

# Queue backend (optional switch)
NUQ_BACKEND=                    # leave empty for Postgres; set "fdb" for FoundationDB
```

> The compose already sets `SEARXNG_ENDPOINT` default to `http://searxng:8080` over the `backend` network, so Firecrawl's `/search` uses your SearXNG instance automatically.

# Verify

```bash
# API info
curl -s http://127.0.0.1:3002/ | head -c 200

# Scrape test
curl -X POST http://127.0.0.1:3002/v2/scrape \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","formats":["markdown"]}'

# Search via SearXNG
curl -X POST http://127.0.0.1:3002/v2/search \
  -H 'Content-Type: application/json' \
  -d '{"query":"test","limit":3}'
```

# Limitations (self-hosted)

Per `SELF_HOST.md`:
1. **No Fire-engine** — advanced anti-bot / IP-block handling is a hosted-only feature. Basic fetch + Playwright work; tougher targets may need manual proxy config.
2. **Manual configuration** — scraping methods beyond basic fetch/Playwright need manual `.env` setup.
3. **Search default** — `/search` uses Google by default unless you set `SEARXNG_ENDPOINT` (which we do).

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| API won't start | RabbitMQ not healthy | `docker compose logs rabbitmq` |
| Search fails | SearXNG down | ensure `searxng` service up; check `SEARXNG_ENDPOINT` |
| Extract 403 | no AI key | set `OPENAI_API_KEY` / `OPENAI_BASE_URL` |
| Build needed | using `build:` images | first `up` compiles api/playwright/nuq-postgres |
