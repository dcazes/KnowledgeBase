---
type: Concept
title: Open WebUI RAG
description: Open WebUI's retrieval pipeline — document extraction engines (default, Tika, Docling), chunking, embedding models, vector stores, hybrid search with rerankers, full-context mode, and web search as retrieval.
resource: https://docs.openwebui.com/features/rag
tags: [open-webui, rag, docling, embeddings, hybrid-search]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openwebui-docs
    resource: "https://docs.openwebui.com"
    title: "Open WebUI documentation"
    author: "site:docs.openwebui.com"
---

# Open WebUI — RAG

1. **Extract** text from uploads using the built-in extractor, Apache Tika, or [Docling](../../ingestion/docling/index.md) for complex PDFs ([Document parsing](../../concepts/document-parsing.md)).
2. **Chunk** by characters or tokens with configurable size and overlap.
3. **Embed** with a local SentenceTransformers model, Ollama, or an OpenAI-compatible embedding endpoint.
4. **Store** in the configured [vector database](../../concepts/vector-databases.md).
5. **Retrieve** with vector or **hybrid** (BM25 + vector) search and an optional reranker, then answer with citations.

Options include *full context mode* (send entire documents when they fit — often better with long-context models), per-knowledge-base settings, and a custom RAG prompt template. Web search results go through the same pipeline.

For graph-based retrieval, connect [LightRAG](../../memory/lightrag/ai-integration.md) as a model through its Ollama-compatible endpoint.

## Related

[Open WebUI index](index.md) · [RAG](../../concepts/rag.md)
