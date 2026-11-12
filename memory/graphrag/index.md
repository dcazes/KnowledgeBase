---
type: Software
title: Microsoft GraphRAG
description: Microsoft Research's graph-based RAG pipeline — LLM-extracted entity graph, Leiden community detection and community summaries, queried with local, global, DRIFT and basic search. Now in maintenance mode.
resource: https://github.com/microsoft/graphrag
tags: [graphrag, microsoft, knowledge-graph, rag, community-detection, python]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphrag-github
    resource: "https://github.com/microsoft/graphrag"
    title: "microsoft/graphrag on GitHub"
    author: "site:github.com"
  - id: graphrag-docs
    resource: "https://microsoft.github.io/graphrag"
    title: "GraphRAG documentation"
    author: "site:microsoft.github.io"
  - id: graphrag-paper
    resource: "https://arxiv.org/abs/2404.16130"
    title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
    author: "Edge et al., arXiv 2404.16130"
  - id: graphrag-blog
    resource: "https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/"
    title: "GraphRAG: Unlocking LLM discovery on narrative private data"
    author: "Microsoft Research"
---

# Microsoft GraphRAG

**GraphRAG** is the research project that popularised the term: index a document corpus by having an LLM extract entities and relationships, cluster the resulting graph into communities, write a summary per community, and use those structures to answer questions that plain vector [RAG](../../concepts/rag.md) cannot — especially "what are the main themes across all these documents?"

| | |
|---|---|
| Category | [GraphRAG](../../concepts/graphrag.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md) |
| License | MIT |
| Language | Python 3.10–3.12 (`graphrag`) |
| Latest release | v3.3.0 (2026-10-08) |
| Status | **Maintenance mode** — bug fixes, dependency and CVE updates only; no new features |

## Contents

* [Overview](overview.md) — the indexing pipeline and the four query modes
* [Installation](installation.md) — `graphrag init`, settings, cost warning
* [Snippets](snippets.md) — index, query, prompt tuning, local models
* [AI Integration](ai-integration.md) — when to use it and what replaced it in practice

## Related

* Concepts: [GraphRAG](../../concepts/graphrag.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md) · [RAG](../../concepts/rag.md)
* Peers: [LightRAG](../lightrag/index.md) (lighter, incremental), [Graphiti](../graphiti/index.md) (temporal), [Cognee](../cognee/index.md), [Graphify](../graphify/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
