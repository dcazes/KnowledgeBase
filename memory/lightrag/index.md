---
type: Reference
title: LightRAG
description: Lightweight, graph-powered RAG engine (HKUDS) — dual-level retrieval over an incremental knowledge graph, local or cloud LLMs, Python library + server.
resource: https://github.com/HKUDS/LightRAG
tags: [lightrag, rag, graph, retrieval, llm, knowledge]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: lightrag-github
    resource: "https://github.com/HKUDS/LightRAG"
    title: "LightRAG GitHub"
    author: "site:github.com"
  - id: lightrag-docs
    resource: "https://lightrag.readthedocs.io/en/latest/"
    title: "LightRAG docs"
    author: "site:lightrag.readthedocs.io"
  - id: lightrag-on-pypi
    resource: "https://pypi.org/project/lightrag-hku/"
    title: "LightRAG on PyPI"
    author: "site:pypi.org"
  - id: paper-arxiv-2410-05779
    resource: "https://arxiv.org/abs/2410.05779"
    title: "Paper (arXiv 2410.05779)"
    author: "site:arxiv.org"
---

# LightRAG

A **lightweight, graph-powered RAG engine** (by HKUDS) that builds an incremental knowledge graph from documents and retrieves with dual-level (low-level/keyword + high-level/entity) search — producing answers grounded in both specific facts and overall themes. Runs as a Python library or as a FastAPI server (`lightrag-server`), local or cloud LLMs.

Local checkout: `programs/LightRAG` (git, HKUDS, main, commit 2026-07-21) at **v1.5.5**; latest on PyPI is **v1.5.6** (`pip install lightrag-hku`). Not deployed as a service on this machine as of 2026-08-13; the checkout includes `docker-compose.yml` / `docker-compose-full.yml` for server deployments.

## Contents

* [Overview](overview.md) — what LightRAG is, graph construction, dual-level retrieval, query modes
* [Installation](installation.md) — `pip install lightrag-hku` or server via Docker; verify
* [Configuration](configuration.md) — working dir, LLM/embedding providers (Ollama/OpenAI), storage backends, chunk settings
* [AI Integration](ai-integration.md) — Python API, REST server, MCP-ish wiring into Hermes/OpenCode, vs GraphRAG
* [Snippets](snippets.md) — insert docs / query / incremental updates / server calls cheat sheet
* [Alternatives](alternatives.md) — GraphRAG (Microsoft), LlamaIndex, Mem0/MemOS memory graphs, vs LightRAG

## Related

* [Graphiti](../graphiti/index.md) — temporal graph for agent memory (different job: memory vs retrieval)
* [Graphify](../graphify/index.md) — folder→knowledge-graph compiler (offline; LightRAG is query-time RAG)
* [Ollama](../../runtime/ollama/index.md) — local LLM backend for LightRAG

## Last verified

**2026-08-13** — Local checkout `programs/LightRAG` v1.5.5 (PyPI latest v1.5.6); not deployed as a service. Docs ground on the local checkout (recon 2026-08-12) + upstream docs.
