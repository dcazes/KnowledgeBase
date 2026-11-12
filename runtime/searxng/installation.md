---
type: Playbook
title: SearXNG Installation
description: Deploy SearXNG with the official container compose template or a single docker run, update it, and put it behind a reverse proxy or private network.
resource: https://docs.searxng.org/admin/installation-docker.html
tags: [searxng, installation, docker, compose]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: searxng-container
    resource: "https://docs.searxng.org/admin/installation-docker.html"
    title: "SearXNG container installation"
    author: "site:docs.searxng.org"
  - id: searxng-docs
    resource: "https://docs.searxng.org"
    title: "SearXNG documentation"
    author: "site:docs.searxng.org"
---

# SearXNG — Installation

## Container compose template (recommended)

The project publishes a maintained Compose file under `container/docker-compose.yml` in the repository; the docs walk through fetching it with its `.env` into a `searxng/` directory and then:

```bash
docker compose up -d
docker compose logs -f core
docker compose pull && docker compose up -d     # update
```

The container is named `searxng-core` and listens on port 8080.

## Single container

```bash
mkdir -p ./searxng/config ./searxng/data
docker run -d --name searxng -p 127.0.0.1:8080:8080 \
  -v ./searxng/config:/etc/searxng -v ./searxng/data:/var/cache/searxng \
  searxng/searxng:latest
```

On first start SearXNG writes a default `settings.yml` into `/etc/searxng`; edit it and restart. Images are on Docker Hub (`searxng/searxng`) and GHCR (`ghcr.io/searxng/searxng`).

## Exposure

* For personal or agent use, bind to `127.0.0.1` or reach it over [Tailscale](../tailscale/index.md).
* A public instance needs a reverse proxy with TLS and the **limiter** (bot protection) enabled.

## Related

[SearXNG index](index.md) · [Configuration](configuration.md) · [Docker Compose](../docker/compose.md)
