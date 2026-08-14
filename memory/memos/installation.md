---
type: Playbook
title: MemOS — Installation & Deployment
description: Run MemOS via pip install MemoryOS (uvicorn :8000) or Docker (API + Neo4j + Qdrant); verify with /health.
resource: https://memos-docs.openmem.net/home/overview/
tags: [memos, install, deploy, uvicorn, docker, memory]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: memos-repo
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemOS repo"
    author: "site:github.com"
  - id: pypi-memoryos
    resource: "https://pypi.org/project/MemoryOS/"
    title: "PyPI — MemoryOS"
    author: "site:pypi.org"
---

# Deployment model

MemOS runs two ways on this machine (as of 2026-08-12 there is **no local checkout** at `programs/memos` — install from PyPI `MemoryOS`, import name `memos`):

1. **Python / uvicorn (primary)** — `pip install MemoryOS` then `uvicorn memos.api.server_api:app` on port **8000**. Not containerized. (The repo's own `make serve` = `poetry run uvicorn memos.api.server_api:app`, same entrypoint.)
2. **Docker** — the repo's `docker/docker-compose.yml` brings up `memos-api` + **Neo4j** (graph) + **Qdrant** (vector), all on `memos_network`, API published `8000:8000`.

> **Status:** **not installed / not running** — no `programs/memos` checkout (verified 2026-08-12). These are the run instructions, not a live-state report.

# Option A — uvicorn (pip)

```bash
pip install MemoryOS            # distribution name; import name is memos
uvicorn memos.api.server_api:app --host 0.0.0.0 --port 8000 --workers 1
# (or, with a repo clone present: make install && make serve)
```

Stop: Ctrl-C / kill the uvicorn process. Status: `docker ps` is **n/a** (not a container).

# Option B — Docker

```bash
# requires a clone of the MemOS repo (not present locally as of 2026-08-12):
git clone https://github.com/MemTensor/MemOS.git programs/memos
cd programs/memos
docker compose -f docker/docker-compose.yml up -d     # memos-api + neo4j + qdrant
docker compose -f docker/docker-compose.yml ps
docker compose -f docker/docker-compose.yml down
```
* Neo4j: `7474` (HTTP) / `7687` (Bolt), auth `neo4j/12345678` (compose default).
* Qdrant: `6333` (REST) / `6334` (gRPC).

# Verify it is up

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8000/health
```

# First-run / config

* Backends (vector DB, graph DB, LLM, embedder) are selected via config — see `docker/.env.example` and `docker/.env` for the env shape.
* For the uvicorn path, ensure a vector DB + LLM/embedder are reachable (Ollama works locally for embeddings).
* Export the OpenAPI contract after API changes: `make openapi` (writes `docs/openapi.json`).

# Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Import error on `make serve` | deps not installed | `make install` (with extras) |
| API 500 / can't connect to DB | Neo4j/Qdrant down or creds wrong | start the Docker stack or fix `QDRANT_*`/`NEO4J_*` env |
| `/health` unreachable | wrong port / not started | confirm `:8000`; `make serve` logs |
| Slow ingest | concurrency | raise scheduler concurrency in config |
