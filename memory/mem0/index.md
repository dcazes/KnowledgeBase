---
type: Reference
title: Mem0
description: Production memory layer for AI agents — self-hostable memory service with vector storage, graph memory, and per-user/per-agent scoping; OpenMemory app, API, and SDKs.
resource: https://github.com/mem0ai/mem0
tags: [mem0, memory, agents, vector, graph, llm]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: mem0-github
    resource: "https://github.com/mem0ai/mem0"
    title: "Mem0 GitHub"
    author: "site:github.com"
  - id: mem0-docs
    resource: "https://docs.mem0.ai"
    title: "Mem0 docs"
    author: "site:docs.mem0.ai"
  - id: mem0-on-pypi
    resource: "https://pypi.org/project/mem0ai/"
    title: "Mem0 on PyPI"
    author: "site:pypi.org"
  - id: openmemory-self-hosted-app
    resource: "https://github.com/mem0ai/OpenMemory"
    title: "OpenMemory (self-hosted app)"
    author: "site:github.com"
---

# Mem0

A **production memory layer for AI agents** — captures, stores, and retrieves facts about users and conversations (with built-in conflict resolution) so agents remember across sessions. Supports vector + graph storage backends, per-user / per-agent / per-run scoping, and ships an OpenMemory web app, a REST API, and Python/JS SDKs.

Local checkout: `programs/mem0` (git, mem0ai, main, commit 2026-07-20) at **v2.0.12**; latest on PyPI is **v2.0.18** (`pip install mem0ai`, uploaded 2026-08-11). The local checkout is present but **not deployed** as of 2026-08-13 — no running containers, no installed service. This is the platform-class competitor to [MemOS](../memos/index.md), [Graphiti](../graphiti/index.md), and [Zep](https://www.getzep.com/).

## Contents

* [Overview](overview.md) — what Mem0 is, memory pipeline (ADD/UPDATE/DELETE/GET/SEARCH), storage backends, scoping
* [Installation](installation.md) — `pip install mem0ai` (v2.0.18) or local v2.0.12; OpenMemory app via Docker; verify
* [Configuration](configuration.md) — `.env` provider keys, `config.json` vector store / graph store / embedding model, defaults
* [AI Integration](ai-integration.md) — Python/JS SDKs, OpenMemory API, MCP-ish integration for Hermes/OpenCode, vs MemOS
* [Snippets](snippets.md) — add / get / search / update memory, scoped searches, OpenMemory HTTP calls
* [Alternatives](../alternatives.md) — MemOS, Graphiti, Zep, LangMem, Mem0 vs each other

## Related

* [MemOS](../memos/index.md) — the other local memory platform (deployed-via-pip, different architecture)
* [Graphiti](../graphiti/index.md) — temporal context graphs for the same agent-memory job
* [Architecture → Memory comparison](../alternatives.md)

## Last verified

**2026-08-13** — Local checkout `programs/mem0` v2.0.12 (PyPI latest v2.0.18); not deployed on this machine. Docs ground on the local checkout (recon 2026-08-12) + upstream docs.mem0.ai.
