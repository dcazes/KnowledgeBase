---
type: Hub
title: Firecrawl Subservices
description: The services that make up a self-hosted Firecrawl stack — API and workers, Playwright rendering service, Redis, RabbitMQ, NuQ PostgreSQL queue and optional FoundationDB — and how a scrape flows through them.
resource: https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md
tags: [firecrawl, subservices, architecture, self-hosting]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: firecrawl-selfhost
    resource: "https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md"
    title: "Self-hosting Firecrawl"
    author: "site:github.com"
  - id: firecrawl-compose
    resource: "https://github.com/firecrawl/firecrawl/blob/main/docker-compose.yaml"
    title: "Firecrawl docker-compose.yaml"
    author: "site:github.com"
---

# Firecrawl — Subservices

```
client ──▶ API (:3002) ──enqueue──▶ NuQ queue (Postgres / FoundationDB)
                                         │
                       workers ◀─────────┘ ──▶ Playwright service (JS rendering)
                          │                 └─▶ fetch engine (static pages)
                          ├─ Redis (rate limits, cache, locks)
                          └─ RabbitMQ (job events / messaging)
```

| Service | Role |
|---|---|
| [API & workers](api.md) | HTTP API plus queue workers that scrape, crawl and post-process |
| [Playwright service](playwright-service.md) | Headless Chromium for JavaScript-heavy pages and actions |
| [Redis](redis.md) | Rate limiting, caching and coordination |
| [RabbitMQ](rabbitmq.md) | Message broker for job events |
| [NuQ PostgreSQL](nuq-postgres.md) | Default durable job queue |
| [FoundationDB](foundationdb.md) | Optional queue backend for larger deployments |

## Related

[Firecrawl index](../index.md) · [Self-hosting](../self-hosting.md) · [Docker Compose](../../../runtime/docker/compose.md)
