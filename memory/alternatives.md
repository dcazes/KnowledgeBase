---
type: Reference
title: "Memory — Alternatives"
description: "Side-by-side comparison of the memory programs documented in this knowledge base — what each does, how they differ, and which alternatives each names."
resource: "https://docs.mem0.ai"
tags: [memory, alternatives, comparison]
generated: { by: "agent:fixer", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "agent:fixer", at: "2026-08-13T00:00:00Z" } ]
status: draft
stale_after: 2027-02-09
sources:
  - id: s1
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify — Alternatives"
    author: human:daniel
  - id: s2
    resource: "https://github.com/getzep/graphiti"
    title: "Graphiti — Alternatives"
    author: human:daniel
  - id: s3
    resource: "https://memos-docs.openmem.net/home/overview/"
    title: "MemOS — Alternatives"
    author: human:daniel
  - id: s4
    resource: "https://docs.mem0.ai"
    title: "Mem0 — Alternatives"
    author: human:daniel
  - id: s5
    resource: "https://lightrag.readthedocs.io/en/latest/"
    title: "LightRAG — Alternatives"
    author: human:daniel
  - id: s6
    resource: "https://docs.cognee.ai"
    title: "Cognee — Alternatives"
    author: human:daniel
  - id: s7
    resource: "https://docs.honcho.dev"
    title: "Honcho — Alternatives"
    author: human:daniel
  - id: s8
    resource: "https://supermemory.ai"
    title: "Supermemory — Alternatives"
    author: human:daniel
  - id: s9
    resource: "https://hindsight.vectorize.io"
    title: "Hindsight — Alternatives"
    author: human:daniel
  - id: s10
    resource: "https://github.com/offendingcommit/openconcho"
    title: "OpenConcho — Alternatives"
    author: human:daniel
---

# Memory — Alternatives

The programs documented under `memory/` are alternatives to one another: they all store or structure information for agents, but they approach it differently — some as graph stores, some as user-memory layers, some as full memory platforms, and some as UIs on top of those. This doc compares them side by side, based only on what each program's own alternatives doc states. Where a source is silent or thin, that is noted rather than filled in.

## Comparison matrix

| Program | Primary purpose | Key differentiators | Best for | Notable alternatives |
|---|---|---|---|---|
| **Graphify** | Confidence-tagged, queryable graph built from mixed inputs (code, docs, PDFs, papers, images, video, URLs) | Static compiled graph with confidence tags; no DB; Hermes client + MCP; can emit an Obsidian vault | Structured, honest codebase/document graphs; compiled reference graph queried via MCP | Obsidian (vanilla), Mem0, LangChain graph retrievers, code2flow/mermaid, repo visualizers |
| **Graphiti** | Temporal context graph for evolving agent memory | Time-aware facts with provenance and episodes; self-hosted (Neo4j etc.); MCP-native; incremental | Evolving agent memory, time queries, auditable fact history | GraphRAG (batch), Zep (managed), Graphify (static), Mem0 (lightweight) |
| **MemOS** | Memory as an OS, not just a store | Scheduling, versioning, multi-cube KB management, feedback/correction; broad taxonomy (textual/tree/preference/skill/KV-cache/LoRA parametric); local-first; multi-modal + tool traces + personas; MCP server | Full-featured self-hosted memory platform | Graphiti, Mem0, Zep, LangMem, raw vector store (Qdrant/Milvus) |
| **Mem0** | Per-user agent memory layer (vector + graph) | Simple API, multi-tenant user memory, OpenMemory UI, many backends | Quick per-user chat memory | MemOS, Graphiti, Zep, LangMem |
| **LightRAG** | Incremental knowledge graph + dual-level retrieval for document Q&A | Cheap to index, updates without rebuild, server or library mode, local LLMs | Local document-Q&A engine with frequent updates | Microsoft GraphRAG, LlamaIndex, RAGFlow, Graphify; Mem0/MemOS/Graphiti are complementary (agent memory, not corpus retrieval) |
| **Cognee** | Knowledge-graph memory pipeline (extract → cognify → load) with semantic layers | Full memory engineering pipeline, frontend, graph-aware search | All-in-one graph memory pipeline | LightRAG, GraphRAG, Graphiti, Mem0/MemOS, LlamaIndex |
| **Honcho** | User modeling: personas, state machine, insights/goals | Answers "who is the user"; stateful UX; the only program here that models the user | Personalized, stateful agent UX | Mem0, MemOS, Graphiti, Zep, LangMem |
| **Supermemory** | Personal AI memory (save → semantic Q&A) | Simple end-user memory, local-first desktop | Save-and-forget personal memory with AI Q&A | Rewind, Recall (Windows), Mem0/MemOS, Obsidian, Notion/Anytype |
| **Hindsight** | Learning-based agent memory (learning passes) | Agents learn and improve over time; SOTA LongMemEval | Agents that must improve over time | Graphiti, Mem0, MemOS, Zep, LangMem |
| **OpenConcho** | UI for Honcho memory (web/desktop) | Browse + chat memory, multi-instance, privacy-first | Seeing and chatting with Honcho-backed agent memory | Honcho SDK only, OpenMemory (Mem0 UI), custom dashboard, MemOS MCP |

