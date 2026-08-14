---
type: Concept
title: Hindsight Overview
description: How Hindsight works — agents that learn (compiled memory/learning passes) vs RAG/knowledge-graph recall; LongMemEval SOTA; architecture.
resource: https://hindsight.vectorize.io
tags: [hindsight, overview, memory, learning]
timestamp: 2026-08-13T00:00:00Z
---

# Overview

Most agent memory systems **recall conversation history**; Hindsight makes agents that **learn** — distilling experience into lasting memory and improving behavior over time.

## Core idea

* **Learn, not just remember** — memory passes compile what happened into reusable knowledge (facts, skills, preferences) rather than returning raw transcripts.
* **Beyond RAG / knowledge graphs** — upstream argues RAG retrieves text and graphs capture static relations; Hindsight focuses on learning loops suited to long-term agent behavior.

## Benchmark position

SOTA on **LongMemEval** (long-term conversational memory benchmark), reported by upstream as of Jan 2026 — the headline claim in the README.

## Repository layout (v0.8.4)

| Package | Role |
|---|---|
| `hindsight-cli` | command-line interface |
| `hindsight-api` | API server (also `hindsight-api-slim`) |
| `hindsight-control-plane` | orchestration/control plane |
| `hindsight-clients` | language SDKs |
| `hindsight-integrations` | framework/agent integrations |
| `hindsight-embed` | embedding support |
| `hindsight-tools` | agent tools |
| `hindsight-all` / `hindsight-all-npm` / `hindsight-all-slim` | aggregated builds |
| `docker/`, `helm/` | deployment manifests |
| `skills/`, `cookbook/` | agent skills + examples |

Deno-first (TypeScript) with Python parts under `uv.lock`/`pyproject.toml`.

## Deployment model

CLI for local use; API + control plane for server deployments (Docker/Helm provided). **Not deployed** on this machine (2026-08-13).

# Citations

[1] [Hindsight docs](https://hindsight.vectorize.io)
[2] [Paper (arXiv 2512.12818)](https://arxiv.org/abs/2512.12818)
[3] [Hindsight GitHub](https://github.com/vectorize-io/hindsight)
