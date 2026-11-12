---
type: Reference
title: Docker Snippets
description: Docker command cheat sheet — containers, images, Compose, volumes, networks, cleanup, debugging, GPUs and Model Runner.
resource: https://docs.docker.com/reference/cli/docker/
tags: [docker, snippets, cli, cheat-sheet]
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

# Docker — Snippets

```bash
# containers
docker run -d --name app -p 127.0.0.1:8080:80 nginx
docker ps -a ; docker logs -f app ; docker exec -it app sh
docker stop app && docker rm app
docker restart app ; docker stats

# images
docker pull image:tag ; docker images ; docker rmi image:tag
docker build -t me/app:dev . ; docker image prune -a

# compose
docker compose up -d ; docker compose logs -f svc ; docker compose down
docker compose pull && docker compose up -d     # update
docker compose exec svc sh

# volumes & networks
docker volume ls ; docker volume inspect v
docker network ls ; docker network inspect bridge

# disk
docker system df ; docker system prune

# debug
docker inspect app --format '{{.State.Health.Status}}'
docker events --since 10m

# GPU
docker run --rm --gpus all nvidia/cuda:12.6.0-base-ubuntu24.04 nvidia-smi

# models & agents
docker model pull ai/gemma3 ; docker model run ai/gemma3 "hi"
docker agent run agent.yaml
```

## Related

[Docker index](index.md) · [Compose](compose.md)
