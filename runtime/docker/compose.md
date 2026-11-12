---
type: Reference
title: Docker Compose
description: Docker Compose for multi-container AI stacks — file anatomy, common commands, profiles, health-checked dependencies, the models element for Model Runner, include, and watch.
resource: https://docs.docker.com/compose/
tags: [docker, compose, yaml, profiles, model-runner]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: compose-github
    resource: "https://github.com/docker/compose"
    title: "docker/compose on GitHub"
    author: "site:github.com"
  - id: compose-spec
    resource: "https://compose-spec.io"
    title: "Compose Specification"
    author: "site:compose-spec.io"
---

# Docker — Compose

Compose describes an application as services, networks, volumes and (since 2025) **models** in one YAML file. Compose v5 is the current major version.

## Example: a small local RAG stack

```yaml
services:
  qdrant:
    image: qdrant/qdrant
    volumes: [qdrant_data:/qdrant/storage]
    healthcheck:
      test: ["CMD", "bash", "-c", "exec 3<>/dev/tcp/localhost/6333"]
      interval: 10s

  ollama:
    image: ollama/ollama
    volumes: [ollama:/root/.ollama]
    deploy:
      resources:
        reservations:
          devices: [{ driver: nvidia, count: all, capabilities: [gpu] }]

  webui:
    image: ghcr.io/open-webui/open-webui:main
    ports: ["3000:8080"]
    environment:
      OLLAMA_BASE_URL: http://ollama:11434
      VECTOR_DB: qdrant
      QDRANT_URI: http://qdrant:6333
    depends_on:
      qdrant: { condition: service_healthy }
      ollama: { condition: service_started }
    profiles: ["ui"]

volumes: { qdrant_data: {}, ollama: {} }
```

Services reach each other by service name (`http://ollama:11434`) on the default network. See [Ollama](../ollama/index.md), [Qdrant](../../databases/qdrant/index.md), [Open WebUI](../../apps/openwebui/index.md).

## Commands

```bash
docker compose up -d                 # start
docker compose --profile ui up -d    # include profile-gated services
docker compose ps / logs -f / down
docker compose pull && docker compose up -d   # update images
docker compose watch                 # rebuild/sync on file changes (dev)
docker compose config                # render the merged file
```

## AI-specific features

* **`models:`** top-level element declares models served by [Docker Model Runner](gpu-ai.md#docker-model-runner) and injects their endpoint into services.
* **`include:`** composes several Compose files (e.g. one per tool) into one stack.
* **Jobs** (partial support since v5.6): manually triggered one-off tasks.

## Tips

* Pin image tags in production; `latest` changes under you.
* Bind ports to `127.0.0.1:` for services that should not be reachable from the network.
* Keep secrets in `.env` (excluded from git) or Compose `secrets:`.

## Related

[Docker index](index.md) · [Volumes & networks](volumes-networks.md) · [GPU & AI](gpu-ai.md)
