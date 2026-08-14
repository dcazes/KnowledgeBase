---
type: Reference
title: SurfSense
description: Self-hosted personal knowledge-graph assistant (modsetter) — scrapes and memorizes your web activity (Reddit, YouTube, docs) into a ZeroSync graph DB with an AI Q&A layer. RUNNING on this machine (9 containers).
resource: https://github.com/modsetter/surfsense
tags: [surfsense, knowledge-graph, scraping, zero, mcp, personal-ai]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: surfsense-github
    resource: "https://github.com/modsetter/surfsense"
    title: "SurfSense GitHub"
    author: "site:github.com"
  - id: surfsense-docs
    resource: "https://docs.modsetter.com/surfsense"
    title: "SurfSense docs"
    author: "site:docs.modsetter.com"
  - id: zero-rocicorp
    resource: "https://zero.rocicorp.dev"
    title: "Zero (Rocicorp)"
    author: "site:zero.rocicorp.dev"
---

# SurfSense

A **self-hosted personal knowledge assistant** (by modsetter) — "your data, your assistant." It scrapes and memorizes your web activity (Reddit, YouTube, docs, files) into a **Zero** (ZeroSync) graph database and provides an AI chat layer that answers from your personal knowledge. Ships with a SurfSense **MCP server** for agent integration.

**LIVE ON THIS MACHINE** — the full stack is running (9 containers, verified via `docker ps` 2026-08-12, up ~3h):

| Container | Image | Ports |
|---|---|---|
| `surfsense-proxy-1` | `caddy:2-alpine` | host `:3929`→80, `:4443`→443 |
| `surfsense-backend-1` | `ghcr.io/modsetter/surfsense-backend` | 8000-8001 |
| `surfsense-frontend-1` | `ghcr.io/modsetter/surfsense-web` | :3000 |
| `surfsense-db-1` | `pgvector/pgvector:pg17` | 5432 |
| `surfsense-searxng-1` | `searxng/searxng:2026.3.13-3c1f68c59` | 8080 |
| `surfsense-redis-1` | `redis:8-alpine` | 6379 |
| `surfsense-celery_worker-1` | surfsense-backend image | — |
| `surfsense-celery_beat-1` | surfsense-backend image | — |
| `surfsense-zero-cache-1` | `rocicorp/zero:1.6.0` | 4848-4849 |

Compose at `programs/surfsense/docker-compose.yml` (+ `docker-compose.gpu.yml`, `postgresql.conf`, `proxy/`, `scripts/`, `mcp/`).

## Contents

* [Overview](overview.md) — what SurfSense is, Zero graph DB, scrapers (Reddit/YouTube), AI Q&A
* [Installation](installation.md) — compose up, version pins, first-run
* [Configuration](configuration.md) — `.env` (SURFSENSE_VERSION, keys), ports, volumes
* [AI Integration](ai-integration.md) — chat + MCP server, agent wiring, querying personal knowledge
* [Snippets](snippets.md) — status / logs / scrape checks / API probes cheat sheet
* [Alternatives](../alternatives.md) — Obsidian, Supermemory, Mem0/MemOS, Rewind vs SurfSense

## Related

* [SearXNG](../../runtime/searxng/index.md) — bundled metasearch service inside this stack
* [Zero](https://zero.rocicorp.dev) — the sync/graph engine behind the cache service
* [Camofox](../camofox/index.md) — browser automation; SurfSense scrapers cover Reddit/YouTube instead

## Last verified

**2026-08-13** — Stack RUNNING (9 containers, up ~3h as of 2026-08-12 recon). Compose pins: pgvector pg17, redis 8-alpine, searxng 2026.3.13-3c1f68c59, zero-cache rocicorp/zero:1.6.0, caddy 2-alpine, backend/frontend ghcr.io/modsetter latest.
