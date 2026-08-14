---
type: HowTo
title: LightRAG Installation
description: Install LightRAG — pip install lightrag-hku (v1.5.6) or local v1.5.5; optional FastAPI server via Docker (compose-full); verify with a first insert+query.
resource: https://lightrag.readthedocs.io/en/latest/
tags: [lightrag, installation, pip, docker, server]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: lightrag-docs-installation
    resource: "https://lightrag.readthedocs.io/en/latest/"
    title: "LightRAG docs — installation"
    author: "site:lightrag.readthedocs.io"
  - id: lightrag-on-pypi
    resource: "https://pypi.org/project/lightrag-hku/"
    title: "LightRAG on PyPI"
    author: "site:pypi.org"
---

# LightRAG — Installation

## 1. Python library

```bash
pip install lightrag-hku        # latest (1.5.6 as of 2026-08-13)
# or the local checkout:
cd programs/LightRAG && pip install -e .
```

Verify:

```bash
python -c "import lightrag; print(lightrag.__version__ if hasattr(lightrag,'__version__') else 'ok')"
```

## 2. Server (Docker, optional)

The checkout ships compose files (Redis + SQLite-based defaults):

```bash
cd programs/LightRAG
docker compose up -d            # default: API on :9621 (lightrag-server)
# full variant with milvus/neo4j wiring:
docker compose -f docker-compose-full.yml up -d
```

`docker-compose-full.yml` includes Milvus + Neo4j services for the production storage set (present in the local checkout, verified 2026-08-12).

## Status on this machine

* `programs/LightRAG` checkout present (v1.5.5) — **not deployed**, no running containers (recon 2026-08-12).
