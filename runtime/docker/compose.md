---
type: Reference
title: Docker — Compose
description: Multi-container apps defined in docker-compose.yml; the primary way the AI stack on this machine is run.
resource: https://docs.docker.com/compose/
tags: [docker, compose, multi-container, services]
timestamp: 2026-07-08T22:35:00Z
---

# What Compose is

Compose lets you define a **multi-container app** in a single `docker-compose.yml`. Instead of typing long `docker run` commands, you describe services, networks, and volumes declaratively and manage them as a group. Almost every program in this KB uses Compose (SearXNG, Frigate, Firecrawl, AnythingLLM, Dify).

# Anatomy of a compose file

```yaml
services:
  app:
    image: nginx:alpine          # or build: .  (path to a Dockerfile)
    container_name: my_app
    ports:
      - "8080:80"                # HOST:CONTAINER
    volumes:
      - ./data:/app/data         # bind mount
      - app_data:/app/persist    # named volume
    environment:
      - TZ=UTC
    networks:
      - app_net
    depends_on:
      - db
    restart: unless-stopped

networks:
  app_net:
    driver: bridge

volumes:
  app_data:
```

Key fields: `image` vs `build`, `ports` (HOST:CONTAINER), `volumes`, `environment`, `depends_on`, `restart`, `networks`.

# Common commands

```bash
docker compose up -d          # build (if needed) + start in background
docker compose ps            # status of services
docker compose logs -f app   # follow logs for one service
docker compose down          # stop + remove containers/networks
docker compose down -v       # also remove named volumes (DESTRUCTIVE)
docker compose pull          # refresh images
docker compose restart app   # restart a single service
```

# Real example from this machine — Firecrawl (embeds SearXNG + subservices)

This is the actual `programs/firecrawl/firecrawl/docker-compose.yaml`. Note the patterns: a shared `backend` network, a host-port mapping (`8080:8080` for SearXNG), and `depends_on` so Firecrawl starts after its dependencies.

```yaml
version: '3.8'

services:
  searxng:
    image: searxng/searxng:latest
    container_name: agent_searxng
    volumes:
      - ./searxng/settings.yml:/etc/searxng/settings.yml:ro
    ports:
      - "8080:8080"            # host 8080 -> container 8080 (example service)
    networks:
      - agent_network
    restart: always

  cloakbrowser-manager:
    image: cloakhq/cloakbrowser-manager:latest
    container_name: agent_cloakbrowser
    ports:
      - "8080:8080"
    volumes:
      - cloak_profiles:/data
    networks:
      - agent_network
    restart: always

  firecrawl:
    image: mendableai/firecrawl:latest
    container_name: agent_firecrawl
    ports:
      - "3002:3002"
    environment:
      - SEARXNG_URL=http://searxng:8080   # internal container name resolves on the bridge
    networks:
      - agent_network
    depends_on:
      - searxng
      - cloakbrowser-manager

networks:
  agent_network:
    driver: bridge

volumes:
  cloak_profiles:
```

# Real example — Frigate (GPU reservation)

From `programs/frigate/docker-compose.yml`. Notice `privileged: true` for hardware access, `shm_size` for detection buffers, a `tmpfs` RAM cache to reduce drive wear, and the **NVIDIA device reservation** under `deploy.resources` (see [GPU & AI](gpu-ai.md)):

```yaml
services:
  frigate:
    container_name: frigate
    privileged: true
    restart: unless-stopped
    image: ghcr.io/blakeblackshear/frigate:stable
    shm_size: "256mb"
    volumes:
      - /home/daniel/Desktop/programs/frigate/config.yml:/config/config.yml
      - "/media/daniel/New Volume/frigate:/media/frigate"
      - /etc/localtime:/etc/localtime:ro
      - type: tmpfs
        target: /tmp/cache
        tmpfs:
          size: 1000000000
    ports:
      - "8971:8971"
      - "5000:5000"
      - "8554:8554"
      - "8555:8555/tcp"
      - "8555:8555/udp"
    environment:
      - FRIGATE_RTSP_PASSWORD=Sept142025!
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

# Tips

* Use `:ro` on bind mounts you don't want the container to write (e.g. config files).
* Give services a `container_name` so logs/`docker exec` are easy to target.
* Prefer `restart: unless-stopped` over `always` for services you may want to keep down during maintenance.
* Internal service-to-service traffic uses the **service name** as the hostname (e.g. `http://searxng:8080`), never the host port.

# Citations

[1] [Docker Compose overview](https://docs.docker.com/compose/)
[2] [Compose file reference](https://docs.docker.com/compose/compose-file/)
[3] [Local SearXNG config - programs/firecrawl/firecrawl/searxng-config/](/../../programs/firecrawl/firecrawl/searxng-config/)
[4] [Local Frigate compose - programs/frigate/docker-compose.yml](/../../programs/frigate/docker-compose.yml)
