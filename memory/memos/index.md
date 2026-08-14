---
type: Reference
title: MemOS
description: Memory operating system for LLM agents — unifies store/retrieve/manage for long-term memory with vector + graph storage, runs as Python library, FastAPI service, and MCP server.
resource: https://github.com/MemTensor/MemOS
tags: [memos, memory, agents, mcp, llm]
timestamp: 2026-08-12T00:00:00Z
---

# MemOS

A **memory operating system** for LLM agents — unifies store / retrieve / manage for long-term memory (textual, tree, preference, skill, KV-cache, LoRA parametric), with scheduling, versioning, and vector + graph storage. Runs as a Python library, a FastAPI service, and an MCP server. PyPI distribution is `MemoryOS` (import name `memos`); no local checkout exists in `programs/` as of 2026-08-12.

> **Deployment note:** on this machine MemOS is **not yet deployed** — there is no `programs/memos` checkout (verified 2026-08-12); the deploy path is `pip install MemoryOS` then run via uvicorn (port 8000, `/health`), or the Docker path in `docker/docker-compose.yml`. See [Installation](installation.md).

## Contents

* [Overview](overview.md) — what MemOS is, memory types, architecture, provider model
* [Installation](installation.md) — `pip install MemoryOS` (import `memos`), uvicorn :8000 or Docker (API + Neo4j + Qdrant); verify with `/health`
* [Configuration](configuration.md) — `.env` model routing (big LLM for write-path, 4B local embed/rerank), MemCube scoping, feedback/correction
* [Benchmarks](benchmarks.md) — OmniMemEval scores (LoCoMo 88.83, LongMemEval 89.20), small-model caveat, vs Mem0/Graphiti/EverOS
* [AI Integration](ai-integration.md) — MCP server for Hermes/OpenCode/Cursor; pairs with Graphiti; official Hermes & OpenClaw local plugins
* [Snippets](snippets.md) — install / serve / API calls / Python `MOS` usage cheat sheet
* [Alternatives](alternatives.md) — Graphiti, Mem0, Zep, LangMem vs MemOS

## Instance facts (from config, not live state)

* **Import name:** `memos` (distribution `MemoryOS`, **v2.0.27** as of 2026-07-31). CLI: `memos`.
* **API entry:** `memos.api.server_api:app` (FastAPI). Port **8000**; health at `GET /health`.
* **Run from:** pip-installed `MemoryOS` → `uvicorn memos.api.server_api:app` (or Docker path).
* **Backends:** vector DB (Qdrant / Milvus), graph DB (Neo4j / Postgres / Nebula), LLM + embedder configurable (Ollama, OpenAI, vLLM, …).
* **MCP server:** shipped under `src/memos/api/` — register in any MCP client for memory.

## Cross-references

* **Graphiti** is the other memory layer in this stack — [Graphiti](../graphiti/index.md). MemOS = structured/textual/preference/skill memory; Graphiti = temporal context graph.
* The agent stack wires both — [Agent Stack](../../agents/agent-stack/index.md).
* Local deploy path: `pip install MemoryOS`; no `programs/memos` checkout exists as of 2026-08-12.

## Last verified

**2026-08-12** — Version bumped to **v2.0.27**; corrected stale claim that a local checkout exists at `programs/memos` (verified absent 2026-08-12 — deploy via pip `MemoryOS`). Prior verification 2026-07-16 against upstream docs/repo.

# Citations

[1] [MemOS repo](https://github.com/MemTensor/MemOS)
[2] [MemOS docs](https://memos-docs.openmem.net/home/overview/)
[3] [PyPI — MemoryOS](https://pypi.org/project/MemoryOS/)
[4] [OmniMemEval / EverMem benchmarks](https://github.com/MemTensor/MemOS)
