---
type: Concept
title: Microsoft GraphRAG Overview
description: How Microsoft GraphRAG indexes text into an entity graph with hierarchical Leiden communities and summaries, and how local, global, DRIFT and basic search use it.
resource: https://microsoft.github.io/graphrag
tags: [graphrag, overview, leiden, community-summaries, global-search]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphrag-docs
    resource: "https://microsoft.github.io/graphrag"
    title: "GraphRAG documentation"
    author: "site:microsoft.github.io"
  - id: graphrag-paper
    resource: "https://arxiv.org/abs/2404.16130"
    title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
    author: "Edge et al., arXiv 2404.16130"
---

# Microsoft GraphRAG — Overview

## Indexing pipeline

1. **Chunk** input documents into text units.
2. **Extract** entities, relationships and claims from each chunk with an LLM.
3. **Build the graph** and merge duplicate entities.
4. **Detect communities** with hierarchical Leiden clustering, producing nested levels from broad to specific.
5. **Summarise** every community with an LLM ("community reports").
6. **Embed** text units and entity descriptions.

Outputs are Parquet tables (entities, relationships, communities, community reports, text units) in `output/`.

## Query modes

| Mode | Best for | How |
|---|---|---|
| **Global search** | Corpus-wide questions ("main themes?") | Map-reduce over community reports |
| **Local search** | Questions about specific entities | Starts from matching entities, gathers neighbours, relationships and source text |
| **DRIFT search** | Specific questions that need broader context | Local search enriched with community information, iteratively refined |
| **Basic search** | Baseline comparison | Plain vector RAG over text units |

The paper (arXiv 2404.16130) showed global search beating vector RAG on comprehensiveness and diversity for sensemaking questions over ~1M-token corpora.

## Trade-offs

* **Cost:** indexing calls an LLM for every chunk plus every community; large corpora get expensive. Start with a small dataset and a cheap model.
* **Static:** adding documents means re-running (parts of) the pipeline; there is no temporal model. For evolving data see [Graphiti](../graphiti/index.md); for cheaper incremental updates see [LightRAG](../lightrag/index.md).
* **Maintenance mode:** stable, but expect no new features.

## Related

[GraphRAG index](index.md) · [GraphRAG concept](../../concepts/graphrag.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md)
