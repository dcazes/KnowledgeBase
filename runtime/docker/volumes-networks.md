---
type: Reference
title: Docker — Volumes & Networks
description: Persistent storage (named volumes vs bind mounts) and container networking (bridge/host/overlay, port publishing).
resource: https://docs.docker.com/engine/storage/volumes/
tags: [docker, volumes, networks, storage, networking]
generated: { by: "human:daniel", at: "2026-07-08T22:35:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-08T22:35:00Z" } ]
status: stable
stale_after: 2027-01-04
sources:
  - id: volumes
    resource: "https://docs.docker.com/engine/storage/volumes/"
    title: "Volumes"
    author: "site:docs.docker.com"
  - id: bind-mounts
    resource: "https://docs.docker.com/engine/storage/bind-mounts/"
    title: "Bind mounts"
    author: "site:docs.docker.com"
  - id: networking-overview
    resource: "https://docs.docker.com/engine/network/"
    title: "Networking overview"
    author: "site:docs.docker.com"
  - id: local-compose-examples-programs-firecrawl-programs-frigate
    resource: "/../../programs/"
    title: "Local compose examples - programs/firecrawl & programs/frigate"
---

# Volumes — persistent storage

Containers are ephemeral; anything written to the container's writable layer is lost when it's removed. Use volumes to persist data.

| Type | Definition | Use when |
|------|------------|----------|
| **Bind mount** | Maps a host path (`/home/...`) into the container. | You want to edit files on the host (configs, source code). |
| **Named volume** | Managed by Docker, stored in `/var/lib/docker/volumes/`. | You want Docker to own persistent data (DBs, profiles). |
| **tmpfs** | RAM-only, never written to disk. | Caches / secrets you don't want on disk (e.g. Frigate's `/tmp/cache`). |

```bash
docker volume create app_data            # named volume
docker volume ls                         # list
docker volume inspect app_data           # where it lives on disk
docker volume rm app_data                # remove (data gone)
```

In compose (from the real SearXNG/Firecrawl stack):

```yaml
volumes:
  - ./searxng/settings.yml:/etc/searxng/settings.yml:ro   # bind mount, read-only
  - cloak_profiles:/data                                  # named volume
```

# Networks — connectivity

By default every container is attached to a **bridge** network and can reach the internet, but containers on different user-defined networks can't see each other unless explicitly connected.

| Driver | Behavior |
|--------|----------|
| `bridge` (default) | Private network on the host; containers talk via service name. |
| `host` | Container shares the host's network stack (no port mapping needed; less isolation). |
| `none` | No networking. |
| `overlay` | Spans multiple Docker hosts (swarm). Not needed for single-machine stacks. |

```bash
docker network create agent_network          # user-defined bridge
docker network ls
docker network inspect agent_network
```

# Port publishing

Maps a port on the **host** to a port in the **container** (`HOST:CONTAINER`):

```bash
docker run -p 8082:8080 nginx     # host 8082 -> container 8080
```

In compose, host ports are remapped to avoid clashes — your SearXNG stack publishes SearXNG on `8082` (not `8080`) because CloakBrowser's panel already uses `8080`. Frigate publishes `8971` (HTTPS UI), `5000` (HTTP UI), `8554` (RTSP), and `8555` (WebRTC, tcp+udp).

# DNS / service discovery

On a user-defined bridge network, Docker runs an internal DNS resolver. Containers reach each other by **service name** (e.g. Firecrawl reaches `http://searxng:8080`). This is why `depends_on` plus the `agent_network` works in your stack.

# Cleaning up

```bash
docker volume prune          # remove unnamed/unused volumes (DESTRUCTIVE)
docker network prune         # remove unused networks
docker system prune -a       # containers, images, networks, build cache
```
