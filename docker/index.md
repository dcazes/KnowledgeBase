---
type: Reference
title: Docker
description: Containerization platform — the runtime foundation for most other programs in this knowledge base.
resource: https://www.docker.com
tags: [docker, containers, runtime]
timestamp: 2026-08-12T00:00:00Z
---

# Docker

Containerization platform — the runtime foundation for most other programs in this knowledge base (SearXNG, Frigate, Firecrawl, AnythingLLM, Dify all run as containers).

## Contents

* [Overview](overview.md) - what Docker is, architecture (client / daemon / containerd / runc), OCI, when to use it
* [Installation & Setup](installation.md) - install on Linux (your Docker Desktop `.deb`), `systemctl --user`, post-install group/socket, verification
* [Images & Containers](images-containers.md) - the core build/pull/run/exec lifecycle, Dockerfile essentials, layer caching
* [Compose](compose.md) - `docker-compose.yml` anatomy, common services, `up`/`down`/`ps`/`logs`, real examples from this machine
* [Volumes & Networks](volumes-networks.md) - named volumes vs bind mounts, bridge/host/overlay networks, port publishing
* [Registry & Images](registry.md) - Docker Hub, private registries, tagging, push/pull, pruning
* [GPU & AI in Containers](gpu-ai.md) - NVIDIA runtime, device reservation, running Frigate / LLM inference on the GTX 1060
* [Snippets](snippets.md) - copy-paste cheat sheet covering the majority of daily use cases

## Quick start

```bash
# Your machine starts Docker Desktop as a user service (see programs/docker/run)
systemctl --user start docker-desktop

# Verify
docker version
docker run hello-world
```

## Cross-references

* **SearXNG** — runs in Docker on the `backend` network — see [SearXNG Installation](../searxng/installation.md)
* **Frigate** — GPU-accelerated container with NVIDIA device reservation — see [Docker GPU & AI](gpu-ai.md) & [Frigate Installation](../frigate/installation.md)
* **Firecrawl** — 6-service Docker stack + SearXNG — see [Firecrawl Self-Hosting](../firecrawl/self-hosting.md)
* **Dify** — full-stack Docker deployment — see [Dify Installation](../dify/installation.md)
* **AnythingLLM** — containerized deployment — see [AnythingLLM Installation](../anythingllm/installation.md)
* **OpenWebUI** — Docker-based — see [OpenWebUI Installation](../openwebui/installation.md)

## Last verified

**2026-08-12** — All configs, compose examples, and GPU settings verified against local `programs/docker/` and running containers. Engine 29.7.2, Compose v5.4.0.

# Citations

[1] [Docker documentation](https://docs.docker.com/)
[2] [Docker Desktop for Linux](https://docs.docker.com/desktop/setup/install/linux/)
[3] [Local install notes - programs/docker/](/../../programs/docker/)