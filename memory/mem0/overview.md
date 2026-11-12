---
type: Concept
title: Mem0 Overview
description: How Mem0 works in 2026 — single-pass ADD-only fact extraction, multi-signal hybrid retrieval (semantic + BM25 + entity), memory scoping by user/agent/run, and how the library, server and platform differ.
resource: https://docs.mem0.ai
tags: [mem0, agent-memory, hybrid-search, entity-linking, architecture]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: mem0-readme
    resource: "https://github.com/mem0ai/mem0"
    title: "Mem0 README — New Memory Algorithm (April 2026)"
    author: "site:github.com"
  - id: mem0-migration-v3
    resource: "https://docs.mem0.ai/migration/oss-v2-to-v3"
    title: "Open Source: Migrating to the New Memory Algorithm"
    author: "site:docs.mem0.ai"
  - id: mem0-benchmarks
    resource: "https://github.com/mem0ai/memory-benchmarks"
    title: "mem0ai/memory-benchmarks"
    author: "site:github.com"
---

# Mem0 — Overview

Mem0 turns conversations into a store of short, self-contained **memories** ("prefers dark mode", "is migrating the API to Postgres") and returns the relevant ones when the agent needs context. It is a practical take on [agent memory](../../concepts/agent-memory.md): rather than stuffing whole transcripts into the prompt, it keeps a compact, searchable fact store — a form of [context engineering](../../concepts/context-engineering.md).

## The memory algorithm (April 2026 redesign)

Mem0 replaced its earlier extract-then-reconcile pipeline (where an LLM decided to ADD, UPDATE or DELETE each fact) with a simpler, faster design:

* **Single-pass, ADD-only extraction.** One LLM call per `add()` extracts facts. Memories accumulate; nothing is overwritten, so history is never lost to a bad merge. `add()` now only returns `ADD` events.
* **Agent facts are first-class.** When an agent confirms an action, that is stored with the same weight as what the user said.
* **Entity linking.** Entities are extracted, embedded and linked across memories.
* **Multi-signal retrieval.** Semantic similarity, BM25 keyword match and entity match are scored in parallel and fused — a [hybrid search](../../concepts/rag.md) approach.
* **Temporal reasoning.** Retrieval is time-aware, so "where does Alice live now?" prefers the latest dated fact.

Mem0 reports LoCoMo 92.5 and LongMemEval 94.4 for its managed platform with this algorithm (versus 71.4 / 67.8 before). The evaluation harness is open source, but note the published numbers are for the platform, which includes optimisations not in the open-source library.

## Graph memory moved to the platform

Older open-source releases could write an entity graph to [Neo4j](../../databases/neo4j/index.md) or [FalkorDB](../../databases/falkordb/index.md) (`enable_graph` + `graph_store`). That integration was **removed from open source** in the redesign; graph memory is now a built-in feature of the managed Mem0 Platform. For self-hosted graph memory, look at [Graphiti](../graphiti/index.md), [Cognee](../cognee/index.md) or [LightRAG](../lightrag/index.md).

## Scoping

Every memory belongs to one or more entities: `user_id`, `agent_id`, `run_id` (session). Since the redesign:

* `add()` and `delete_all()` take entity ids as top-level arguments.
* `search()` and `get_all()` take them inside `filters={...}` — passing them top-level raises `ValueError`.

## Three ways to run it

| Mode | What you get | Typical use |
|---|---|---|
| Library (`pip install mem0ai` / `npm install mem0ai`) | `Memory` object in your process; default local [Qdrant](../../databases/qdrant/index.md) on Python, in-memory store on Node | Prototypes, single-service apps |
| Self-hosted server (`server/` in the repo) | REST API + dashboard, API keys and auth on by default | Teams on their own infrastructure |
| Mem0 Platform (managed) | Graph memory, user profiles, advanced retrieval | Zero-ops production |

## Strengths and trade-offs

* **Strengths:** small API, many provider integrations, strong benchmark results, works with any [OpenAI-compatible](../../concepts/openai-compatible-api.md) or local model.
* **Trade-offs:** extraction quality depends on the LLM you configure; ADD-only means stale facts linger (retrieval ranks them down rather than deleting them); graph features are platform-only.

## Related

[Mem0 index](index.md) · [Configuration](configuration.md) · [Agent memory](../../concepts/agent-memory.md) · [Memory alternatives](../alternatives.md)
