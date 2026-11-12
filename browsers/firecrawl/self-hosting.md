---
type: Playbook
title: Firecrawl Self-Hosting
description: Run Firecrawl yourself with Docker Compose — services in the stack, first-run settings, SearXNG search, local LLMs for extraction, proxies, admin routes and security responsibilities.
resource: https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md
tags: [firecrawl, self-hosting, docker, searxng, ollama]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: firecrawl-selfhost
    resource: "https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md"
    title: "Self-hosting Firecrawl"
    author: "site:github.com"
---

# Firecrawl — Self-Hosting

```bash
git clone https://github.com/firecrawl/firecrawl && cd firecrawl
cp apps/api/.env.example .env          # edit
docker compose up -d                   # API on http://localhost:3002
```

## What runs

API and workers, a [Playwright service](subservices/playwright-service.md), [Redis](subservices/redis.md), [RabbitMQ](subservices/rabbitmq.md), [NuQ PostgreSQL](subservices/nuq-postgres.md) and optional [FoundationDB](subservices/foundationdb.md) for the queue. Only the API is published to the host by default.

## First-run settings

| Variable | Purpose |
|---|---|
| `USE_DB_AUTHENTICATION=false` | Skip API-key auth for a first local run; turn auth on before sharing |
| `NUM_WORKERS_PER_QUEUE` | Worker concurrency |
| `PLAYWRIGHT_MICROSERVICE_URL` | Browser rendering service |
| `SEARXNG_ENDPOINT`, `SEARXNG_ENGINES`, `SEARXNG_CATEGORIES` | Use [SearXNG](../../runtime/searxng/index.md) for `/search` |
| `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `MODEL_NAME` | LLM for JSON extraction — any [OpenAI-compatible](../../concepts/openai-compatible-api.md) server |
| `OLLAMA_BASE_URL` | Use [Ollama](../../runtime/ollama/index.md) for extraction |
| `PROXY_SERVER`, `PROXY_USERNAME`, `PROXY_PASSWORD` | Outbound proxy |
| `BULL_AUTH_KEY` | Enables key-protected admin routes and the queue UI |

## Responsibilities

Self-hosting gives you control and makes you responsible for security, capacity, upgrades, data retention and compliance — including respecting sites' terms and robots rules. Keep the API off the public internet unless authentication is on. See [Self-hosting](../../concepts/self-hosting.md).

## Related

[Firecrawl index](index.md) · [Subservices](subservices/index.md) · [Docker Compose](../../runtime/docker/compose.md)
