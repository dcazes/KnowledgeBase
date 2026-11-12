---
type: Software
title: Docker
description: Container platform — Docker Engine, Compose and Desktop — that packages applications with their dependencies; the default way to self-host the AI tools in this vault, now with built-in local model serving (Model Runner), an MCP gateway and catalog, and Docker Agent.
resource: https://www.docker.com
tags: [docker, containers, compose, self-hosting, model-runner, mcp, runtime]
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
  - id: compose-github
    resource: "https://github.com/docker/compose"
    title: "docker/compose on GitHub"
    author: "site:github.com"
---

# Docker

**Docker** runs software in containers: isolated processes built from layered images that bundle an application with everything it needs. Almost every self-hostable tool in this vault ships a `docker run` line or a `docker-compose.yml`, which makes Docker the foundation of [self-hosting](../../concepts/self-hosting.md) an AI stack. Since 2025 Docker has also added AI-specific features: **Model Runner** for local LLMs, an **MCP Toolkit / Gateway** for tool servers, and **Docker Agent** for YAML-defined agents.

| | |
|---|---|
| Category | Runtime · [Self-hosting](../../concepts/self-hosting.md) |
| License | Engine (Moby) and Compose: Apache-2.0; Docker Desktop: commercial licence for larger companies |
| Latest | Engine 29.9.3 (2026-11-03) · Compose v5.7.1 (2026-11-11) · Model Runner v1.2.9 |
| Platforms | Linux (Engine), macOS / Windows / Linux (Desktop) |

## Contents

* [Overview](overview.md) — architecture and key concepts
* [Installation](installation.md) — Engine vs Desktop, post-install
* [Images & containers](images-containers.md) — lifecycle, Dockerfiles, caching, multi-stage builds
* [Compose](compose.md) — multi-container apps, profiles, `models`, health checks
* [Volumes & networks](volumes-networks.md) — persistence, service discovery, ports
* [Registries](registry.md) — tagging, pushing, pruning, OCI artifacts
* [GPU & AI](gpu-ai.md) — NVIDIA GPUs, Model Runner, MCP Gateway, Docker Agent
* [Snippets](snippets.md) — command cheat sheet

## Related

* Concepts: [Self-hosting](../../concepts/self-hosting.md) · [Local inference](../../concepts/local-inference.md) · [MCP](../../concepts/mcp.md)
* Runs: [Ollama](../ollama/index.md), [vLLM](../vllm/index.md), [SearXNG](../searxng/index.md), [Open WebUI](../../apps/openwebui/index.md), [Dify](../../agents/dify/index.md), [Firecrawl](../../browsers/firecrawl/index.md), [Qdrant](../../databases/qdrant/index.md), [Neo4j](../../databases/neo4j/index.md), [Langfuse](../../observability/langfuse/index.md), [n8n](../../apps/n8n/index.md), [Frigate](../../tools/frigate/index.md)
* Networking: [Tailscale](../tailscale/index.md)
* Comparison: [Runtime alternatives](../alternatives.md)
