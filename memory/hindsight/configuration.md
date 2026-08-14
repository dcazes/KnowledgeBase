---
type: HowTo
title: Hindsight Configuration
description: Configure Hindsight — control plane + API settings, model/LLM config, persistence, agent SDK options; what's in the v0.8.4 checkout.
resource: https://hindsight.vectorize.io
tags: [hindsight, configuration, control-plane, api]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: hindsight-docs-configuration
    resource: "https://hindsight.vectorize.io"
    title: "Hindsight docs — configuration"
    author: "site:hindsight.vectorize.io"
  - id: hindsight-github
    resource: "https://github.com/vectorize-io/hindsight"
    title: "Hindsight GitHub"
    author: "site:github.com"
---

# Configuration

Configuration is split between the **control plane** (orchestration) and the **API** (service layer), per the repo layout.

## LLM / model config

```env
# typical service env (see hindsight-api / control-plane env templates in repo)
LLM_API_KEY=sk-...
LLM_MODEL=gpt-4o            # or anthropic/ollama per support
EMBEDDING_MODEL=...
```

## Persistence

Server deployments use the `docker/` compose (Postgres or similar backing store — see the compose files in the checkout) and `helm/` for Kubernetes; volumes/state configured there.

## Agent integration config

* `hindsight-clients` — SDKs configure base URL + auth for API/control-plane.
* `hindsight-integrations` — drop-in config for supported agent frameworks.
* `skills/` — agent skills ship in the repo and are wired via your agent's skill/MCP config.

## CLI config

CLI reads env or a local config for API endpoint + keys (per `hindsight-cli` docs in checkout).

> The checkout is **not deployed** here (2026-08-13) — config files are templates in the repo, not live env on this machine.
