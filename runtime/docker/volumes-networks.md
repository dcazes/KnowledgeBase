---
type: Reference
title: Docker Volumes & Networks
description: Persistent storage with named volumes and bind mounts, user-defined networks with DNS service discovery, port publishing and binding to localhost, and cleanup.
resource: https://docs.docker.com/engine/storage/
tags: [docker, volumes, networks, ports, storage]
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

# Docker — Volumes & Networks

## Volumes

| Kind | Syntax | Use |
|---|---|---|
| Named volume | `-v pgdata:/var/lib/postgresql/data` | Databases, model caches — managed by Docker |
| Bind mount | `-v ./config:/app/config:ro` | Config files and source code from the host |
| tmpfs | `--tmpfs /tmp` | Scratch data in memory |

```bash
docker volume ls
docker volume inspect pgdata
docker run --rm -v pgdata:/data -v "$PWD":/backup alpine tar czf /backup/pgdata.tgz -C /data .
```

Model caches (Ollama, Hugging Face) are large — put them on named volumes so upgrades do not re-download models.

## Networks

* Containers on the same **user-defined network** resolve each other by name via Docker's embedded DNS. Compose creates one per project automatically.
* The default `bridge` network has no name resolution.
* `--network host` shares the host's network stack (Linux only); simple but bypasses isolation.

```bash
docker network create ai
docker run -d --network ai --name searxng searxng/searxng
docker run --rm --network ai curlimages/curl http://searxng:8080
```

## Ports

`-p 8080:80` publishes on **all** host interfaces. Use `-p 127.0.0.1:8080:80` for local-only services, and a private network such as [Tailscale](../tailscale/index.md) or a reverse proxy for remote access. Docker's port publishing can bypass host firewalls like `ufw`.

## Cleanup

```bash
docker system df
docker system prune            # stopped containers, unused networks, dangling images
docker volume prune            # unused volumes — destructive
```

## Related

[Docker index](index.md) · [Compose](compose.md) · [Self-hosting](../../concepts/self-hosting.md)
