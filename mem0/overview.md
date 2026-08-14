---
type: Concept
title: Mem0 Overview
description: How Mem0 works — memory pipeline (ADD/UPDATE/DELETE/GET/SEARCH), storage backends (vector + graph), per-user/per-agent scoping, OpenMemory app vs library.
resource: https://docs.mem0.ai
tags: [mem0, memory, agents, pipeline, vector, graph]
timestamp: 2026-08-13T00:00:00Z
---

# Overview

Mem0 is a **memory layer for LLM agents**: it turns raw conversation/context into structured, persistent, queryable memory that agents can reuse across sessions. It is "MemGPT-style" memory management made self-hostable — the PyPI package `mem0ai` (import `mem0`).

## Memory pipeline

The core API is five operations (mirroring a database):

* **ADD** — store a new memory about a user/agent/run (text + metadata + embeddings).
* **UPDATE** — replace an existing memory (with conflict resolution on `memory_id`).
* **DELETE** — remove a memory by `memory_id`.
* **GET** — list all memories for a user/agent (optionally filtered).
* **SEARCH** — semantic search over memory, scoped by user/agent/run or globally, with optional filters.

Conflicts: when ADD collides with an existing similar memory, Mem0 merges/updates rather than duplicating (configurable `on_conflict: "replace" | "keep"`).

## Storage backends

Configured in `config.json` under `vector_store` and `graph_store`:

| Backend | Kind | Notes |
|---|---|---|
| Qdrant (default) | vector | embedded/docker; also Milvus, Pinecone, Weaviate, Chroma, FAISS, pgvector |
| Neo4j / FalkorDB | graph | entity/fact graph memory via LLM extraction |

Embedding models: OpenAI (default), Ollama, HuggingFace, Gemini, Bedrock, etc.

## Scoping

Memory is namespaced by `user_id` / `agent_id` / `run_id` — pass the same scopes on ADD and SEARCH to isolate per-user or per-agent memory (the standard multi-tenant pattern).

## OpenMemory vs library

Two ways to run:

1. **Library** — `from mem0 import Memory`; call `memory.add / search / get / update / delete` in-process. Simple, no server.
2. **OpenMemory app** — self-hosted FastAPI server + web UI (`docker compose up` on :3000) exposing the same operations over REST with per-user keys.

Local checkout `programs/mem0` v2.0.12 is the library; the app is the `OpenMemory` companion repo (not checked out here).

# Citations

[1] [Mem0 docs — overview](https://docs.mem0.ai)
[2] [Mem0 GitHub](https://github.com/mem0ai/mem0)
[3] [OpenMemory](https://github.com/mem0ai/OpenMemory)
