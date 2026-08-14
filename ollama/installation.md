---
type: HowTo
title: Ollama Installation
description: Install Ollama — Docker compose (programs/ollama/docker-compose.yaml, :11434) or native binary; pull a model; verify with /api/tags.
resource: https://docs.ollama.com
tags: [ollama, installation, docker, binary]
timestamp: 2026-08-13T00:00:00Z
---

# Installation

## Option A — Docker (the local checkout's path)

`programs/ollama/docker-compose.yaml` (present, verified 2026-08-12):

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "11434:11434"
    restart: "no"
    volumes:
      - ollama:/root/.ollama   # (volumes section in the same file)
```

```bash
cd programs/ollama && docker compose up -d
docker exec ollama ollama pull llama3.1
```

## Option B — Native binary

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama serve &              # :11434
```

## Verify

```bash
curl -s http://localhost:11434/api/tags          # list pulled models
ollama run llama3.1                               # interactive chat
```

## Status on this machine

* Only the compose file exists; **no container running, no binary** (recon 2026-08-12). Deploy on demand with option A.

# Citations

[1] [Ollama docs — install](https://docs.ollama.com)
[2] [Docker Hub — ollama/ollama](https://hub.docker.com/r/ollama/ollama)
