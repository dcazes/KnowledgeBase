---
type: Concept
title: SurfSense Overview
description: What SurfSense is — personal knowledge-graph assistant: scrapers (Reddit, YouTube, docs), Zero graph DB storage, AI Q&A from personal memory, MCP server.
resource: https://github.com/modsetter/surfsense
tags: [surfsense, overview, knowledge-graph, zero]
timestamp: 2026-08-13T00:00:00Z
---

# Overview

SurfSense is a **self-hosted personal knowledge-graph assistant**: it continuously memorizes your web activity, stores it in a local graph database, and lets an AI assistant answer from that personal knowledge.

## Data flow

1. **Capture** — scrapers fetch content you engage with:
   * Reddit (posts/comments)
   * YouTube (videos/transcripts)
   * Docs / files / manual inputs
   * (SearXNG service included for search fallback)
2. **Store** — scraped items land in **Zero** (Rocicorp's ZeroSync engine, `rocicorp/zero:1.6.0` cache service) over Postgres (pgvector/pg17) as a graph of entities/relations.
3. **Query** — the AI chat layer answers questions grounded in the graph; the **MCP server** exposes the same memory to agents.

## Architecture (9 containers)

| Service | Role |
|---|---|
| `proxy` (caddy) | TLS/reverse proxy — **only service with host ports** (:3929 http, :4443 https) |
| `backend` (FastAPI) | API + AI orchestration (8000-8001, container-internal) |
| `frontend` (web) | chat UI (:3000, container-internal, served via proxy) |
| `db` (pgvector) | primary store (5432, internal) |
| `redis` | cache/queue (6379, internal) |
| `celery_worker` / `celery_beat` | async scraping pipeline |
| `zero-cache` | Zero sync/graph cache (4848-4849, internal) |
| `searxng` | bundled metasearch (8080, internal) |

## Positioning

End-user personal knowledge (like Supermemory) but **self-hosted + graph-based + agent-accessible (MCP)** — closer to the developer memory stack than a consumer app.

# Citations

[1] [SurfSense GitHub](https://github.com/modsetter/surfsense)
[2] [SurfSense docs](https://docs.modsetter.com/surfsense)
[3] [Zero](https://zero.rocicorp.dev)
