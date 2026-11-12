---
type: Concept
title: Retrieval-Augmented Generation (RAG)
description: What RAG is and how it works — ingestion, chunking, embedding, retrieval (vector, keyword, hybrid), reranking and generation with citations — plus advanced variants (agentic RAG, GraphRAG, long-context trade-offs) and the tools in this vault that implement each stage.
resource: https://arxiv.org/abs/2005.11401
tags: [concept, rag, retrieval, hybrid-search, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: rag-paper
    resource: "https://arxiv.org/abs/2005.11401"
    title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    author: "Lewis et al., arXiv 2005.11401"
---

# Retrieval-Augmented Generation (RAG)

**RAG** gives a model knowledge it was not trained on by retrieving relevant text at question time and putting it in the prompt. It is the most common pattern in applied AI, and almost every tool in this vault touches one of its stages.

## The pipeline

| Stage | What happens | Tools here |
|---|---|---|
| Ingest | Get content from files and the web | [Docling](../ingestion/docling/index.md), [MarkItDown](../ingestion/markitdown/index.md), [Firecrawl](../browsers/firecrawl/index.md), [Crawl4AI](../browsers/crawl4ai/index.md) — see [Document parsing](document-parsing.md) |
| Chunk | Split into passages that keep context (headings, parent sections) | Docling chunkers, [LightRAG](../memory/lightrag/index.md), [Dify](../agents/dify/rag-pipeline.md) |
| Embed | Turn chunks into vectors | [Embeddings](embeddings.md) via [Ollama](../runtime/ollama/index.md), [vLLM](../runtime/vllm/index.md) |
| Store | Index vectors with metadata | [Vector databases](vector-databases.md): [Qdrant](../databases/qdrant/index.md), [pgvector](../databases/pgvector/index.md) |
| Retrieve | Vector, keyword (BM25) or **hybrid** search, filters | Qdrant hybrid queries, pgvector + full-text |
| Rerank | Cross-encoder or LLM reorders candidates | LightRAG mix mode, Open WebUI, Mem0 |
| Generate | Answer with citations | Any model |
| Evaluate | Faithfulness, context precision/recall | [Ragas](../observability/ragas/index.md), [promptfoo](../observability/promptfoo/index.md) — see [Evals](evals.md) |

## Variants

* **Hybrid search** (semantic + keyword) is now the default in serious systems; pure vector search misses exact terms and IDs.
* **Agentic RAG** — the model decides when and what to search, iterating with [tool calls](tool-calling.md).
* **[GraphRAG](graphrag.md)** — retrieve through a [knowledge graph](knowledge-graphs.md) for multi-hop and corpus-wide questions.
* **Memory as RAG** — [agent memory](agent-memory.md) systems retrieve facts about users instead of documents.
* **Long context** — when the corpus fits in the window, skipping retrieval can beat it; RAG still wins on cost, freshness and citations.

## Ready-made RAG apps

[Open WebUI](../apps/openwebui/rag.md), [AnythingLLM](../apps/anythingllm/index.md), [SurfSense](../browsers/surfsense/index.md), [Dify](../agents/dify/index.md), [Supermemory](../memory/supermemory/index.md).

## Related

[Embeddings](embeddings.md) · [Vector databases](vector-databases.md) · [GraphRAG](graphrag.md) · [Context engineering](context-engineering.md) · [Concepts index](index.md)
