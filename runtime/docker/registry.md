---
type: Reference
title: Docker — Registry & Images
description: Image registries (Docker Hub, private), tagging strategy, push/pull, and safe pruning of disk space.
resource: https://docs.docker.com/docker-hub/
tags: [docker, registry, images, hub, tagging]
generated: { by: "human:daniel", at: "2026-07-08T22:35:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-08T22:35:00Z" } ]
status: stable
stale_after: 2027-01-04
sources:
  - id: docker-hub
    resource: "https://docs.docker.com/docker-hub/"
    title: "Docker Hub"
    author: "site:docs.docker.com"
  - id: docker-tag-reference
    resource: "https://docs.docker.com/reference/cli/docker/image/tag/"
    title: "docker tag reference"
    author: "site:docs.docker.com"
  - id: docker-pull-reference
    resource: "https://docs.docker.com/reference/cli/docker/image/pull/"
    title: "docker pull reference"
    author: "site:docs.docker.com"
  - id: ghcr-github-container-registry
    resource: "https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry"
    title: "GHCR (GitHub Container Registry)"
    author: "site:docs.github.com"
---

# Registries

A **registry** stores and distributes images.

* **Docker Hub** (`docker.io`) — the default public registry. `nginx` actually means `docker.io/library/nginx`.
* **GitHub Container Registry** (`ghcr.io`) — used by Frigate (`ghcr.io/blakeblackshear/frigate:stable`).
* **Private / self-hosted** — e.g. a registry you run yourself, or cloud registries (GCR, ECR, ACR).

# Tagging

Tags identify a specific image version. Always pin a tag (avoid relying on `:latest` in production):

```bash
docker pull nginx:1.27-alpine
docker tag myapp:1.0 myreg.io/daniel/myapp:1.0
```

# Push / pull

```bash
docker login                                    # authenticate to a registry
docker pull ghcr.io/blakeblackshear/frigate:stable
docker push myreg.io/daniel/myapp:1.0
```

# Image management & pruning

Images accumulate fast. Keep disk usage in check:

```bash
docker image ls
docker image prune              # remove dangling (<none>) images
docker image prune -a           # remove all unused images (not in any container)
docker system df                # see space used by images/volumes/containers
```

# Tips

* Pin versions in compose (`image: searxng/searxng:2024.x` instead of `:latest`) so updates are deliberate.
* Use digest pinning for reproducibility: `image: repo/app@sha256:abc...`.
* `docker system prune -a` is the nuclear option — combine with `--volumes` only if you mean to wipe data.
