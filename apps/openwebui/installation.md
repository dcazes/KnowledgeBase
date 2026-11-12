---
type: Playbook
title: Open WebUI Installation
description: Install Open WebUI with Docker (main, slim, cuda or bundled-Ollama images) or Python, connect to Ollama, and update it.
resource: https://github.com/open-webui/open-webui
tags: [open-webui, installation, docker, pip]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openwebui-github
    resource: "https://github.com/open-webui/open-webui"
    title: "open-webui/open-webui on GitHub"
    author: "site:github.com"
---

# Open WebUI — Installation

## Docker

```bash
docker run -d -p 127.0.0.1:3000:8080 --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:main
```

| Tag | Includes |
|---|---|
| `:main` | Standard image with local AI dependencies |
| `:slim` | Uses external services for embeddings, extraction and voice |
| `:cuda` | CUDA acceleration |
| `:ollama` | Bundled Ollama |
| `:dev` | Latest development build |

Add `-e OLLAMA_BASE_URL=http://ollama:11434` or `-e OPENAI_API_KEY=...` as needed. The first account created becomes admin.

## Python

```bash
DATA_DIR=~/.open-webui uvx --python 3.12 open-webui@latest serve      # http://localhost:8080
pip install open-webui && open-webui serve
```

## Update

`docker pull ghcr.io/open-webui/open-webui:main` and recreate the container; the named volume keeps your data.

## Related

[Open WebUI index](index.md) · [Configuration](configuration.md) · [Docker](../../runtime/docker/index.md)
