---
type: Reference
title: Dify — Architecture
description: The Dify container set — api, api_websocket, worker, worker_beat, web, databases, redis, sandbox, plugin_daemon, ssrf_proxy, nginx, and selectable vector stores.
resource: https://github.com/langgenius/dify/tree/main/docker
tags: [dify, architecture, containers, celery, redis, vector-db, subservices]
timestamp: 2026-07-09T00:52:00Z
---

# Service topology

From `docker/docker-compose.yaml`, Dify runs as a set of cooperating containers:

```
browser / API client
        │  :80 (nginx)
        ▼
   ┌─────────────────────────────────────────────┐
   │  nginx  (reverse proxy → web + api)           │
   └───────┬───────────────────────┬───────────────┘
           │                       │
           ▼                       ▼
      web (Next.js)          api  +  api_websocket
                               │
                  ┌────────────┼─────────────────┐
                  ▼            ▼                 ▼
              worker       worker_beat      plugin_daemon
                  │            │                 │
                  ▼            ▼                 ▼
               redis (Celery broker)      external tool/plugin calls
                  │
                  ▼
        db_postgres / db_mysql  (metadata, datasets)
                  │
                  ▼
        vector store (weaviate / qdrant / pgvector / chroma / milvus / …)
   sandbox        ── isolated code execution
   ssrf_proxy     ── protects outbound requests from SSRF
   certbot        ── optional TLS
```

# Core services

| Service | Role |
|---------|------|
| `api` | Flask backend — app logic, RAG, model calls |
| `api_websocket` | WebSocket endpoint for streaming |
| `worker` | Celery worker — async jobs (indexing, dataset ops) |
| `worker_beat` | Celery beat — schedules periodic tasks |
| `web` | Next.js frontend UI |
| `nginx` | Reverse proxy, serves :80 |
| `db_postgres` / `db_mysql` | relational metadata/datasets store |
| `redis` | Celery broker + cache |
| `sandbox` | isolated code execution (for code nodes/tools) |
| `plugin_daemon` | serves tools/integrations/plugins |
| `ssrf_proxy` | mitigates SSRF on outbound fetches |
| `certbot` | optional Let's Encrypt TLS |

# Vector stores (pick one)

The compose defines many; you enable the one you want and set `VECTOR_STORE`:

`weaviate` (default), `qdrant`, `pgvector`, `chroma`, `milvus-standalone`, `oceanbase`, `opensearch`, `couchbase-server`, `iris`, `oracle`, `vastbase`, `pgvecto-rs`, `seekdb`.

# Middleware compose

`docker-compose.middleware.yaml` isolates the backbone: `db_postgres`, `db_mysql`, `redis`, `sandbox`, `plugin_daemon`, `ssrf_proxy`, `weaviate`.

# Why this matters

Celery + Redis means heavy jobs (document indexing, batch embedding) run off the request path — the API stays responsive. The sandbox + ssrf_proxy are security boundaries for user-supplied code and outbound fetches.

# Citations

[1] [docker/docker-compose.yaml (local)](/../../programs/archive/dify/docker/docker-compose.yaml)
[2] [docker-compose.middleware.yaml (local)](/../../programs/archive/dify/docker/docker-compose.middleware.yaml)
[3] [AGENTS.md — async via Celery/Redis](/../../programs/archive/dify/AGENTS.md)
