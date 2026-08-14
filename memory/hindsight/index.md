---
type: Reference
title: Hindsight
description: Agent memory system (vectorize-io) — agents that learn, not just remember; SOTA on LongMemEval; Deno/TypeScript monorepo with CLI, API, control plane, integrations.
resource: https://github.com/vectorize-io/hindsight
tags: [hindsight, memory, agents, longmemeval, vectorize]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: hindsight-github
    resource: "https://github.com/vectorize-io/hindsight"
    title: "Hindsight GitHub"
    author: "site:github.com"
  - id: hindsight-docs
    resource: "https://hindsight.vectorize.io"
    title: "Hindsight docs"
    author: "site:hindsight.vectorize.io"
  - id: paper-arxiv-2512-12818
    resource: "https://arxiv.org/abs/2512.12818"
    title: "Paper (arXiv 2512.12818)"
    author: "site:arxiv.org"
---

# Hindsight

An **agent memory system** (by Vectorize) focused on making agents **learn over time, not just recall conversation history** — trained-away from RAG/knowledge-graph shortcomings for long-term memory. Reports **state-of-the-art results on LongMemEval** (per upstream as of Jan 2026). Monorepo: **uv Python workspace** (8 members: hindsight-all, hindsight-api, hindsight-api-slim, hindsight-all-slim, hindsight-dev, hindsight-mcp-server, hindsight-clients/python, hindsight-embed) + **Rust CLI** (`hindsight-cli`, bin `hindsight`) + **Next.js/TS control plane** (`@vectorize-io/hindsight-control-plane`).

Local checkout: `programs/hindsight` (git, vectorize-io, main, commit 2026-07-17) at **v0.8.4**. Sub-packages: `hindsight-cli`, `hindsight-api`, `hindsight-control-plane`, `hindsight-clients`, `hindsight-integrations`, `hindsight-embed`, `hindsight-tools`, `docker/`, `helm/`, `skills/`, `cookbook/`. **Not deployed** as of 2026-08-13.

## Contents

* [Overview](overview.md) — learn vs remember, memory architecture, benchmark position
* [Installation](installation.md) — Rust CLI (`hindsight`), Python API (uv), npm `@vectorize-io/hindsight-all`, or control-plane deploy (Docker/Helm); verify
* [Configuration](configuration.md) — control plane + API settings, model config, persistence
* [AI Integration](ai-integration.md) — agent SDK/clients, skills, integrations, vs Graphiti/Mem0
* [Snippets](snippets.md) — CLI, client calls, API probes cheat sheet
* [Alternatives](../alternatives.md) — Graphiti, Mem0, MemOS, Zep, LangMem vs Hindsight

## Related

* [Graphiti](../graphiti/index.md), [Mem0](../mem0/index.md), [MemOS](../memos/index.md) — the other agent-memory systems in this vault
* [Architecture → Memory comparison](../alternatives.md)

## Last verified

**2026-08-13** — Local checkout `programs/hindsight` v0.8.4 (git, vectorize-io, 2026-07-17); not deployed. Grounded on local checkout README/package versions + upstream docs.
