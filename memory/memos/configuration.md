---
type: Reference
title: MemOS Configuration
description: Where MemOS configuration lives — docker/.env.example and .env.example-full for LLM provider, embedder, vector DB, graph DB and scheduler — and choices for local models.
resource: https://github.com/MemTensor/MemOS/blob/main/docker/.env.example-full
tags: [memos, configuration, env, ollama]
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
---

# MemOS — Configuration

Self-hosted MemOS reads a `.env` file. Start from `docker/.env.example`; every option is listed in `docker/.env.example-full`.

| Area | What you set |
|---|---|
| LLM provider | Hosted (OpenAI-compatible APIs) or local servers such as [Ollama](../../runtime/ollama/index.md) and [vLLM](../../runtime/vllm/index.md) |
| Embedder | Embedding model and dimensions — see [Embeddings](../../concepts/embeddings.md) |
| Vector DB | [Qdrant](../../databases/qdrant/index.md) by default |
| Graph DB | [Neo4j](../../databases/neo4j/index.md) by default |
| Scheduler | MemScheduler workers and async ingestion settings |

## Tips

* Pick the embedding model before ingesting; changing it later requires re-embedding.
* Keep the API on a private network or behind auth; the example binds `0.0.0.0:8000`.
* The local plugin needs none of this — it uses SQLite on the device.

## Related

[MemOS index](index.md) · [Installation](installation.md) · [Vector databases](../../concepts/vector-databases.md)
