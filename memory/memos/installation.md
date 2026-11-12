---
type: Playbook
title: MemOS Installation
description: Four ways to run MemOS — the hosted Cloud API, self-hosted with Docker Compose (API, Neo4j, Qdrant), uvicorn without Docker, or the cloud and local agent plugins.
resource: https://memos-docs.openmem.net
tags: [memos, installation, docker, neo4j, qdrant]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: memos-github
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemTensor/MemOS on GitHub"
    author: "site:github.com"
  - id: memos-docs
    resource: "https://memos-docs.openmem.net"
    title: "MemOS documentation"
    author: "site:memos-docs.openmem.net"
---

# MemOS — Installation

| | Cloud API | Self-host | Cloud plugin | Local plugin |
|---|---|---|---|---|
| Best for | Apps, fully managed | Teams on own infra | OpenClaw, zero ops | Hermes, OpenClaw, DeepSeek Harness on-device |
| Infra | None | Neo4j + Qdrant | None | None (SQLite) |
| Data lives | MemOS Cloud | Your servers | MemOS Cloud | Your machine |

## Cloud API

Sign up on the MemOS dashboard and create an API key (prefix `mpg-`); keep it server-side.

## Self-host with Docker

```bash
git clone https://github.com/MemTensor/MemOS.git && cd MemOS
cp docker/.env.example .env          # fill in model keys
cd docker && docker compose up       # MemOS API + Neo4j + Qdrant, API on :8000
```

## Without Docker

Run [Neo4j](../../databases/neo4j/index.md) and [Qdrant](../../databases/qdrant/index.md) yourself, then:

```bash
cd MemOS/src
uvicorn memos.api.server_api:app --host 0.0.0.0 --port 8000 --workers 1
```

## Plugins

* **OpenClaw cloud plugin:** `openclaw plugins install` the MemOS cloud plugin.
* **Local plugin:** `npm install` the local plugin and follow the agent-specific setup for Hermes, OpenClaw or DeepSeek Harness.

## Related

[MemOS index](index.md) · [Configuration](configuration.md) · [Docker](../../runtime/docker/index.md)
