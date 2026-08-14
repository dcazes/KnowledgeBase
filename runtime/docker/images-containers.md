---
type: Reference
title: Docker — Images & Containers
description: The core lifecycle (build/pull/run/exec/stop/rm), Dockerfile essentials, and how layer caching keeps builds fast.
resource: https://docs.docker.com/get-started/docker-concepts/building-images/
tags: [docker, images, containers, dockerfile]
generated: { by: "human:daniel", at: "2026-07-08T22:35:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-08T22:35:00Z" } ]
status: stable
stale_after: 2027-01-04
sources:
  - id: docker-building-images-concepts
    resource: "https://docs.docker.com/get-started/docker-concepts/building-images/"
    title: "Docker building images concepts"
    author: "site:docs.docker.com"
  - id: dockerfile-reference
    resource: "https://docs.docker.com/reference/dockerfile/"
    title: "Dockerfile reference"
    author: "site:docs.docker.com"
  - id: best-practices-for-writing-dockerfiles
    resource: "https://docs.docker.com/build/building/best-practices/"
    title: "Best practices for writing Dockerfiles"
    author: "site:docs.docker.com"
  - id: docker-exec-reference
    resource: "https://docs.docker.com/reference/cli/docker/container/exec/"
    title: "docker exec reference"
    author: "site:docs.docker.com"
---

# Docker — Lifecycle commands

```bash
# Pull an image from a registry
docker pull nginx:alpine

# Run a container (detached, named, port-mapped)
docker run -d --name web -p 8080:80 nginx:alpine

# List running / all containers
docker ps
docker ps -a

# Shell into a running container
docker exec -it web /bin/sh

# Stream logs
docker logs -f web

# Stop and remove
docker stop web
docker rm web

# Remove an image
docker rmi nginx:alpine
```

# Dockerfile essentials

A `Dockerfile` defines how to build an image. Key instructions:

| Instruction | Purpose |
|-------------|---------|
| `FROM <image>` | Base image (start here). Use slim/alpine when possible. |
| `WORKDIR /app` | Set the working directory for subsequent steps. |
| `COPY . /app` | Copy files from build context into the image. |
| `RUN <cmd>` | Execute at build time (install deps, compile). |
| `ENV KEY=val` | Set environment variables. |
| `EXPOSE 8080` | Document a port (does not publish it). |
| `CMD ["exec","arg"]` | Default command run when the container starts. |
| `ENTRYPOINT` | Fixed command; `CMD` becomes its args. |

Minimal example:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run it:

```bash
docker build -t myapp:1.0 .
docker run -d --name myapp -p 8000:8000 myapp:1.0
```

# Layer caching (the thing that makes builds fast)

Every Dockerfile line = one **layer**. Docker caches layers and only rebuilds a layer (and everything after it) when its instruction or inputs change. Optimize by ordering:

1. Put rarely-changing steps first (`FROM`, system deps).
2. Copy dependency manifests and install **before** copying source code.
3. Copy source last.

```dockerfile
COPY requirements.txt .      # changes often? no -> cached
RUN pip install -r requirements.txt
COPY . .                     # source changes -> only this + later rebuild
```

Use `.dockerignore` to keep the build context small (exclude `.git`, `node_modules`, `venv`).

# Multi-stage builds (smaller final images)

```dockerfile
FROM node:22 AS build
WORKDIR /app
COPY . .
RUN npm ci && npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

# Inspecting

```bash
docker image ls
docker image history myapp:1.0     # see layer sizes
docker inspect web                 # full JSON config/state
docker stats                       # live CPU/mem/IO per container
```
