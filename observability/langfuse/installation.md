---
type: Playbook
title: Langfuse Installation
description: Self-host Langfuse with Docker Compose — the web and worker services with PostgreSQL, ClickHouse, Redis and S3-compatible storage — or use Langfuse Cloud; then create API keys.
resource: https://langfuse.com/self-hosting
tags: [langfuse, installation, docker, clickhouse]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langfuse-github
    resource: "https://github.com/langfuse/langfuse"
    title: "langfuse/langfuse on GitHub"
    author: "site:github.com"
  - id: langfuse-docs
    resource: "https://langfuse.com/docs"
    title: "Langfuse documentation"
    author: "site:langfuse.com"
---

# Langfuse — Installation

```bash
git clone --depth=1 https://github.com/langfuse/langfuse.git && cd langfuse
docker compose up          # UI on http://localhost:3000
```

The stack runs **langfuse-web**, **langfuse-worker**, PostgreSQL (metadata), **ClickHouse** (traces and analytics), Redis (queues/cache) and MinIO or another S3-compatible store (events, media). Change every default secret in the Compose file before exposing it. For production use the Helm chart or Terraform modules.

Create a project, then copy the public and secret keys:

```bash
export LANGFUSE_PUBLIC_KEY=pk-lf-...
export LANGFUSE_SECRET_KEY=sk-lf-...
export LANGFUSE_HOST=http://localhost:3000
```

## Related

[Langfuse index](index.md) · [Docker Compose](../../runtime/docker/compose.md)
