---
type: HowTo
title: Cognee Installation
description: Install Cognee — pip install cognee (v1.4.2) or local v1.4.0; optional Docker compose (API + Postgres + vector) + cognee-frontend; verify with add+cognify.
resource: https://docs.cognee.ai
tags: [cognee, installation, pip, docker]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: cognee-docs-quickstart
    resource: "https://docs.cognee.ai"
    title: "Cognee docs — quickstart"
    author: "site:docs.cognee.ai"
  - id: cognee-on-pypi
    resource: "https://pypi.org/project/cognee/"
    title: "Cognee on PyPI"
    author: "site:pypi.org"
---

# Installation

## 1. Python library

```bash
pip install cognee              # latest (1.4.2 as of 2026-08-13)
# or the local checkout:
cd programs/cognee && pip install -e .
```

Verify:

```bash
python -c "import cognee; print(cognee.__version__ if hasattr(cognee,'__version__') else 'ok')"
```

## 2. Docker (API + backends, optional)

The checkout includes `docker-compose.yml`:

```bash
cd programs/cognee
docker compose up -d            # API + Postgres + vector store
```

## 3. Frontend (optional)

The checkout includes a `cognee-frontend` app (UI for browsing/searching the knowledge graph). Run per its README (Dev server / container).

## Status on this machine

* `programs/cognee` checkout present (v1.4.0), compose + frontend present — **not deployed**, no running containers (recon 2026-08-12).
