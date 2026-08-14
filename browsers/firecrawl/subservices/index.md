---
type: Reference
title: Firecrawl Subservices
description: One topic page per Firecrawl stack container — api, playwright-service, redis, rabbitmq, nuq-postgres, foundationdb.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, subservices, docker, stack]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: firecrawl-github
    resource: "https://github.com/firecrawl/firecrawl"
    title: "Firecrawl GitHub"
    author: "site:github.com"
  - id: self-hosting-docs-self-host-md
    resource: "https://github.com/firecrawl/firecrawl/blob/main/SELF_HOST.md"
    title: "Self-hosting docs (SELF_HOST.md)"
    author: "site:github.com"
  - id: local-stack-programs-firecrawl-firecrawl-docker-compose-yaml
    resource: "/../../programs/firecrawl/firecrawl/docker-compose.yaml"
    title: "Local stack - programs/firecrawl/firecrawl/docker-compose.yaml"
---

# Subservices

Firecrawl's self-hosted stack is a set of cooperating containers. Each gets its own topic page:

* [API](api.md) - the Node/TS orchestrator + workers (the `firecrawl` image, port 3002)
* [Playwright Service](playwright-service.md) - browser rendering microservice
* [Redis](redis.md) - cache + rate-limit store
* [RabbitMQ](rabbitmq.md) - AMQP job queue
* [NUQ Postgres](nuq-postgres.md) - Postgres-backed job/state store
* [FoundationDB](foundationdb.md) - experimental queue backend (NUQ_BACKEND=fdb)

The `searxng` service (added to the same compose) is documented under [SearXNG](../../../runtime/searxng/index.md); it is the search backend, not a Firecrawl subservice.

# How they fit

```
api ──uses──> redis (cache/ratelimit)
api ──publishes/consumes──> rabbitmq (queue)
api ──stores jobs/state──> nuq-postgres  (or foundationdb if NUQ_BACKEND=fdb)
api ──renders via──> playwright-service
api ──searches via──> searxng (SEARXNG_ENDPOINT)
```
