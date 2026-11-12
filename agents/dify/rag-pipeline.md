---
type: Concept
title: Dify RAG Pipeline
description: Dify knowledge bases — ingestion and parsing, chunking modes including parent-child, embedding and indexing, hybrid search with reranking, knowledge pipelines, external knowledge APIs, and the agent knowledge base.
resource: https://docs.dify.ai
tags: [dify, rag, knowledge-base, chunking, retrieval]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: dify-docs
    resource: "https://docs.dify.ai"
    title: "Dify documentation"
    author: "site:docs.dify.ai"
---

# Dify — RAG Pipeline

1. **Ingest** files (PDF, Word, slides, spreadsheets, Markdown, HTML), web pages via crawlers such as [Firecrawl](../../browsers/firecrawl/index.md), or Notion.
2. **Parse and chunk** — general or parent-child chunking (small chunks for matching, larger parents for context); custom delimiters and overlap. Parsing plugins such as [Docling](../../ingestion/docling/index.md) can replace the default extractor.
3. **Embed and index** into the configured [vector database](../../concepts/vector-databases.md), or use economical keyword indexing.
4. **Retrieve** with vector, full-text or hybrid search, plus a reranker and score threshold.
5. **Use** in apps through Knowledge Retrieval nodes, with citations.

**Knowledge pipelines** make step 1–3 a customisable workflow; **external knowledge APIs** connect existing retrieval systems (e.g. [LightRAG](../../memory/lightrag/index.md)); the **Agent Knowledge Base** (1.18+) lets agents read knowledge directly. Dataset-scoped API keys allow per-knowledge-base access.

See [RAG](../../concepts/rag.md) for the underlying concepts and [Ragas](../../observability/ragas/index.md) for evaluation.

## Related

[Dify index](index.md) · [Workflows & agents](workflows-agents.md)
