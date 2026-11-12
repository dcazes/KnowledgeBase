---
type: Playbook
title: Honcho Installation
description: Run Honcho managed, as a local stack with honcho-cli, with Docker Compose from source, or natively with PostgreSQL + pgvector; configure the LLM provider and point SDKs at it.
resource: https://github.com/plastic-labs/honcho
tags: [honcho, installation, docker, cli, pgvector, self-hosting]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: honcho-github
    resource: "https://github.com/plastic-labs/honcho"
    title: "plastic-labs/honcho on GitHub"
    author: "site:github.com"
  - id: honcho-cli
    resource: "https://pypi.org/project/honcho-cli/"
    title: "honcho-cli on PyPI"
    author: "site:pypi.org"
---

# Honcho — Installation

## Managed

Get a key at app.honcho.dev (each organisation gets a dedicated instance) and use the SDKs with `HONCHO_API_KEY`.

## Local stack with the CLI

```bash
uv tool install honcho-cli
honcho init                 # API key or browser login + server URL, written to ~/.honcho/config.json
honcho start --setup basic  # writes the LLM key the deriver needs; starts API + deriver + Postgres + Redis in Docker
honcho doctor
honcho workspace inspect
```

## Docker from source

```bash
git clone https://github.com/plastic-labs/honcho.git && cd honcho
cp docker-compose.yml.example docker-compose.yml
cp .env.template .env       # set LLM_OPENAI_API_KEY, or another provider such as OpenRouter
docker compose up           # API on http://localhost:8000
```

## Native

Needs uv (installs Python 3.13+), PostgreSQL with [pgvector](../../databases/pgvector/index.md) (plus optional `pg_trgm` for faster message search) and one LLM provider key. Redis caching is optional (`CACHE_ENABLED=false` by default).

```bash
uv sync
# create a honcho role and database, then: CREATE EXTENSION vector;
```

## Point the SDK at your server

```python
honcho = Honcho(workspace_id="my-app", base_url="http://localhost:8000")   # or HONCHO_URL
```

## Related

[Honcho index](index.md) · [Snippets](snippets.md) · [Self-hosting](../../concepts/self-hosting.md)
