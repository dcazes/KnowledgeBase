---
type: Reference
title: Firecrawl Subservice — Playwright Service
description: The playwright-service container — a standalone Playwright browser-rendering microservice the api delegates JS-heavy page rendering to.
resource: https://github.com/firecrawl/firecrawl/tree/main/apps/playwright-service-ts
tags: [firecrawl, playwright, subservice, browser, rendering, scraping]
generated: { by: "human:daniel", at: "2026-07-09T00:33:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:33:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: apps-playwright-service-ts-github
    resource: "https://github.com/firecrawl/firecrawl/tree/main/apps/playwright-service-ts"
    title: "apps/playwright-service-ts (GitHub)"
    author: "site:github.com"
  - id: local-compose
    resource: "/../../programs/firecrawl/firecrawl/docker-compose.yaml"
    title: "Local compose"
---

# Role

`playwright-service` is a **separate browser-rendering microservice**. When the api needs to render or interact with a JavaScript-heavy page, it calls this service instead of embedding a browser in the api process. This isolates browser resource usage (and crashes) from the API.

# Image & runtime

* Built from `apps/playwright-service-ts` (package `playwright-scraper-api`).
* Express server (`api.ts`), default `PORT=3000`.
* Scrape endpoint: `/scrape` (referenced by the api via `PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/scrape`).
* Uses `playwright ^1.58`, `proxy-chain` (for authenticated proxies), `user-agents`.
* Resource limits in compose: `cpus: 2.0`, `mem_limit: 4G`.
* `tmpfs: /tmp/.cache` (noexec, nosuid, 1g) for browser temp.

# Configuration (env)

| Var | Purpose |
|-----|---------|
| `PORT` | listen port (3000) |
| `PROXY_SERVER` / `PROXY_USERNAME` / `PROXY_PASSWORD` | upstream proxy for renders |
| `ALLOW_LOCAL_WEBHOOKS` | permit local webhook targets |
| `BLOCK_MEDIA` | block images/media during render (speed) |
| `MAX_CONCURRENT_PAGES` | browser concurrency (defaults from `CRAWL_CONCURRENT_REQUESTS`) |

# How the api uses it

The api's `PLAYWRIGHT_MICROSERVICE_URL` points here. Any scrape that requires a real browser (JS execution, interactions, screenshots) is forwarded to this service.

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Browser renders fail | service down | `docker compose restart playwright-service` |
| Slow renders | `MAX_CONCURRENT_PAGES` too low | raise it |
| Blocked by target | no proxy set | configure `PROXY_SERVER` |
