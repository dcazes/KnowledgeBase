---
type: Reference
title: Weaviate — AI Integration
description: Weaviate's place in the KB pipeline — ingestion from parsers, serving agents, and complementing the graph layers.
resource: https://weaviate.io/developers/weaviate
tags: [weaviate, integration, ingestion, agents, hermes, opencode, graphify, graphiti]
generated: { by: "human:daniel", at: "2026-07-09T06:07:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T06:07:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: weaviate-docs
    resource: "https://weaviate.io/developers/weaviate"
    title: "Weaviate docs"
    author: "site:weaviate.io"
  - id: hybrid-search
    resource: "hybrid-search.md"
    title: "Hybrid search"
  - id: hermes
    resource: "/../../../hermes/index.md"
    title: "Hermes"
  - id: opencode
    resource: "/../../../opencode/index.md"
    title: "OpenCode"
  - id: graphiti
    resource: "/../../../graphiti/index.md"
    title: "Graphiti"
---

# Weaviate — Pipeline position

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
