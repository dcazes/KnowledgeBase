---
type: Software
title: Mem0
description: Open-source memory layer for AI agents and assistants — extracts facts from conversations, stores them in a vector store, and retrieves them with hybrid (semantic + BM25 + entity) search. Library, self-hosted server, and managed platform.
resource: https://github.com/mem0ai/mem0
tags: [mem0, agent-memory, memory, vector-search, hybrid-search, python, typescript]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: mem0-github
    resource: "https://github.com/mem0ai/mem0"
    title: "mem0ai/mem0 on GitHub"
    author: "site:github.com"
  - id: mem0-docs
    resource: "https://docs.mem0.ai"
    title: "Mem0 documentation"
    author: "site:docs.mem0.ai"
  - id: mem0-pypi
    resource: "https://pypi.org/project/mem0ai/"
    title: "mem0ai on PyPI"
    author: "site:pypi.org"
---

# Mem0

**Mem0** ("mem-zero") is a memory layer that sits between an application and its LLM. It extracts durable facts from conversations, stores them with embeddings, and retrieves the relevant ones on later turns, so an assistant remembers users, sessions and agents across conversations. It is one of the most widely used projects in the [agent memory](../../concepts/agent-memory.md) space.

| | |
|---|---|
| Category | [Agent memory](../../concepts/agent-memory.md) |
| License | Apache-2.0 |
| Languages | Python (`mem0ai`), TypeScript (`mem0ai` on npm) |
| Latest release | Python v2.2.1 (2026-09-25); TypeScript SDK 3.3.1 |
| Deployment | In-process library · self-hosted server (Docker) · managed Mem0 Platform |

## Contents

* [Overview](overview.md) — the April 2026 memory algorithm: ADD-only extraction, hybrid retrieval, entity linking
* [Installation](installation.md) — library, self-hosted server, CLI
* [Configuration](configuration.md) — LLM, embedder, vector store and reranker providers
* [Snippets](snippets.md) — add/search/get_all/delete, local-only config, CLI
* [AI Integration](ai-integration.md) — chat loop pattern, MCP and agent skills, framework integrations

## Related

* Concepts: [Agent memory](../../concepts/agent-memory.md) · [Vector databases](../../concepts/vector-databases.md) · [Embeddings](../../concepts/embeddings.md) · [Context engineering](../../concepts/context-engineering.md)
* Peers: [Zep](../zep/index.md) / [Graphiti](../graphiti/index.md) (temporal graph memory), [Letta](../letta/index.md) (agent-managed memory), [Honcho](../honcho/index.md), [Supermemory](../supermemory/index.md), [Hindsight](../hindsight/index.md), [MemOS](../memos/index.md), [Cognee](../cognee/index.md)
* Default backends: [Qdrant](../../databases/qdrant/index.md), [pgvector](../../databases/pgvector/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
