---
type: Concept
title: Hindsight Overview
description: How Hindsight works — agents that learn (compiled memory/learning passes) vs RAG/knowledge-graph recall; LongMemEval SOTA; architecture.
resource: https://hindsight.vectorize.io
tags: [hindsight, overview, memory, learning]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: hindsight-docs
    resource: "https://hindsight.vectorize.io"
    title: "Hindsight docs"
    author: "site:hindsight.vectorize.io"
  - id: paper-arxiv-2512-12818
    resource: "https://arxiv.org/abs/2512.12818"
    title: "Paper (arXiv 2512.12818)"
    author: "site:arxiv.org"
  - id: hindsight-github
    resource: "https://github.com/vectorize-io/hindsight"
    title: "Hindsight GitHub"
    author: "site:github.com"
---

# Hindsight — Overview

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
