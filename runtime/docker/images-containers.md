---
type: Reference
title: Docker Images & Containers
description: Working with Docker images and containers — lifecycle commands, Dockerfile essentials, layer caching, multi-stage builds, health checks and inspection.
resource: https://docs.docker.com/build/
tags: [docker, images, containers, dockerfile, buildkit]
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

# Docker — Images & Containers

## Lifecycle

```bash
docker pull qdrant/qdrant:latest
docker run -d --name qdrant -p 6333:6333 -v qdrant_data:/qdrant/storage qdrant/qdrant
docker ps -a
docker logs -f qdrant
docker exec -it qdrant sh
docker stop qdrant && docker rm qdrant
```

## Dockerfile essentials

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt   # cached unless requirements change
COPY . .
USER 1000
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Layer caching:** each instruction is a layer; put rarely-changing steps (dependencies) before often-changing ones (source code).

## Multi-stage builds

```dockerfile
FROM node:22 AS build
WORKDIR /src
COPY . .
RUN npm ci && npm run build

FROM nginx:alpine
COPY --from=build /src/dist /usr/share/nginx/html
```

The final image contains only the build output, not the toolchain.

## Inspecting

```bash
docker inspect qdrant            # full JSON config
docker stats                     # live CPU / memory
docker image history <image>     # layers and sizes
docker buildx build --platform linux/amd64,linux/arm64 -t me/app:1.0 --push .
```

## Related

[Docker index](index.md) · [Compose](compose.md) · [Registries](registry.md)
