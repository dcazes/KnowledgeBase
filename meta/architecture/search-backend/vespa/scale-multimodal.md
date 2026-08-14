---
type: Reference
title: Vespa — Scale & Multimodal
description: Vespa at billion-scale and how text, code, and image modalities are represented as vectors/fields for unified retrieval.
resource: https://vespa.ai/vector-database/
tags: [vespa, scale, billion, multimodal, text, code, image, embedding]
generated: { by: "human:daniel", at: "2026-07-09T06:02:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T06:02:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: vespa-scale
    resource: "https://vespa.ai/vector-database/"
    title: "Vespa scale"
    author: "site:vespa.ai"
  - id: code-rag-ast-chunking
    resource: "https://www.lancedb.com/blog/building-rag-on-codebases-part-2"
    title: "Code RAG — AST chunking"
    author: "site:www.lancedb.com"
  - id: colpali-late-interaction
    resource: "https://huggingface.co/blog/manu/colpali"
    title: "ColPali late interaction"
    author: "site:huggingface.co"
  - id: architecture-overview
    resource: "/../../index.md"
    title: "Architecture overview"
---

# Scale

Vespa is built for **billion-scale** corpora: distributed indexing, sharding, and low-latency ranking. This addresses the "when the KB gets massive" requirement directly — you don't outgrow it by adding chunks.

# Multimodal representation

Vespa stores each modality as **fields**; you choose the embedding per field:

| Modality | Representation | Embedder |
|----------|---------------|----------|
| **Text / Markdown** | dense vector + text (BM25) | general embedding model |
| **Code** | dense vector (AST-chunked) + text (BM25 on source) | code embedding model (e.g. Voyage-code) |
| **Images** | dense vector of the page/image | ColPali/ColQwen (late-interaction) or VLM caption → text embed |

Key point: **code must be chunked structurally** (function/class units via AST), not as prose — verified best practice for code RAG. The embedder output is just a vector field in Vespa; Vespa doesn't care which modality produced it.

# Unified query across modalities

Because all signals are fields in one schema, a single query can rank text, code, and image hits together (weighted by your ranking function).