## Graphify

Graphify is positioned as a confidence-tagged, queryable graph built from mixed inputs (code, docs, papers, media) with an agent/MCP surface. Its source compares it against four kinds of alternatives: **Obsidian (vanilla)** — manual `[[links]]`, no automatic extraction, no confidence semantics, no agent query API, but zero inference cost and a complement rather than a replacement (Graphify can emit an Obsidian vault); **Mem0** — purpose-built conversational/episodic memory with a simple API, but not a structured entity-relationship graph and without source-confidence tagging; **LangChain graph retrievers** — fully programmable graph + vector RAG, but you build and maintain extraction yourself; and **code2flow/mermaid/static visualizers** — instant, no-LLM diagrams, but static-only with no semantic cross-file reasoning or query layer. The source's decision guide says Graphify is what this machine uses for extracting structure from a mixed corpus.

See also: [Graphify index](./graphify/index.md)

## Graphiti

Graphiti is an open-source, temporal context graph for agent memory that you self-host (Neo4j etc.). Its source compares it against **GraphRAG (Microsoft)** — batch entity graph with community summaries, good for static corpora but not incremental, slower queries, no real temporality; **Zep** — a managed version of Graphiti's engine, turnkey and governed with sub-200ms claims at scale, but a vendor dependency and not self-hosted-free; **Graphify** — a static, confidence-tagged compiled graph, light with no DB, but not temporal (snapshot only); and **Mem0** — a lightweight memory layer, simple and fast, but less graph-native with weaker relational/temporal modeling. The decision guide also points to MemOS, Honcho, LightRAG, and Cognee as related systems.

See also: [Graphiti index](./graphiti/index.md)

## MemOS

MemOS is described as "memory as an OS" rather than just a store: scheduling, versioning, multi-cube KB management, feedback/correction, a broad memory taxonomy (textual, tree, preference, skill, KV-cache, LoRA parametric), local-first operation, and multi-modal + tool traces + personas in one space. Its source compares it against **Graphiti** (temporal context graph with episodes and provenance — graph-centric, less of a full OS), **Mem0** (layered memory, simple API, popular, hosted + OSS — less explicit scheduling/parametric memory), **Zep / Graphiti-like** (strong developer ergonomics, but a separate stack to operate), **LangMem** (LangChain memory abstraction, tied to that ecosystem), and a **raw vector store (Qdrant/Milvus)** (fast and simple, but black-box with no structured/inspectable memory or scheduling). The source notes you might pick something else for a quick semantic store, time-aware relational reasoning (Graphiti), per-user modeling (Honcho), lightweight RAG-style memory (Mem0 or Supermemory), or schema-native incremental graphs (LightRAG/Cognee).

See also: [MemOS index](./memos/index.md)

## Mem0

Mem0 is a vector + graph memory layer with per-user scoping, a simple API, multi-tenant user memory, an OpenMemory UI, and many backends. Its source compares it against **MemOS** (richest feature set, MCP server, benchmarked — the deployed-via-pip option on this machine), **Graphiti** (temporal context graph with fact provenance, episodes, change tracking — best when memory must be auditable over time), **Zep** (temporal knowledge graph, cloud-hosted alternative to Graphiti), and **LangMem** (LangGraph memory SDK — only if already on LangChain). The source notes Mem0 is a good default for per-user chat memory but is **not deployed locally** (checkout only), and that Mem0's graph store (Neo4j) covers light graph needs while Graphiti is the heavy graph engine.

