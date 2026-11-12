---
type: Concept
title: Self-Hosting AI
description: Running an AI stack on your own infrastructure — why (privacy, cost, control), the layers (models, gateway, data, apps, agents), Docker Compose as glue, private networking, backups, updates and security baselines.
resource: https://docs.docker.com
tags: [concept, self-hosting, homelab, docker, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docker-docs
    resource: "https://docs.docker.com"
    title: "Docker documentation"
    author: "site:docs.docker.com"
  - id: tailscale-kb
    resource: "https://tailscale.com/kb"
    title: "Tailscale knowledge base"
    author: "site:tailscale.com"
---

# Self-Hosting AI

Most tools in this vault can run on your own hardware. Self-hosting trades convenience for **privacy** (data never leaves), **cost control** (no per-token fees for local models), **availability offline** and **freedom to customise**.

## A reference stack

| Layer | Options here |
|---|---|
| Models | [Ollama](../runtime/ollama/index.md), [vLLM](../runtime/vllm/index.md), [llama.cpp](../runtime/llamacpp/index.md), [LM Studio](../runtime/lmstudio/index.md) — [Local inference](local-inference.md) |
| Gateway | [LiteLLM](../runtime/litellm/index.md) |
| Data | [Qdrant](../databases/qdrant/index.md), [pgvector](../databases/pgvector/index.md), [Neo4j](../databases/neo4j/index.md) |
| Memory | [Mem0](../memory/mem0/index.md), [Graphiti](../memory/graphiti/index.md), [Honcho](../memory/honcho/index.md), [Hindsight](../memory/hindsight/index.md), [Cognee](../memory/cognee/index.md) |
| Web | [SearXNG](../runtime/searxng/index.md), [Firecrawl](../browsers/firecrawl/self-hosting.md), [Crawl4AI](../browsers/crawl4ai/index.md) |
| Apps | [Open WebUI](../apps/openwebui/index.md), [AnythingLLM](../apps/anythingllm/index.md), [n8n](../apps/n8n/index.md), [Dify](../agents/dify/index.md) |
| Agents | [Hermes](../agents/hermes/index.md), [OpenClaw](../agents/openclaw/index.md), [OpenCode](../agents/opencode/index.md) |
| Observability | [Langfuse](../observability/langfuse/index.md) |

[Docker Compose](../runtime/docker/compose.md) ties services together; [Tailscale](../runtime/tailscale/index.md) gives private access from your devices.

## Baselines

* Bind services to `127.0.0.1` or the private network; many AI servers ship without authentication.
* Pin image versions; read release notes for breaking changes (e.g. [Dify](../agents/dify/installation.md), [Frigate](../tools/frigate/installation.md)).
* Back up volumes (databases, model caches are re-downloadable, memories are not).
* Keep secrets in `.env` files outside git.
* Watch GPU memory: several model servers on one GPU compete.

## Related

[Agent security](agent-security.md) · [Runtime alternatives](../runtime/alternatives.md) · [Concepts index](index.md)
