---
type: Playbook
title: Cognee Installation
description: Install Cognee with pip or uv (with the GLiNER extra for no-LLM mode), try the bundled demo, run the API, UI and MCP server with Docker, and understand single-user vs multi-tenant mode.
resource: https://docs.cognee.ai/getting-started/installation
tags: [cognee, installation, docker, uv, pip]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cognee-github
    resource: "https://github.com/topoteretes/cognee"
    title: "topoteretes/cognee on GitHub"
    author: "site:github.com"
  - id: cognee-docs
    resource: "https://docs.cognee.ai"
    title: "Cognee documentation"
    author: "site:docs.cognee.ai"
---

# Cognee — Installation

## Library

```bash
uv pip install "cognee[gliner]"      # gliner = local extraction model for no-LLM mode
pip install cognee                   # base package
cognee-cli demo                      # explore a bundled prebuilt graph, no API key needed
cognee-cli -ui                       # local UI (needs Node.js/npm; Docker for its MCP service)
```

Python 3.10–3.14 is supported.

## Docker (API only)

```bash
docker run --rm -it -p 8000:8000 \
  -e LLM_API_KEY="..." \
  -e ENABLE_BACKEND_ACCESS_CONTROL=false \
  -v cognee_storage:/cognee-storage \
  cognee/cognee:main
```

`ENABLE_BACKEND_ACCESS_CONTROL=false` is the single-user posture. Without it the API runs multi-tenant and every `/api/v1` call needs an authenticated user.

## Docker Compose (API + UI + MCP)

```bash
git clone https://github.com/topoteretes/cognee && cd cognee
cp .env.template .env        # configure providers
docker compose --profile ui --profile mcp up
```

Default ports: API **8000**, UI **3000**, MCP **8001**. For anything beyond a local demo, configure authentication, persistent storage and production backends.

## Related

[Cognee index](index.md) · [Configuration](configuration.md) · [Docker](../../runtime/docker/index.md)
