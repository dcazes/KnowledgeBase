---
type: Software
title: LightRAG
description: Graph-enhanced RAG engine from HKU — LLM-extracted entity graph plus vector retrieval with dual-level (local/global) and mix query modes, incremental updates, a WebUI/API server, and multimodal parsing via MinerU or Docling.
resource: https://github.com/HKUDS/LightRAG
tags: [lightrag, graphrag, rag, knowledge-graph, python, webui]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: lightrag-github
    resource: "https://github.com/HKUDS/LightRAG"
    title: "HKUDS/LightRAG on GitHub"
    author: "site:github.com"
  - id: lightrag-paper
    resource: "https://arxiv.org/abs/2410.05779"
    title: "LightRAG: Simple and Fast Retrieval-Augmented Generation"
    author: "Guo et al., arXiv 2410.05779 (EMNLP 2025)"
---

# LightRAG

**LightRAG** is a lighter alternative to [Microsoft GraphRAG](../graphrag/index.md): it extracts entities and relationships into a graph, indexes them alongside text chunks in a vector store, and retrieves at two levels — specific entities (local) and broader relationship themes (global). New documents are merged incrementally rather than rebuilding the index.

| | |
|---|---|
| Category | [GraphRAG](../../concepts/graphrag.md) · [RAG](../../concepts/rag.md) |
| License | MIT |
| Language | Python 3.11+ (`lightrag-hku`); WebUI in TypeScript |
| Latest release | v1.5.7 (2026-09-02) |
| Server | `lightrag-server` — WebUI at `:9621/webui`, REST docs at `:9621/docs`, Ollama-compatible chat endpoint |
| Paper | EMNLP 2025 (arXiv 2410.05779) |

## Contents

* [Overview](overview.md) — indexing, dual-level retrieval, query modes, 2026 features
* [Installation](installation.md) — uv tool, source, Docker Compose, setup wizard
* [Configuration](configuration.md) — `.env`, role-specific LLMs, storage backends, chunking
* [Snippets](snippets.md) — Python API, server API, query modes
* [AI Integration](ai-integration.md) — using LightRAG from chat UIs and agents

## Related

* Concepts: [GraphRAG](../../concepts/graphrag.md) · [RAG](../../concepts/rag.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md) · [Document parsing](../../concepts/document-parsing.md)
* Peers: [Microsoft GraphRAG](../graphrag/index.md), [Graphiti](../graphiti/index.md), [Cognee](../cognee/index.md); parsers [Docling](../../ingestion/docling/index.md); evals [Ragas](../../observability/ragas/index.md), tracing [Langfuse](../../observability/langfuse/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
