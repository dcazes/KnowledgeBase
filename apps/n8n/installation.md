---
type: Playbook
title: n8n Installation
description: Self-host n8n with Docker or the install script, run it with PostgreSQL via Compose for production, or install with npm; secure it with an encryption key and HTTPS.
resource: https://docs.n8n.io/hosting/
tags: [n8n, installation, docker, postgres]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: n8n-github
    resource: "https://github.com/n8n-io/n8n"
    title: "n8n-io/n8n on GitHub"
    author: "site:github.com"
  - id: n8n-docs
    resource: "https://docs.n8n.io"
    title: "n8n documentation"
    author: "site:docs.n8n.io"
---

# n8n — Installation

```bash
curl -fsSL https://get.n8n.io | sh                       # quick start (needs Docker)
docker volume create n8n_data
docker run -it --rm --name n8n -p 127.0.0.1:5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
npx n8n                                                  # or npm install -g n8n
```

Editor at `http://localhost:5678`.

## Production

* Use PostgreSQL (`DB_TYPE=postgresdb`, `DB_POSTGRESDB_*`) and a persistent volume.
* Set `N8N_ENCRYPTION_KEY` (credentials are encrypted with it — back it up).
* Put it behind HTTPS (`WEBHOOK_URL`, `N8N_HOST`, `N8N_PROTOCOL`); queue mode with Redis and workers scales execution.
* Keep the editor private, e.g. on [Tailscale](../../runtime/tailscale/index.md), while exposing only webhook paths if needed.

## Related

[n8n index](index.md) · [Docker Compose](../../runtime/docker/compose.md)
