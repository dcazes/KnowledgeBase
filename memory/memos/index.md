---
type: Software
title: MemOS
description: Memory operating system for LLMs and agents from MemTensor — a unified add/retrieve/edit/delete API over graph-structured, multi-modal memory organised in composable memory cubes, with an async scheduler, feedback-based correction, and plugins for OpenClaw, Hermes and DeepSeek Harness.
resource: https://github.com/MemTensor/MemOS
tags: [memos, memtensor, agent-memory, memory-cubes, knowledge-graph, python]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: memos-github
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemTensor/MemOS on GitHub"
    author: "site:github.com"
  - id: memos-docs
    resource: "https://memos-docs.openmem.net"
    title: "MemOS documentation"
    author: "site:memos-docs.openmem.net"
  - id: memos-paper
    resource: "https://arxiv.org/abs/2507.03724"
    title: "MemOS: A Memory OS for AI System"
    author: "Li et al., arXiv 2507.03724"
---

# MemOS

**MemOS** treats memory as a system resource that an "operating system" schedules and manages, rather than a passive vector store. Memories are graph-structured and inspectable, grouped into **memory cubes** that can be isolated per user or project and composed or shared between agents. Version 2.0 is code-named *Stardust*.

| | |
|---|---|
| Category | [Agent memory](../../concepts/agent-memory.md) |
| License | Apache-2.0 |
| Language | Python server (PyPI `MemoryOS`); TypeScript plugins |
| Latest release | v2.0.36 (2026-11-09) |
| Deployment | MemOS Cloud API · self-hosted (Docker: API + [Neo4j](../../databases/neo4j/index.md) + [Qdrant](../../databases/qdrant/index.md)) · cloud plugin · local plugin (SQLite) |

## Contents

* [Overview](overview.md) — memory cubes, MemScheduler, memory types, feedback
* [Installation](installation.md) — cloud, Docker, uvicorn, plugins
* [Configuration](configuration.md) — `.env` options for LLM, embedder, graph and vector stores
* [Snippets](snippets.md) — REST calls for cloud and self-hosted
* [Benchmarks](benchmarks.md) — OmniMemEval results and how to read them
* [AI Integration](ai-integration.md) — OpenClaw, Hermes, DeepSeek Harness plugins

## Related

* Concepts: [Agent memory](../../concepts/agent-memory.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md) · [Agent skills](../../concepts/agent-skills.md) · [Evals](../../concepts/evals.md)
* Peers: [Mem0](../mem0/index.md), [Hindsight](../hindsight/index.md), [Letta](../letta/index.md), [Honcho](../honcho/index.md), [Supermemory](../supermemory/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
