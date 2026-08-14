---
type: Reference
title: Weaviate
description: Open-source vector database with hybrid search (dense + BM25), multi-vector support, and pluggable modules for code/image embeddings — the lighter, schema-first candidate primary search backend.
resource: https://weaviate.io/
tags: [weaviate, vector-db, hybrid-search, search]
timestamp: 2026-08-12T00:00:00Z
---

# Weaviate

An open-source **vector database** with first-class **hybrid search** (dense + sparse/BM25), **multi-vector** support, and pluggable **modules** for code and image embeddings. For this KB it's the lighter, schema-first candidate **primary search backend** — easier to start than Vespa, still hybrid and multimodal.

## Contents

* [Overview](overview.md) - what Weaviate is
* [Hybrid Search](hybrid-search.md) - dense + sparse + reranker modules
* [Modules & Multimodal](modules-multimodal.md) - code/image modules, multi-vector
* [AI Integration](ai-integration.md) - ingestion, agents, graph layers

## Instance facts (this machine)

* **Not installed** — candidate architecture only; document from upstream.
* **Role here:** alternative primary search backend (vs Vespa) for the multi-modal KB.
* **Constraint:** self-hostable (matches local-first stack).

# Citations

[1] [Weaviate](https://weaviate.io/)
[2] [Weaviate docs](https://weaviate.io/developers/weaviate)
[3] [Search backend comparison](/../../search-backend/vespa-vs-weaviate.md)
