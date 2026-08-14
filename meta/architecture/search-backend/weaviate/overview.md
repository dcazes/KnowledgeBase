---
type: Software
title: Weaviate — Overview
description: Open-source vector database with hybrid search, multi-vector support, and pluggable code/image modules; schema-first and self-hostable.
resource: https://weaviate.io/
tags: [weaviate, vector-db, hybrid, modules, multimodal, self-hosted]
generated: { by: "human:daniel", at: "2026-07-09T06:04:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T06:04:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: weaviate
    resource: "https://weaviate.io/"
    title: "Weaviate"
    author: "site:weaviate.io"
  - id: weaviate-vs-vespa
    resource: "https://zilliz.com/comparison/vespa-vs-weaviate"
    title: "Weaviate vs Vespa"
    author: "site:zilliz.com"
  - id: architecture-overview
    resource: "/../../index.md"
    title: "Architecture overview"
---

# What Weaviate is

Weaviate is an open-source **vector database** built for AI applications. Its standout features: **hybrid search** (combine dense vector + keyword/sparse), **multi-vector** objects (store several vectors per item — e.g. a page image + its caption), and a **module system** that adds embedding/reranking/image/code capabilities. It's schema-first and designed to self-host.

# Why it fits a massive KB

* **Hybrid out of the box** — no separate keyword index to maintain.
* **Multi-vector** — ideal for images (page-vector + text-vector) and code (source + intent).
* **Modules** — `text2vec-*`, `multi2vec-*`, `reranker-*`, `generative-*` plug in embedders/rerankers.
* **Self-hosted** — Docker/K8s; matches your local-first stack.
* **Scales** — distributed mode for large corpora.

# Position in the architecture

```
Ingest → embed (via modules) → Weaviate (hybrid + multi-vector)
                                    │
                                    ▼
                       graph layers (Graphiti / Graphify) — auxiliary
                                    │
                                    ▼
                              Agents (Hermes / OpenCode)
```

Weaviate is the **retrieval core**; graphs layer on relationships/memory.

# Versus Vespa

Weaviate is **easier to start** (schema-first, modules) but does less *unified* ranking/inference in one engine than Vespa. For most KB sizes it's plenty; pick Vespa if you need unified billion-scale ranking without extra systems.
