---
type: Reference
title: Weaviate — Modules & Multimodal
description: Weaviate's module system and multi-vector objects for handling text, code, and image modalities.
resource: https://weaviate.io/developers/weaviate/modules
tags: [weaviate, modules, multimodal, multi-vector, code, image, embed]
generated: { by: "human:daniel", at: "2026-07-09T06:06:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T06:06:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: modules-docs
    resource: "https://weaviate.io/developers/weaviate/modules"
    title: "Modules docs"
    author: "site:weaviate.io"
  - id: multi-vector
    resource: "https://weaviate.io/developers/weaviate/concepts/vector-index"
    title: "Multi-vector"
    author: "site:weaviate.io"
  - id: colpali
    resource: "https://huggingface.co/blog/manu/colpali"
    title: "ColPali"
    author: "site:huggingface.co"
  - id: code-rag-ast
    resource: "https://www.lancedb.com/blog/building-rag-on-codebases-part-2"
    title: "Code RAG AST"
    author: "site:www.lancedb.com"
---

# Modules

Weaviate's capabilities come from **modules**:
* `text2vec-*` — text embedding (OpenAI, Cohere, HuggingFace, local).
* `multi2vec-*` — multi-modal (image+text) embedding.
* `reranker-*` — reranking.
* `generative-*` — RAG generation.

# Multi-vector objects

A single object can hold **multiple vectors** — perfect for mixed modalities:
* An **image** page: store the ColPali/ColQwen page-vector **and** a VLM caption-vector.
* **Code**: store source-vector **and** intent-vector.

```python
# conceptual: multi-vector object
collection.data.insert(
    properties={"doc_type":"image","program":"kbv2"},
    vector={ "page": page_vec, "caption": caption_vec }
)
```

# Modality handling

| Modality | Weaviate approach |
|----------|-------------------|
| Text | `text2vec-*` + BM25 (hybrid) |
| Code | AST-chunked source + code embedder; BM25 on identifiers |
| Image | `multi2vec-*` or store ColPali/VLM vectors as named vectors |
