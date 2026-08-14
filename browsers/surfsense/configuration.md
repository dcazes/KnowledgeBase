---
type: HowTo
title: SurfSense Configuration
description: Configure SurfSense — .env (SURFSENSE_VERSION, SURFSENSE_VARIANT, keys), ports, volumes, scraper targets, gpu variant.
resource: https://github.com/modsetter/surfsense
tags: [surfsense, configuration, env, volumes]
timestamp: 2026-08-13T00:00:00Z
---

# Configuration

## `.env`

```env
SURFSENSE_VERSION=latest        # image tag for backend/frontend
SURFSENSE_VARIANT=              # e.g. cuda for GPU images (see gpu compose)
# secrets / keys (from .env.example — never commit real values)
POSTGRES_PASSWORD=...
REDIS_PASSWORD=...
# scraper + LLM keys (OpenAI/Anthropic/local as configured)
```

`SURFSENSE_VERSION` + `SURFSENSE_VARIANT` template the backend image ref: `ghcr.io/modsetter/surfsense-backend:${SURFSENSE_VERSION:-latest}${SURFSENSE_VARIANT:+-\${SURFSENSE_VARIANT}}` (verified in compose).

## Ports (compose, observed running)

**Only the proxy publishes host ports.** Everything else is container-internal (`expose` in compose — not reachable from the host).

| Port | Service | Host-accessible? |
|---|---|---|
| 3929 (http) / 4443 (https) | proxy (caddy) | **yes** (published) |
| 3000 | frontend | no (internal; reachable via proxy) |
| 8000-8001 | backend | no (internal) |
| 5432 | db | no (internal) |
| 6379 | redis | no (internal) |
| 8080 | searxng | no (internal) |
| 4848-4849 | zero-cache | no (internal) |

## Volumes (compose)

`postgres_data`, `redis_data`, `shared_temp`, `object_store`, `zero_cache_data`, `caddy_data`, `caddy_config` — named volumes for state persistence. `whatsapp_sessions` is declared in the volume list but **not mounted** (its `volumes:` entry is commented out in compose — verified 2026-08-13).

## Scraper configuration

* Reddit/YouTube targets configured in-app (UI) or via API; Celery workers execute the scrape jobs (celery_beat schedules).
* SearXNG instance config lives in `programs/surfsense/searxng/` (the bundled metasearch service).

## GPU variant

`docker-compose.gpu.yml` adds GPU passthrough (for local models/embeddings) — use when `SURFSENSE_VARIANT=cuda` images are selected.

# Citations

[1] [SurfSense GitHub — compose](https://github.com/modsetter/surfsense)
[2] [SurfSense docs](https://docs.modsetter.com/surfsense)
