---
type: Concept
title: Dify Architecture
description: Services in a self-hosted Dify stack — API and worker, web front end, nginx, PostgreSQL, Redis, a vector database (Weaviate by default), the plugin daemon, the code sandbox, SSRF proxy, and agent backend and runtime.
resource: https://github.com/langgenius/dify/tree/main/docker
tags: [dify, architecture, docker, services]
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

# Dify — Architecture

```
browser ──▶ nginx ──▶ web (Next.js)
                 └──▶ api (Flask) ──▶ PostgreSQL · Redis · vector DB · object storage
                         │
                     worker (Celery: indexing, async tasks)
                         │
     plugin daemon (models, tools, strategies) · sandbox (code node) · ssrf_proxy
     agent backend + agent runtime (sandboxed autonomous agents)
```

| Service | Role |
|---|---|
| api / worker | Core logic; Celery workers run indexing and long tasks |
| web | Front end |
| db (PostgreSQL), redis | State, cache, queues |
| Vector store | Weaviate by default; Qdrant, pgvector, Milvus, OpenSearch, Elasticsearch, Chroma and more selectable via `VECTOR_STORE` |
| plugin_daemon | Runs installed plugins in isolation |
| sandbox | Executes code nodes safely |
| ssrf_proxy | Outbound proxy preventing server-side request forgery from workflows |
| agent backend/runtime | Sandboxes for autonomous agents (token-protected since 1.18) |

Upgrade the API, workers and agent images together; read each release's upgrade guide.

## Related

[Dify index](index.md) · [Installation](installation.md) · [Vector databases](../../concepts/vector-databases.md)
