---
type: Software
title: MemOS — Overview
description: Memory Operating System for LLM agents — unified store/retrieve/manage for long-term memory (textual, tree, preference, skill, KV-cache, LoRA) with scheduling, versioning, vector + graph storage.
resource: https://memos-docs.openmem.net/home/overview/
tags: [memos, memory, memory-os, agents, rag, mcp, llm]
timestamp: 2026-07-16T00:00:00Z
---

# What MemOS is

**MemOS** (MemoryOS) is a **Memory Operating System** for LLMs and AI agents. It unifies **store / retrieve / manage** for long-term memory so agents get context-aware, personalized, evolving memory — covering KB, multi-modal, tool, and persona memory. Unlike a black-box embedding store, memory is structured as an inspectable, editable graph.

Key features (from upstream README):
* **Unified Memory API** — one API to add / retrieve / edit / delete memory.
* **Multi-Modal Memory** — text, images, tool traces, personas retrieved together.
* **Multi-Cube KB management** — multiple knowledge bases as composable *memory cubes* (isolation, sharing, dynamic composition).
* **Async ingestion via MemScheduler** — millisecond-latency memory ops under concurrency.
* **Memory feedback & correction** — refine memory with natural-language feedback over time.

# Memory types

| Type | What it stores |
|------|----------------|
| Textual | `naive_text` / `general_text` / `tree_text` / `simple_tree_text` |
| Preference | `pref_text` / `simple_pref_text` |
| Activation (parametric) | `kv_cache` / `vllm_kv_cache` / `lora` |
| Skill | reusable agent behaviors (skill-mem extra) |

# How it works

MemOS is a Python package (`import memos`) with a top-level `MOS` entry that orchestrates **memory cubes** (`GeneralMemCube`) aggregating multiple memory types, a **scheduler** (`GeneralScheduler`) for async ops, user/tenant management, and provider plug-ins (LLM, embedder, vector DB, graph DB, chunker, parser, reranker) wired through factory registries.

* **LLM / embedder:** OpenAI, Azure, Ollama, vLLM, Qwen, DeepSeek, HuggingFace; embedders Ollama / sentence-transformers / universal_api.
* **Vector DB:** Qdrant, Milvus. **Graph DB:** Neo4j, Postgres, Nebula, Neo4j-community.
* **API:** FastAPI (`memos.api.server_api:app`) on `:8000`, routers `admin_/product_/server_`, plus an **MCP server**.

# How it fits your stack

* Sits as the **general memory layer** alongside **Graphiti** (temporal context graph) — MemOS covers structured/textual/preference/skill memory; Graphiti covers time-aware episodes.
* Exposed as an **MCP server** so Hermes / OpenCode / Cursor / Windsurf can use it as agent memory.
* Official **Hermes Agent local plugin** and **OpenClaw plugin** exist (hybrid FTS5 + vector retrieval, local-first SQLite, skill evolution).

# Citations

[1] [MemOS repo](https://github.com/MemTensor/MemOS)
[2] [MemOS docs](https://memos-docs.openmem.net/home/overview/)
[3] [PyPI — MemoryOS](https://pypi.org/project/MemoryOS/)
