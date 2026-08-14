---
type: Reference
title: Firecrawl Subservice — NUQ Postgres
description: The nuq-postgres container — Postgres-backed job and state store for the Firecrawl queue (NUQ backend).
resource: https://github.com/firecrawl/firecrawl/tree/main/apps/nuq-postgres
tags: [firecrawl, postgres, subservice, nuq, queue, state]
generated: { by: "human:daniel", at: "2026-07-09T00:36:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:36:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: apps-nuq-postgres-github
    resource: "https://github.com/firecrawl/firecrawl/tree/main/apps/nuq-postgres"
    title: "apps/nuq-postgres (GitHub)"
    author: "site:github.com"
  - id: local-compose
    resource: "/../../programs/firecrawl/firecrawl/docker-compose.yaml"
    title: "Local compose"
---

# Firecrawl — Role

`nuq-postgres` is the **default job/state store** for Firecrawl's queue ("NUQ" = the queue subsystem). It persists job definitions, statuses, and crawl state so work survives restarts. Wired via `POSTGRES_*` env vars (`POSTGRES_HOST=nuq-postgres`, port 5432).

# Image & runtime

* Built from `apps/nuq-postgres` (ships a `nuq.sql` schema init).
* Env: `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` (default `postgres`/`postgres`/`postgres` in compose).
* Port 5432 (internal; not published to host in the compose).

# Relationship to the queue

```
api ── NUQ_RABBITMQ_URL (amqp) ──> rabbitmq   (message transport)
api ── POSTGRES_* (sql)        ──> nuq-postgres (durable job/state store)
```

RabbitMQ moves the messages; Postgres is the source of truth for job state.

# Alternative: FoundationDB

Set `NUQ_BACKEND=fdb` to use FoundationDB instead of Postgres (see [FoundationDB](foundationdb.md)). With the default (no `NUQ_BACKEND`), Postgres is used.

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Jobs lost / state errors | Postgres down | `docker compose restart nuq-postgres` |
| Schema issues | `nuq.sql` not applied | rebuild the `nuq-postgres` image |
