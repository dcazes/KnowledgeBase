---
type: Reference
title: Weaviate — AI Integration
description: Weaviate's place in the KB pipeline — ingestion from parsers, serving agents, and complementing the graph layers.
resource: https://weaviate.io/developers/weaviate
tags: [weaviate, integration, ingestion, agents, hermes, opencode, graphify, graphiti]
timestamp: 2026-07-09T06:07:00Z
---

# Pipeline position

```
Parsers (Docling/Marker) ─┐
Code AST splitter ─────────┼─► embed (modules) ─► Weaviate (hybrid core)
Image (ColPali/VLM) ──────┘
                              │
                              ▼
        Graph layers: Graphiti (memory) / Graphify (map)  — auxiliary
                              │
                              ▼
                  Agents: Hermes (~/.hermes/) / OpenCode (.opencode.json)
```

# Ingestion

* Objects carry `doc_type`, `program`, `tags`, `timestamp` (for filtering) + named vectors.
* Embeddings via modules — can point at your `:4000` proxy (OpenAI-compatible) or local models.
* Code chunks: source + AST metadata so hybrid (BM25 + vector) works.

# Serving agents

* **Hermes** — skill/tool calling Weaviate's REST/GraphQL query API.
* **OpenCode** — MCP server or custom tool.
* Graph layers query Weaviate, then add relationships.

# Why under the graphs

Graphiti/Graphify = relationships; Weaviate = relevance/retrieval. For a massive KB, retrieval is Weaviate's job; graphs are auxiliary.

# Citations

[1] [Weaviate docs](https://weaviate.io/developers/weaviate)
[2] [Hybrid search](hybrid-search.md)
[3] [Hermes](/../../../hermes/index.md)
[4] [OpenCode](/../../../opencode/index.md)
[5] [Graphiti](/../../../graphiti/index.md)
