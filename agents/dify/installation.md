---
type: Playbook
title: Dify Installation
description: Self-host Dify with Docker Compose — prepare .env including the agent sandbox token, start the stack, run the setup wizard, and upgrade safely.
resource: https://github.com/langgenius/dify
tags: [dify, installation, docker-compose, upgrade]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: dify-github
    resource: "https://github.com/langgenius/dify"
    title: "langgenius/dify on GitHub"
    author: "site:github.com"
---

# Dify — Installation

Requirements: Docker with Compose, at least 2 CPU cores and 4 GB RAM.

```bash
git clone https://github.com/langgenius/dify.git && cd dify/docker
cp .env.example .env
openssl rand -hex 32           # paste into DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN in .env
docker compose up -d
docker compose ps --all
```

Open `http://localhost/install` to create the admin account.

## Upgrading

Keep your `.env`, read the release's upgrade notes (some releases need staged steps, e.g. the Weaviate jump in 1.17.1), back up PostgreSQL and the vector store, then pull and restart.

## Related

[Dify index](index.md) · [Architecture](architecture.md) · [Docker Compose](../../runtime/docker/compose.md)
