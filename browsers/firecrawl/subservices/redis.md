---
type: Reference
title: Firecrawl Subservice — Redis
description: The redis container — cache and rate-limit store used by the Firecrawl api (REDIS_URL / REDIS_RATE_LIMIT_URL).
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, redis, subservice, cache, rate-limit]
generated: { by: "human:daniel", at: "2026-07-09T00:34:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:34:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: local-compose-redis-service
    resource: "/../../programs/firecrawl/firecrawl/docker-compose.yaml"
    title: "Local compose (redis service)"
---

# Firecrawl — Role

Redis backs two things in the Firecrawl stack:
1. **General cache** (`REDIS_URL`) — short-term caching of scrape/search results.
2. **Rate limiting** (`REDIS_RATE_LIMIT_URL`) — throttling per key/IP.

It is a standard `redis:alpine` container; no custom build.

# Configuration (api env)

```
REDIS_URL=redis://redis:6379
REDIS_RATE_LIMIT_URL=redis://redis:6379
```

Both point at the `redis` service on the `backend` network (port 6379).

# Notes

* The api falls back to image defaults if these aren't set, but the compose wires them explicitly.
* Rate limiting without Redis would fail — Redis must be up for the api to start cleanly.
* Valkey is mentioned as an (untested) alternative in compose comments.

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| API errors on rate limit | redis down | `docker compose restart redis` |
| Cache misses / slow | redis evicting | check memory; increase if needed |
