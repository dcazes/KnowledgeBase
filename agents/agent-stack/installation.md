---
type: Playbook
title: Agent Stack — Installation & Deployment
description: Run the whole agentic stack from one Docker Compose using the include pattern; set up env, pull images, bring it up.
resource: https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/
tags: [agent-stack, install, docker, compose, include, deployment]
timestamp: 2026-07-09T00:00:00Z
---

# Deployment model

The Agent Stack is a **single master compose** that `include`s each program's existing compose and adds the new services (Weaviate, Ollama, LiteLLM, Graphiti/FalkorDB, parser). This keeps each program as its own source of truth — no duplicated configs or rebuilt images.

> **STATUS: PROTOTYPE / TEMPLATE — NOT deployed on this machine.** Fill `.env` before any real deploy.

# The include pattern (recommended)

A top-level `docker-compose.yml` with:

```yaml
include:
  - programs/firecrawl/firecrawl/docker-compose.yaml   # searxng + firecrawl + subservices
  - programs/frigate/docker-compose.yml                # frigate
  - ./new-services.yml                                  # weaviate/ollama/litellm/graphiti/parser
```

Compose merges them into one project (`name: agent-stack`). Each service keeps its own source of truth; nothing is duplicated. The committed `docker-compose.yml` here follows this pattern (network `agent-net`, shared volumes).

# Start / stop

Run from `kbv2/agent-stack/`:

```bash
cd kbv2/agent-stack
cp .env.example .env          # fill every CHANGE_ME
docker compose up -d          # bring up the whole stack
docker compose ps             # check status
docker compose logs -f        # follow logs
docker compose down           # stop (keeps volumes)
```

# What you still need to obtain (NOT downloaded — plan only)

| Component | How to get it |
|-----------|---------------|
| Weaviate | `docker pull semitechnologies/weaviate:latest` |
| Ollama | `docker pull ollama/ollama:latest` then `ollama pull nomic-embed-text` + `qwen2.5-coder:3b` |
| LiteLLM | `docker pull ghcr.io/berriai/litellm:main-latest` |
| Graphiti MCP + FalkorDB | `docker pull getzep/graphiti-mcp:latest` + `docker pull falkordb/falkordb:latest` |
| Docling / MinerU | build from `parser-service/Dockerfile.*` (or `pip install`) |
| Free-tier API keys | OpenRouter / Groq / Google AI Studio → put in `.env` |

**Already present, no action:** SearXNG, Firecrawl (+subservices), OpenWebUI, Camofox, Frigate, Tailscale (binary), CloakBrowser.

# Avoid duplicate copies

* **Images:** reference by existing name/tag (e.g. `mendableai/firecrawl:latest`, `camofox-browser:134...`). Don't rebuild.
* **Configs:** mount the real files — SearXNG: `./searxng-settings.yml:/etc/searxng/settings.yml:ro`; Frigate: `programs/frigate/config.yml`; Firecrawl: reuse its existing `.env` + compose via `include`.
* **Networks:** one shared `agent-net`; fragments join via `external: true`.
* **Data:** keep volumes under one root so state isn't scattered.

# Verify it is up

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080/        # SearXNG
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:3002/        # Firecrawl
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8000/health  # Graphiti MCP
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8087/        # Weaviate
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:4000/health  # LiteLLM
```

# Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Service won't start | missing image | `docker pull` the component |
| Auth/secret errors | `.env` still has `CHANGE_ME` | fill every placeholder before `up` |
| Cross-service name fails | wrong network | ensure all fragments join `agent-net` (`external: true`) |
| GPU not used by Ollama | nvidia runtime absent | install nvidia-container-toolkit |

# Citations

[1] [Compose include / merge spec](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/)
[2] [Firecrawl master compose](/../../programs/firecrawl/firecrawl/docker-compose.yaml)
[3] [Frigate compose](/../../programs/frigate/docker-compose.yml)
