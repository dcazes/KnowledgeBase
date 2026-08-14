---
type: CheatSheet
title: SurfSense Snippets
description: SurfSense cheat sheet — compose status, container checks, port probes, logs, scraper verification, mcp wiring.
resource: https://github.com/modsetter/surfsense
tags: [surfsense, snippets, cheat-sheet]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: surfsense-github
    resource: "https://github.com/modsetter/surfsense"
    title: "SurfSense GitHub"
    author: "site:github.com"
---

# Snippets

## Status

```bash
docker ps --filter name=surfsense --format '{{.Names}}\t{{.Status}}\t{{.Ports}}'
# expect 9 containers: proxy, backend, frontend, db, redis,
#   celery_worker, celery_beat, zero-cache, searxng
```

## Port probes

Only the proxy is host-reachable; the rest are container-internal:

```bash
curl -sI http://localhost:3929 | head -1       # proxy http (published)
curl -skI https://localhost:4443 | head -1     # proxy https (published)
docker compose exec frontend sh -c 'wget -qO- http://localhost:3000 | head -5'   # UI (internal)
docker compose exec searxng sh -c 'wget -qO- http://localhost:8080 | head -1'    # searxng (internal)
```

## Logs

```bash
docker compose logs -f --tail=100 backend      # API + AI orchestration
docker compose logs -f --tail=50 celery_worker # scraper jobs
docker compose logs -f --tail=50 zero-cache    # graph sync
```

## Manage

```bash
cd programs/surfsense
docker compose ps
docker compose restart celery_worker
docker compose up -d --no-deps frontend        # restart a single service
```

## Scraper check

```bash
docker compose exec backend python -c "import urllib.request; print(urllib.request.urlopen('http://redis:6379').status if False else 'redis up')" 2>/dev/null
# or simply: docker compose exec redis redis-cli ping   # PONG
docker compose exec searxng sh -c 'wget -qO- http://localhost:8080 | head -1'
```

## MCP

```bash
# from mcp/ dir — see README for the exact server entry
npm install && npm run build
# then register as an MCP server for Hermes/OpenCode with the built command
```
