---
type: Software
title: Docker — Overview
description: Containerization platform that packages apps and dependencies into portable, isolated containers sharing the host kernel.
resource: https://docs.docker.com/get-started/docker-overview/
tags: [docker, containers, infrastructure, devops]
timestamp: 2026-07-08T22:35:00Z
---

# What Docker is

Docker is a platform for building, shipping, and running applications in **containers** — lightweight, isolated environments that bundle an app with everything it needs (code, runtime, libraries, config). Containers share the host OS kernel but get their own filesystem, process space, and network stack, making them far lighter than virtual machines.

On this machine Docker is the **foundation layer**: SearXNG, Frigate, Firecrawl, AnythingLLM, and Dify all run as containers (see [Compose](compose.md) for the real configs).

# Architecture

Docker is a client/server system:

| Component | Role |
|-----------|------|
| **Docker CLI** (`docker`) | Client you type commands into. |
| **Docker daemon** (`dockerd`) | Server that builds, runs, and manages containers, images, networks, and volumes. Listens on a Unix socket (`/var/run/docker.sock`). |
| **containerd** | Core container runtime that the daemon uses to manage the container lifecycle. |
| **runc** | Low-level OCI runtime that actually creates/spawns container processes. |
| **OCI images** | Images follow the **Open Container Initiative** spec, so any OCI-compliant runtime can run them. |

```
docker CLI  ──>  dockerd (daemon)  ──>  containerd  ──>  runc  ──>  container
```

# Key concepts

* **Image** — an immutable, layered template used to create containers (think "class" vs instance).
* **Container** — a running instance of an image.
* **Layer** — each Dockerfile instruction creates a read-only layer; layers are cached and shared.
* **Registry** — a store for images (Docker Hub by default; see [Registry](registry.md)).
* **Volume / Network** — persistent storage and connectivity primitives (see [Volumes & Networks](volumes-networks.md)).

# When to use Docker

* **Use it** when you want reproducible environments, isolation, easy cleanup, or to run services (like your AI stack) without polluting the host.
* **It is not** a substitute for a VM when you need a different kernel, or for heavy local LLM inference where you'd rather talk to cloud endpoints (your setup routes inference through OpenRouter/NIM per the KB plan).

# Citations

[1] [Docker overview](https://docs.docker.com/get-started/docker-overview/)
[2] [Docker architecture](https://docs.docker.com/get-started/docker-overview/#docker-architecture)
[3] [OCI image spec](https://github.com/opencontainers/image-spec)
