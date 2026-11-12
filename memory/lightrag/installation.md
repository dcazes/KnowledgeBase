---
type: Playbook
title: LightRAG Installation
description: Install LightRAG Server from PyPI with uv, from source with the WebUI build, or with Docker Compose; use the interactive setup wizard and secure the server.
resource: https://github.com/HKUDS/LightRAG
tags: [lightrag, installation, uv, docker, webui]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: lightrag-github
    resource: "https://github.com/HKUDS/LightRAG"
    title: "HKUDS/LightRAG on GitHub"
    author: "site:github.com"
  - id: lightrag-docker
    resource: "https://github.com/HKUDS/LightRAG/blob/main/docs/DockerDeployment.md"
    title: "LightRAG Docker deployment"
    author: "site:github.com"
---

# LightRAG — Installation

## PyPI (server + prebuilt WebUI)

```bash
uv tool install "lightrag-hku[api]"          # or: pip install "lightrag-hku[api]" in a venv
curl -O https://raw.githubusercontent.com/HKUDS/LightRAG/main/env.example
cp env.example .env                          # set model keys first
lightrag-server                              # http://localhost:9621/webui
```

Library only: `pip install lightrag-hku`.

## From source

```bash
git clone https://github.com/HKUDS/LightRAG.git && cd LightRAG
uv sync --extra api                          # API + WebUI runtime
cd lightrag_webui && bun install --frozen-lockfile && bun run build && cd ..
cp env.example .env && lightrag-server
```

## Docker Compose

```bash
git clone https://github.com/HKUDS/LightRAG.git && cd LightRAG
cp env.example .env
docker compose up
```

Official GHCR images are signed with Sigstore Cosign.

## Setup wizard

```bash
make env-base             # LLM, embedding, reranker (required first)
make env-storage          # storage backends and their services
make env-server           # port, auth, SSL
make env-security-check   # audit .env for risky settings
```

## Secure it

`lightrag-server` binds to all interfaces with authentication off. On any shared network set `LIGHTRAG_API_KEY` and/or account auth, or bind to localhost and reach it over a private network such as [Tailscale](../../runtime/tailscale/index.md).

## Related

[LightRAG index](index.md) · [Configuration](configuration.md) · [Docker](../../runtime/docker/index.md)