See also: [Mem0 index](./mem0/index.md)

## LightRAG

LightRAG is an incremental knowledge graph with dual-level retrieval: cheap to index, updates without rebuild, server or library mode, and works with local LLMs. Its source compares it against **Microsoft GraphRAG** (batch global + local search, best for corpus-level global understanding, but heavier index cost and overkill for small corpora), **LlamaIndex** (pluggable indexes with a huge ecosystem, but more assembly required), **RAGFlow** (deep-document RAG with layouts, good for PDFs/structured docs, but a heavier stack with more services), and **Graphify** (a static folder→graph compiler — a different job: build once, query via MCP). Mem0/MemOS/Graphiti are called complementary rather than competitors because they handle agent memory across sessions, not corpus retrieval. The source notes LightRAG is not yet deployed here.

See also: [LightRAG index](./lightrag/index.md)

## Cognee

Cognee is described as a full knowledge-graph memory pipeline (extract → cognify → load) with semantic layers, a frontend, and graph-aware search. Its source compares it against **LightRAG** (lighter, cheaper to index, server mode — quick graph RAG without a full pipeline), **GraphRAG (Microsoft)** (batch global/local graph search with heavy index cost and batch rebuilds), **Graphiti** (temporal context graph for session/fact memory — a different job), **Mem0/MemOS** (per-user/agent memory with a quick API — user memory, not corpus knowledge engineering), and **LlamaIndex** (a general pluggable RAG framework with more assembly). The source notes Cognee is not deployed here.

See also: [Cognee index](./cognee/index.md)

## Honcho

Honcho is user modeling rather than a memory store: personas, a state machine, insights/goals — it answers "who is the user" and enables stateful UX. Its source says this is unique among the compared tools: none of the others model the user. It compares Honcho against **Mem0** (per-user facts with a simple API, but no user-model layer), **MemOS** (memory OS with scheduling and KV — a memory store without persona modeling), **Graphiti** (temporal context graph — fact history, not a user model), **Zep** (hosted graph memory, cloud alternative to Graphiti), and **LangMem** (LangGraph memory SDK, only on LangChain). The source suggests combos: Honcho for the user model, Graphiti for provenance, Mem0/MemOS for bulk storage.

See also: [Honcho index](./honcho/index.md)

## Supermemory

Supermemory is a personal AI memory app (save → semantic Q&A), simple end-user memory with a local-first desktop. Its source compares it against **Rewind** (screen-recording memory that captures everything visually — heavy, with a privacy trade-off), **Recall (Windows)** (timeline screenshots + local AI, OS-integrated but Windows-only), **Mem0/MemOS** (developer memory platforms with APIs/MCP — the agent-stack choice here), **Obsidian** (local-first PKM, full control, plugins — the main knowledge base here), and **Notion/Anytype** (notes + databases, collaborative/docs, cloud or different philosophy). The source notes Supermemory is installed (app data present 2026-07) but idle.

See also: [Supermemory index](./supermemory/index.md)

## Hindsight

Hindsight is learning-based agent memory: learning passes let agents improve over time, with SOTA LongMemEval claims. Its source compares it against **Graphiti** (temporal context graph — auditable fact history), **Mem0** (vector + graph user memory — quick user-fact memory), **MemOS** (memory OS with scheduling and MCP — full-featured memory platform), **Zep** (temporal knowledge graph — cloud option), and **LangMem** (LangGraph memory — only on LangChain). The source frames Hindsight's learning passes as the unique offering and suggests a combo of Hindsight (learning) + Graphiti (provenance). It notes Hindsight is not deployed here.

See also: [Hindsight index](./hindsight/index.md)

## OpenConcho

OpenConcho is a UI for Honcho memory (web/desktop): browse + chat memory, multi-instance, privacy-first. Its source compares it against **Honcho SDK only** (no UI, least moving parts — when agents only need programmatic memory), **OpenMemory** (the Mem0 UI — if you choose Mem0 rather than Honcho), a **custom dashboard** (exact fit but overkill, duplicates OpenConcho), and **MemOS MCP** (a full memory platform with its own UI/MCP — a different backend, no Honcho). The source notes OpenConcho is the companion UI when Honcho is the memory backend, and is not deployed here yet.

See also: [OpenConcho index](./openconcho/index.md)