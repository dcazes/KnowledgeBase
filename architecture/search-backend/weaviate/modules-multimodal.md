---
type: Reference
title: Weaviate — Modules & Multimodal
description: Weaviate's module system and multi-vector objects for handling text, code, and image modalities.
resource: https://weaviate.io/developers/weaviate/modules
tags: [weaviate, modules, multimodal, multi-vector, code, image, embed]
timestamp: 2026-07-09T06:06:00Z
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

# Citations

[1] [Modules docs](https://weaviate.io/developers/weaviate/modules)
[2] [Multi-vector](https://weaviate.io/developers/weaviate/concepts/vector-index)
[3] [ColPali](https://huggingface.co/blog/manu/colpali)
[4] [Code RAG AST](https://www.lancedb.com/blog/building-rag-on-codebases-part-2)
