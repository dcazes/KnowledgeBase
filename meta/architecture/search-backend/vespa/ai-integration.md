---
type: Reference
title: Vespa — AI Integration
description: How Vespa fits the KB pipeline — ingestion from parsers, serving agents (Hermes/OpenCode), and sitting under the graph layers.
resource: https://docs.vespa.ai/
tags: [vespa, integration, ingestion, agents, hermes, opencode, graphify, graphiti]
generated: { by: "human:daniel", at: "2026-07-09T06:03:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T06:03:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: vespa-docs
    resource: "https://docs.vespa.ai/"
    title: "Vespa docs"
    author: "site:docs.vespa.ai"
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

# Pipeline position

```
Parsers (Docling/Marker) ─┐
Code AST splitter ─────────┼─► embed ─► Vespa (search core)
Image (ColPali/VLM) ──────┘
                              │
                              ▼
        Graph layers: Graphiti (memory) / Graphify (map)  — auxiliary
                              │
                              ▼
                  Agents: Hermes (~/.hermes/) / OpenCode (.opencode.json)
```

# Ingestion

* Feed Vespa documents with: `content` (text/BM25), `vector` (embedding), `doc_type`, `program`, `tags`, `timestamp`.
* Embeddings can come from your `:4000` proxy (OpenAI-compatible) or local models.
* Code chunks carry source + AST metadata so BM25 + vector both work.

# Serving agents

* **Hermes** — a skill/tools calling Vespa's query API (HTTP) returns ranked chunks.
* **OpenCode** — MCP server or custom tool hitting Vespa.
* Graph layers query Vespa too, then layer relationships on top.

# Why under the graphs

Graphiti/Graphify answer "what relates to X"; Vespa answers "what's relevant to this query." For a massive KB, relevance comes from Vespa; relationships from the graphs.
