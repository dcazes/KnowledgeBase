---
type: Reference
title: Agent Stack
description: All-in-one Docker Compose prototype wiring the agentic stack (SearXNG, Firecrawl, Camofox, Frigate, Ollama, LiteLLM, Graphiti, Weaviate) on one agent-net network.
resource: https://github.com/mendableai/firecrawl
tags: [agent-stack, docker-compose, prototype, litellm, docling, mineru]
timestamp: 2026-08-12T00:00:00Z
---

# Agent Stack

All-in-one prototype that wires the whole agentic stack into **one** Docker Compose using `include` — SearXNG, Firecrawl, Camofox, Frigate, Ollama, LiteLLM, Graphiti MCP (FalkorDB), and Weaviate — so a single `docker compose up -d` brings everything up on one `agent-net` network.

> **STATUS: PROTOTYPE / TEMPLATE.** This is a *code prototype* — it is **not deployed** on this machine. Secrets are placeholders (`CHANGE_ME`); never commit real values. The individual services also have their own standalone composes (see each program's card).

## Contents

* [Overview](overview.md) — what the agent stack is, the architectural decisions, the integration map
* [Installation](installation.md) — how to run the whole stack from one compose (the `include` pattern), deploy steps, env setup
* [AI Integration](ai-integration.md) — how each component connects (Weaviate, Graphiti, Docling/MinerU, Ollama, LiteLLM, browsers)
* [Notes](notes.md) — per-service rationale, locked decisions, gaps, local-model plan
* Prototype config (committed here, not deployed):
  * `docker-compose.yml` — the all-in-one compose (includes existing composes + adds new services)
  * `.env.example` — all environment variables (copy → `.env`, fill in)
  * `searxng-settings.yml` — SearXNG settings mounted into the `searxng` service
  * `litellm/config.yaml` — LiteLLM `:4000` proxy config
  * `parser-service/` — Docling/MinerU parser wrapper (Dockerfiles + wrapper script)

## Instance facts (from config, not live state)

* **Network:** all services share `agent-net` (bridge) and reach each other by service name (e.g. `http://searxng:8080`, `http://litellm:4000`, `http://weaviate:8080`).
* **Host ports exposed:** `8080` (SearXNG), `3002` (Firecrawl), `9377`/`6080` (Camofox), `11434` (Ollama), `4000` (LiteLLM), `8000` (Graphiti MCP), `8087` (Weaviate), `15672` (RabbitMQ mgmt).
* **Locked decisions:** memory = **Graphiti** (FalkorDB), search backend = **Weaviate** (start; Vespa optional), parsers = **Docling** v2.119.0 (+ **MinerU** v3.1.0 for scans — license changed from AGPLv3 to the "MinerU Open Source License", Apache-2.0-based), LLM gateway = **LiteLLM** v1.96.0 `:4000`.

## Cross-references

* Individual services have their own standalone notes — see [Firecrawl](../firecrawl/index.md), [SearXNG](../searxng/index.md), [Frigate](../frigate/index.md), [Camofox](../camofox/index.md), [CloakBrowser](../cloakbrowser/index.md), [Graphiti](../graphiti/index.md), [MemOS](../memos/index.md), [OpenWebUI](../openwebui/index.md), [Dify](../dify/index.md), [Tailscale](../tailscale/index.md).
* The blueprint that motivated this: [Agentic System Blueprint](../architecture/agentic-system-blueprint.md)
* Search-backend comparison: [Vespa vs Weaviate](../architecture/search-backend/vespa-vs-weaviate.md)
* Memory comparison: [Graphiti vs Mem0](../architecture/memory/memory-comparison.md)

## Last verified

**2026-08-12** — Version pins refreshed (LiteLLM v1.96.0, Docling v2.119.0, MinerU v3.1.0). Prototype compose, env, and integration docs originally verified 2026-07-09 against upstream (Firecrawl 6-svc, Graphiti MCP FalkorDB, Weaviate end-user, SearXNG-docker, Camofox, Ollama, LiteLLM). Flattened from `architecture/agent-stack/` into this top-level `agent-stack/` folder on 2026-07-16 to match the one-folder-per-program convention.

# Citations

[1] [Firecrawl repo](https://github.com/mendableai/firecrawl)
[2] [Graphiti MCP](https://github.com/getzep/graphiti/tree/main/mcp_server)
[3] [Weaviate install](https://weaviate.io/developers/weaviate/installation/docker-compose)
[4] [SearXNG-docker](https://github.com/searxng/searxng-docker)
[5] [Camofox](https://github.com/camofox/camofox)
[6] [Ollama](https://github.com/ollama/ollama)
[7] [LiteLLM](https://github.com/BerriAI/litellm)
[8] [Blueprint](../architecture/agentic-system-blueprint.md)
