---
type: Concept
title: LightRAG Overview
description: How LightRAG indexes documents into a graph plus vectors, how dual-level retrieval and the local, global, hybrid, naive and mix query modes work, and what changed in 2025–2026.
resource: https://github.com/HKUDS/LightRAG
tags: [lightrag, overview, graphrag, query-modes, reranker]
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

# LightRAG — Overview

## Indexing

1. Split documents into chunks (strategies: `Fix`, `Recursive`, `Vector`, `Paragraph`).
2. An LLM extracts entities and relationships from each chunk, with descriptions and keywords.
3. Duplicates are merged into a graph; entities, relationships and chunks are all embedded.
4. New documents go through the same steps and are **merged** into the existing graph — no full rebuild. Deleting a document regenerates the affected parts of the graph.

## Query modes

| Mode | Retrieves |
|---|---|
| `local` | Entities matching the query's low-level keywords, plus their neighbourhood |
| `global` | Relationships matching high-level (thematic) keywords |
| `hybrid` | `local` + `global` |
| `naive` | Plain vector search over chunks (baseline [RAG](../../concepts/rag.md)) |
| `mix` | Graph + vector retrieval, reranked — the default when a reranker is configured |
| `bypass` | Send the query straight to the LLM |

## Notable 2025–2026 additions

* **Reranker support** (mix mode as default) and returned contexts for evaluation.
* **[Ragas](../../observability/ragas/index.md) evaluation** and **[Langfuse](../../observability/langfuse/index.md) tracing** integrations.
* **Role-specific LLMs** — separate models for EXTRACT, QUERY, KEYWORDS and VLM.
* **RAG-Anything merged in** — multimodal parsing (images, tables, equations) via MinerU or [Docling](../../ingestion/docling/index.md) services.
* **OpenSearch** as a unified backend for all four storage types; setup wizard; smart heading detection for Word documents.
* Better extraction with open models such as Qwen3-30B-A3B.

## Trade-offs

* Much cheaper to index than Microsoft GraphRAG (no community summarisation pass), but extraction still costs one LLM call per chunk.
* The embedding model must be fixed before the first upload; changing it means re-indexing everything.
* The server binds `0.0.0.0` with authentication **off** by default — secure it before exposing it.

## Related

[LightRAG index](index.md) · [GraphRAG concept](../../concepts/graphrag.md) · [Microsoft GraphRAG](../graphrag/overview.md)
