---
type: Reference
title: Docker Registries
description: Image registries — Docker Hub, GHCR and private registries; tagging and pushing; digests and signing; pruning; and OCI artifacts such as models and agents.
resource: https://docs.docker.com/docker-hub/
tags: [docker, registry, ghcr, oci, tags]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docker-docs
    resource: "https://docs.docker.com"
    title: "Docker documentation"
    author: "site:docs.docker.com"
---

# Docker — Registries

## Common registries

| Registry | Example image |
|---|---|
| Docker Hub | `ollama/ollama`, `qdrant/qdrant`, `searxng/searxng` |
| GitHub Container Registry | `ghcr.io/open-webui/open-webui`, `ghcr.io/vectorize-io/hindsight` |
| Self-hosted | `registry:2` / Harbor / Zot |

## Tag, push, pull

```bash
docker login ghcr.io
docker tag myapp:latest ghcr.io/me/myapp:1.2.0
docker push ghcr.io/me/myapp:1.2.0
docker pull ghcr.io/me/myapp@sha256:...      # pin by digest for reproducibility
```

## Trust

* Prefer official or verified publishers; check the source repository.
* Many projects sign images with Sigstore Cosign (e.g. [LightRAG](../../memory/lightrag/installation.md)); verify with `cosign verify`.
* Pin by digest for production deploys.

## OCI artifacts beyond images

Registries now store more than containers: Docker Model Runner pulls **models** as OCI artifacts (`ai/gemma3`), and [Docker Agent](gpu-ai.md#docker-agent) pushes and pulls **agent definitions**. Helm charts (e.g. [Hindsight](../../memory/hindsight/installation.md)) are also distributed as OCI artifacts.

## Pruning

```bash
docker image ls --filter dangling=true
docker image prune -a          # remove all images not used by a container
```

## Related

[Docker index](index.md) · [Images & containers](images-containers.md)
