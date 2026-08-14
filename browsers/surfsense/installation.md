---
type: HowTo
title: SurfSense Installation
description: Install/run SurfSense — docker compose up from programs/surfsense, version pins, first-run setup, verification via containers/ports.
resource: https://github.com/modsetter/surfsense
tags: [surfsense, installation, docker, compose]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: surfsense-github-compose
    resource: "https://github.com/modsetter/surfsense"
    title: "SurfSense GitHub — compose"
    author: "site:github.com"
  - id: surfsense-docs
    resource: "https://docs.modsetter.com/surfsense"
    title: "SurfSense docs"
    author: "site:docs.modsetter.com"
---

# Installation

## 1. Compose up

```bash
cd programs/surfsense
cp .env.example .env          # set SURFSENSE_VERSION, API keys, secrets
docker compose up -d          # migrations run first, then the 9 services
```

Compose files present (verified 2026-08-12):

* `docker-compose.yml` — full stack (db/migrations/redis/searxng/proxy/backend/celery_worker/celery_beat/zero-cache/frontend)
* `docker-compose.gpu.yml` — GPU variant (for local-LLM embedding/inference)
* `postgresql.conf`, `proxy/`, `scripts/` — supporting configs

## 2. First run

1. `migrations` service initializes the schema before the rest start.
2. Proxy front at **:3929** (http) / **:4443** (https) — the only host-reachable ports (frontend :3000, backend :8000, searxng :8080 are container-internal).
3. Add scraper targets (Reddit subreddits, YouTube channels) via the UI or config.

## 3. Verify (as observed 2026-08-12)

```bash
docker ps --filter name=surfsense     # 9 containers running
curl -sI http://localhost:3929 | head -1        # proxy responds (published)
# frontend/backend/searxng are internal-only — probe them from inside:
docker compose exec frontend sh -c 'wget -qO- http://localhost:3000 | head -5'
```

## Version pins (compose, verified)

* `pgvector/pgvector:pg17`, `redis:8-alpine`, `searxng/searxng:2026.3.13-3c1f68c59`, `caddy:2-alpine`, `rocicorp/zero:1.6.0`, backend/frontend `ghcr.io/modsetter/...:${SURFSENSE_VERSION:-latest}`.
