---
type: Playbook
title: Dify — Installation
description: Deploy Dify Community Edition via Docker Compose from the local docker/ directory and reach the setup dashboard.
resource: https://docs.dify.ai/getting-started/install-self-hosted
tags: [dify, install, docker, compose, self-hosted, deployment]
timestamp: 2026-07-09T00:51:00Z
---

# Requirements

* Docker + Docker Compose.
* CPU ≥ 2 cores, RAM ≥ 4 GiB (more for heavier workloads).
* Pick **one** vector database (Weaviate is the default in the compose).

# Deploy (from local source)

```bash
cd programs/archive/dify/docker
cp .env.example .env         # required before first launch
docker compose up -d
```

This starts the full stack (api, worker, web, db, redis, sandbox, plugin_daemon, ssrf_proxy, nginx, and a vector store).

# First launch

Open the setup page in a browser:

```
http://localhost/install
```

Complete the initialization (admin account, model provider). After that, the app is at `http://localhost/`.

> The compose publishes nginx on **:80**. If something else uses :80, edit `docker/.env` / the compose port mapping.

# Configuration

* Edit `docker/.env` for core settings; advanced vars are split under `docker/envs/` by theme.
* After changes: `docker compose up -d` from the `docker` directory.
* Full env reference: https://docs.dify.ai/getting-started/install-self-hosted/environments

# Choose a vector store

The compose includes many (weaviate, qdrant, pgvector, chroma, milvus, oceanbase, opensearch, couchbase, iris, oracle, vastbase, pgvecto-rs). Default is **Weaviate**. To switch, enable the relevant service in the compose and set `VECTOR_STORE` in `.env`.

# Verify

```bash
docker compose ps          # all services healthy
curl -s -o /dev/null -w "%{http_code}\n" http://localhost/install
docker compose logs -f api
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| :80 already in use | port clash | change nginx port in compose/.env |
| Worker not processing | Redis down | `docker compose restart redis` |
| Plugins missing | plugin_daemon down | `docker compose restart plugin_daemon` |
| Migration errors | db not ready | wait; re-run `docker compose up -d` |

# Citations

[1] [Install self-hosted](https://docs.dify.ai/getting-started/install-self-hosted)
[2] [Local docker dir - programs/archive/dify/docker/](/../../programs/archive/dify/docker/)
[3] [README quick start](/../../programs/archive/dify/README.md)
