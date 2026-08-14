---
type: Reference
title: Firecrawl Subservice — API
description: The firecrawl api container — Node/TS orchestrator and workers that expose the /v0 /v1 /v2 HTTP API on port 3002.
resource: https://github.com/firecrawl/firecrawl/tree/main/apps/api
tags: [firecrawl, api, subservice, node, typescript, workers]
generated: { by: "human:daniel", at: "2026-07-09T00:32:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:32:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: apps-api-github
    resource: "https://github.com/firecrawl/firecrawl/tree/main/apps/api"
    title: "apps/api (GitHub)"
    author: "site:github.com"
  - id: local-compose-programs-firecrawl-firecrawl-docker-compose-yaml
    resource: "/../../programs/firecrawl/firecrawl/docker-compose.yaml"
    title: "Local compose - programs/firecrawl/firecrawl/docker-compose.yaml"
---

# Role

The `api` service is the **brain** of the stack: it serves the HTTP API, orchestrates scrape/crawl/search jobs, and runs the background workers that actually do the work. Built from `apps/api` (package `firecrawl-scraper-js`).

# Image & runtime

* Built from `apps/api` (or `ghcr.io/firecrawl/firecrawl` if using prebuilt images).
* Command: `node dist/src/harness.js --start-docker`.
* Listens on `HOST:PORT` (default `0.0.0.0:3002`; `INTERNAL_PORT=3002`).
* Resource limits in compose: `cpus: 4.0`, `mem_limit: 8G`.

# HTTP surface

The server mounts three routers (from `apps/api/src/index.ts`):
```
app.use(v0Router);
app.use("/v1", v1Router);
app.use("/v2", v2Router);
```
Plus `/admin/<BULL_AUTH_KEY>/queues` (BullMQ dashboard) and a `/` health/info route.

v2 controllers include: `scrape`, `scrape-browser`, `search`, `f-search`, `crawl`, `crawl-status`, `crawl-cancel`, `map`, `batch-scrape`, `extract`, `agent`, `parse`, `browser`, `queue-status`, `token-usage`, and more. See [API Reference](../api-reference.md).

# Workers

The api container also runs the queue workers (same image, different process):
- `queue-worker` / `nuq-worker` / `nuq-fdb-worker` / `extract-worker` / `index-worker` / `zdr-worker` / `cclog-worker` / `nuq-prefetch-worker` / `nuq-reconciler-worker`.

# Key environment

| Var | Default | Purpose |
|-----|---------|---------|
| `PORT` / `INTERNAL_PORT` | 3002 | Listen port |
| `HOST` | 0.0.0.0 | Bind host |
| `REDIS_URL` | redis://redis:6379 | cache + rate-limit |
| `REDIS_RATE_LIMIT_URL` | redis://redis:6379 | rate limiting |
| `NUQ_RABBITMQ_URL` | amqp://rabbitmq:5672 | job queue |
| `POSTGRES_*` | nuq-postgres:5432 | job/state store |
| `PLAYWRIGHT_MICROSERVICE_URL` | http://playwright-service:3000/scrape | browser rendering |
| `SEARXNG_ENDPOINT` | http://searxng:8080 | search backend |
| `OPENAI_API_KEY` / `OPENAI_BASE_URL` / `MODEL_NAME` | — | AI features (extract/agent) |
| `USE_DB_AUTHENTICATION` | false | Supabase auth (off by default) |
| `NUQ_BACKEND` | — | `fdb` to use FoundationDB instead of Postgres |

# Depends on

```
depends_on:
  redis:        service_started
  playwright-service: service_started
  rabbitmq:     service_healthy
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| API won't start | RabbitMQ not healthy | `docker compose logs rabbitmq` |
| 503 / queue errors | Redis/Postgres down | check those services |
| AI features 403 | no `OPENAI_API_KEY` | set key or `OPENAI_BASE_URL` |
| Search empty | SearXNG down / wrong endpoint | verify `SEARXNG_ENDPOINT` + SearXNG up |
