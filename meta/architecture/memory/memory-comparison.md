---
type: Reference
title: Agent Memory Systems — Comparison
description: "Head-to-head comparison of the agent-memory layer: Graphiti (temporal context graph), Mem0 (vector memory), MemOS (memory OS), Honcho (user modeling), LightRAG/Cognee (incremental graphs), Supermemory (RAG-style)."
resource: https://github.com/getzep/graphiti
tags: [graphiti, mem0, memos, honcho, comparison, memory, agent-memory, temporal, vector, memory-os]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: graphiti
    resource: "https://github.com/getzep/graphiti"
    title: "Graphiti"
    author: "site:github.com"
  - id: mem0
    resource: "https://mem0.ai/"
    title: "Mem0"
    author: "site:mem0.ai"
  - id: graphiti-vs-graphrag
    resource: "https://github.com/getzep/graphiti#graphiti-vs-graphrag"
    title: "Graphiti vs GraphRAG"
    author: "site:github.com"
  - id: memos
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemOS"
    author: "site:github.com"
  - id: memos-a-memory-os-for-ai-system-arxiv-2507-03724
    resource: "https://arxiv.org/abs/2507.03724"
    title: "MemOS: A Memory OS for AI System (arXiv:2507.03724)"
    author: "site:arxiv.org"
  - id: honcho
    resource: "https://docs.honcho.dev"
    title: "Honcho"
    author: "site:docs.honcho.dev"
---

# Agent Memory Systems — Comparison

This is the **hub comparison for agent-memory layers** in the KB. The three original systems are compared head-to-head; the newer P3 sets are mapped below.

## Head-to-head (original three)

| Dimension | **Graphiti** | **Mem0** | **MemOS** |
|-----------|--------------|----------|-----------|
| Core model | **Temporal context graph** (entities/edges + validity windows + episodes) | Vector + LLM memory (facts/messages) | **Memory OS** — MemCube (plaintext + activation + parameter memory, versioned) |
| Temporality | Explicit bi-temporal (when true / superseded) | Versioned memories, less explicit time model | Lifecycle: versioning, decay, feedback/correction |
| Provenance | **Episodes** — raw source preserved, full lineage | Stores memories; less raw-source linkage | Typed MemCubes with source/score/scope metadata |
| Backend | Neo4j / FalkorDB / Neptune / Kuzu | Vector store (self-host or API) | **Self-host:** Neo4j (graph) + Qdrant (vector) · **Local plugin:** SQLite + FTS5+vector |
| Graph-native | ✅ relationships are first-class | ❌ mostly flat vector memories | ✅ graph (Neo4j) when self-hosted; ❌ in local-plugin mode |
| Lifecycle mgmt | Graph evolution via episodes | Basic add/retrieve + categories | **Explicit:** feedback, correction, decay, tiering (L1/L2/L3) |
| Deploy weight | Heavy (graph DB) | Light (vector store) | Self-host: heavy (Neo4j+Qdrant) · Local plugin: light (SQLite, zero cloud) |
| Small-model proof | ❌ unverified | ❌ unverified | ❌ unverified (mitigate via model routing: big LLM extract, 4B embed/rerank) |
| License | Apache-2.0 | — | Apache-2.0 |

## Where the newer P3 sets fit

| System | Core model | Backend | KB docs |
|---|---|---|---|
| **Honcho** | **User modeling** — peers, sessions, messages, derived **conclusions** (who the user is) | Honcho server (FastAPI, Postgres + LLM) | [Honcho](../../../memory/honcho/index.md) |
| **LightRAG** | Incremental knowledge graph (graph + text chunks) with dual-level retrieval | Any graph/vector store | [LightRAG](../../../memory/lightrag/index.md) |
| **Cognee** | Schema-native knowledge graph (ontologies, ECL) | Neo4j + vector + graph ops | [Cognee](../../../memory/cognee/index.md) |
| **Supermemory** | RAG-style agent memory — semantic store over web/notes | Self-hosted memory server | [Supermemory](../../../memory/supermemory/index.md) |
| **Hindsight** | Learning memory (LongMemEval SOTA), Python workspace + Rust CLI + Next.js control plane | Hindsight API/control plane | [Hindsight](../../../memory/hindsight/index.md) |

## Decision guide

* **Pick Graphiti** if you need **temporal, relationship-rich, provenance-aware** memory and can run Neo4j. Best for agents operating on changing real-world state.
* **Pick Mem0** if you want **simple, fast agent memory** without standing up a graph database; good when flat vector memory + LLM extraction is enough.
* **Pick MemOS** if you want the **most batteries-included, unified** option — graph + vector + lifecycle (versioning, feedback, decay) in one system, with a 100% on-device Hermes local plugin available. Chosen for this machine for "simplicity + customizability." Upgrade to self-host (Neo4j+Qdrant) only if graph-native retrieval is explicitly needed.
* **Pick Honcho** for **user modeling** — you need to know *who* a peer is (preferences, derived conclusions) on top of raw facts.
* **Pick LightRAG/Cognee** when the job is **incremental graph building over documents**, not ephemeral user memory.
* **Pick Supermemory/Hindsight** for learning/reasoning-oriented memory at the lighter or research edge.

## How they relate to the KB

All of these can serve as the **memory layer** above the search backend (Vespa/Weaviate) and alongside the local Firecrawl+SearXNG search stack. Graphiti adds a graph dimension; Mem0 is the lighter flat option; MemOS unifies graph+vector with an explicit memory lifecycle; Honcho adds the user-modeling dimension none of the others provide. Graphify (static graph) is a separate, non-temporal concern.
