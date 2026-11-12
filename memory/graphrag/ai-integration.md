---
type: Playbook
title: Microsoft GraphRAG AI Integration
description: Where Microsoft GraphRAG fits in an AI stack today — corpus-level sensemaking, using its Parquet outputs as agent tools, and lighter or temporal alternatives.
resource: https://github.com/microsoft/graphrag
tags: [graphrag, integration, agents, rag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphrag-github
    resource: "https://github.com/microsoft/graphrag"
    title: "microsoft/graphrag on GitHub"
    author: "site:github.com"
  - id: graphrag-paper
    resource: "https://arxiv.org/abs/2404.16130"
    title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
    author: "Edge et al., arXiv 2404.16130"
---

# Microsoft GraphRAG — AI Integration

## When it is the right tool

* You have a fixed corpus (reports, transcripts, a book series) and need **global** answers across it.
* You can afford an expensive one-off index and the corpus changes rarely.

## Using it from agents

* Wrap `graphrag query` (or the Python query API) as a tool so an agent can call global search for broad questions and local search for entity questions — a simple form of [agentic RAG](../../concepts/rag.md).
* The Parquet outputs (entities, relationships, community reports) can be loaded into [Neo4j](../../databases/neo4j/index.md) for exploration, or into a [vector database](../../concepts/vector-databases.md) for your own retrieval.

## What people use instead in 2026

GraphRAG's ideas — entity extraction, communities, multi-level summaries — live on in other tools:

* [LightRAG](../lightrag/index.md): dual-level graph + vector retrieval with incremental updates and much cheaper indexing.
* [Graphiti](../graphiti/index.md) / [Zep](../zep/index.md): temporal graphs for changing data and agent memory.
* [Cognee](../cognee/index.md): pipeline-based memory that builds graphs and vectors together.
* Long-context models: for small corpora, putting everything in context can beat any index.

## Related

[GraphRAG index](index.md) · [GraphRAG concept](../../concepts/graphrag.md) · [Memory alternatives](../alternatives.md)
