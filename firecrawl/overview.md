---
type: Software
title: Firecrawl — Overview
description: Open-source web context API (search/scrape/crawl/extract/agent) that turns web pages into LLM-ready Markdown/JSON; self-hosted here as a 6-service Docker stack.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, web-scraping, scraping, extraction, rag, agents, self-hosted]
timestamp: 2026-07-09T00:30:00Z
---

# What Firecrawl is

Firecrawl is an open-source **web context API**: you give it a URL or query, and it returns clean, LLM-ready output — Markdown, structured JSON, screenshots, or extracted fields. It handles the hard parts of web data: JS-heavy pages, rotating proxies, rate limits, and bot detection (on the hosted cloud; self-hosted has caveats — see [Self-Hosting](self-hosting.md)).

Headline capabilities (from upstream README):
- **Industry-leading reliability** — covers ~96% of the web including JS-heavy pages.
- **Fast** — P95 ~3.4s across millions of pages.
- **LLM-ready output** — clean markdown/JSON/screenshots, fewer tokens.
- **Agent-ready** — single command to connect any agent or MCP client.
- **Actions** — click/scroll/type/wait before extracting.
- **Media parsing** — PDF, DOCX, etc.

# Core endpoints (v2)

| Endpoint | Does |
|----------|------|
| `/v2/scrape` | Convert one URL → markdown/HTML/screenshot/JSON |
| `/v2/search` | Search the web, return result content |
| `/v2/crawl` | Scrape all URLs of a site in one request |
| `/v2/map` | Discover all URLs on a site instantly |
| `/v2/batch-scrape` | Scrape thousands of URLs asynchronously |
| `/v2/extract` | Structured field extraction (needs AI key) |
| `/v2/agent` | Describe a goal; automated data gathering |
| `/v2/parse` | Parse/upload a file (PDF/DOCX) |

See [API Reference](api-reference.md) for request/response shapes.

# Architecture (self-hosted)

```
client (agent / script / SDK)
        │  HTTP :3002
        ▼
   ┌─────────────────────────────┐
   │  api  (Node/TS, firecrawl-scraper-js)   ← orchestrator + workers
   └───┬───────┬──────────┬───────┘
       │       │          │
       ▼       ▼          ▼
   redis    rabbitmq   nuq-postgres / foundationdb   (queue + state)
       ▲                   │
       │                   ▼
   playwright-service  (browser rendering via Playwright)
       ▲
       │  SEARXNG_ENDPOINT
   SearXNG  (search backend, http://searxng:8080)
```

The `api` container fans work to background workers; jobs move through Redis (cache/rate-limit), RabbitMQ (AMQP queue), and either NUQ-Postgres or FoundationDB (job/state store). Browser rendering is delegated to `playwright-service`.

# Why it's here

In your stack, Firecrawl is the **extraction engine**: agents call its API (or MCP) to pull clean web content, and it uses your **SearXNG** instance for the `/search` backend. This keeps scraping centralized, reliable, and private (self-hosted).

# Licensing / product

- Firecrawl is open source (Mendable product). Self-hosted instances lack Fire-engine (advanced anti-bot) — see [Self-Hosting](self-hosting.md).
- Hosted cloud also available at firecrawl.dev.

# Citations

[1] [Firecrawl GitHub](https://github.com/firecrawl/firecrawl)
[2] [Feature overview (README)](https://github.com/firecrawl/firecrawl#feature-overview)
[3] [Self-hosting limitations](https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md)
