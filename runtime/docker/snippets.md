---
type: Playbook
title: Docker — Snippets & Cheat Sheet
description: Copy-paste commands and compose fragments covering the majority of daily Docker use cases on this machine.
resource: https://docs.docker.com/reference/cli/docker/
tags: [docker, snippets, cheat-sheet, reference]
generated: { by: "human:daniel", at: "2026-07-08T22:35:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-08T22:35:00Z" } ]
status: stable
stale_after: 2027-01-04
sources:
  - id: docker-cli-reference
    resource: "https://docs.docker.com/reference/cli/docker/"
    title: "Docker CLI reference"
    author: "site:docs.docker.com"
  - id: compose-cli-reference
    resource: "https://docs.docker.com/reference/cli/docker/compose/"
    title: "Compose CLI reference"
    author: "site:docs.docker.com"
  - id: local-install-run-script-programs-docker
    resource: "/../../programs/docker/"
    title: "Local install / run script - programs/docker/"
---

# Start / verify (your machine)

```bash
systemctl --user start docker-desktop     # from programs/docker/run
docker version
docker run hello-world
```

# Run a container

```bash
docker run -d --name web -p 8080:80 nginx:alpine     # detached, named, port map
docker run -it --rm ubuntu:22.04 /bin/bash           # interactive, auto-remove on exit
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi
```

# Lifecycle

```bash
docker ps -a                      # all containers
docker start web / docker stop web / docker restart web
docker exec -it web /bin/sh      # shell inside running container
docker logs -f web               # follow logs
docker rm -f web                 # force remove
```

# Images

```bash
docker pull nginx:alpine
docker build -t myapp:1.0 .      # build from Dockerfile in cwd
docker image ls
docker tag myapp:1.0 myreg.io/daniel/myapp:1.0
docker push myreg.io/daniel/myapp:1.0
docker image prune -a            # remove unused images
```

# Compose (multi-container)

```bash
docker compose up -d             # start stack in background
docker compose ps                # status
docker compose logs -f <svc>     # follow one service
docker compose down              # stop + remove
docker compose down -v           # + remove volumes (DESTRUCTIVE)
docker compose restart <svc>
```

Minimal compose:

```yaml
services:
  app:
    image: nginx:alpine
    ports: ["8080:80"]
    restart: unless-stopped
```

# Volumes

```bash
docker volume create data
docker volume ls
docker volume inspect data
docker run -v data:/app/data -v $PWD/config.yml:/etc/app/config.yml:ro myapp
docker volume prune
```

# Networks

```bash
docker network create net
docker network ls
docker run --network net --name db postgres:16     # reachable as "db" by peers
docker network prune
```

# Cleanup / disk

```bash
docker system df                 # disk usage
docker system prune -a           # containers + images + networks + cache
docker container prune           # stopped containers only
```

# Inspect / debug

```bash
docker inspect web               # full JSON config
docker stats                     # live resource use
docker top web                   # processes in container
docker diff web                  # filesystem changes vs image
```

# GPU check (GTX 1060)

```bash
nvidia-smi                                          # host
docker exec -it frigate nvidia-smi                  # inside Frigate container
```
