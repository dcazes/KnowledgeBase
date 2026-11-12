---
type: Concept
title: Docker Overview
description: How Docker works — client, daemon, containerd and runc; images, layers, containers, volumes, networks and registries; and when containers are the right tool.
resource: https://docs.docker.com/get-started/docker-overview/
tags: [docker, overview, architecture, containers]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docker-docs
    resource: "https://docs.docker.com"
    title: "Docker documentation"
    author: "site:docs.docker.com"
  - id: moby-github
    resource: "https://github.com/moby/moby"
    title: "moby/moby (Docker Engine)"
    author: "site:github.com"
---

# Docker — Overview

## Architecture

```
docker CLI ──REST──▶ dockerd ──▶ containerd ──▶ runc ──▶ container process
                       │
                       └─ images, volumes, networks, build cache (BuildKit)
```

* **Client** (`docker`) sends commands to the **daemon** (`dockerd`) over a socket.
* The daemon delegates container lifecycle to **containerd**, which uses **runc** to create Linux namespaces and cgroups.
* **Docker Desktop** runs the same engine in a lightweight VM on macOS and Windows (and optionally Linux) and adds a GUI, extensions, Model Runner and the MCP Toolkit.

## Key concepts

| Concept | Meaning |
|---|---|
| Image | Read-only, layered filesystem + metadata, built from a Dockerfile |
| Container | A running (or stopped) instance of an image with a writable layer |
| Volume | Persistent storage that outlives containers |
| Network | Virtual network; containers on the same user-defined network resolve each other by name |
| Registry | Stores and distributes images (Docker Hub, GHCR, private registries) |
| Compose | Declarative multi-container applications in YAML |

## When to use it

* Running third-party services (vector databases, chat UIs, search engines) without polluting the host.
* Reproducible environments and one-command stacks with [Compose](compose.md).
* GPU workloads with the NVIDIA Container Toolkit ([GPU & AI](gpu-ai.md)).

Containers share the host kernel: they isolate processes, but are not a strong security boundary for untrusted code. For running agent-generated code, see sandboxing in [Agent security](../../concepts/agent-security.md).

## Related

[Docker index](index.md) · [Images & containers](images-containers.md) · [Self-hosting](../../concepts/self-hosting.md)
