---
type: Concept
title: GraphRAG
description: GraphRAG — retrieval-augmented generation that uses a knowledge graph built from data, for multi-hop reasoning and corpus-wide questions — covering Microsoft's community-summary approach, dual-level retrieval, temporal graphs, code graphs, and the trade-offs against vector RAG.
resource: https://arxiv.org/abs/2404.16130
tags: [concept, graphrag, knowledge-graph, rag, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphrag-paper
    resource: "https://arxiv.org/abs/2404.16130"
    title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
    author: "Edge et al., arXiv 2404.16130"
  - id: lightrag-paper
    resource: "https://arxiv.org/abs/2410.05779"
    title: "LightRAG: Simple and Fast Retrieval-Augmented Generation"
    author: "Guo et al., arXiv 2410.05779"
  - id: zep-paper
    resource: "https://arxiv.org/abs/2501.13956"
    title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
    author: "Rasmussen et al., arXiv 2501.13956"
---

# GraphRAG

**GraphRAG** extends [RAG](rag.md) with a [knowledge graph](knowledge-graphs.md): an LLM (or a parser) extracts entities and relationships from the data, and retrieval follows those relationships instead of — or as well as — matching text chunks by similarity.

## Why graphs help

* **Multi-hop questions** ("which suppliers of our top customer had outages?") need several connected facts that no single chunk contains.
* **Global questions** ("what are the main themes across 10,000 reports?") need summaries over the whole corpus.
* **Provenance and change**: edges can carry sources and validity times.

## Families of approaches

| Approach | Idea | Tool |
|---|---|---|
| Community summaries | Cluster the entity graph (Leiden) and pre-summarise each community; answer global questions by map-reduce | [Microsoft GraphRAG](../memory/graphrag/index.md) |
| Dual-level retrieval | Match low-level entities and high-level relationship themes, plus vectors; incremental updates | [LightRAG](../memory/lightrag/index.md) |
| Temporal context graphs | Bi-temporal facts with episodes as provenance; for evolving data and memory | [Graphiti](../memory/graphiti/index.md), [Zep](../memory/zep/index.md) |
| Pipeline memory | Graph + vectors built together, enriched over time | [Cognee](../memory/cognee/index.md) |
| Code graphs | Deterministic AST-derived graphs of a codebase | [Graphify](../memory/graphify/index.md) |
| Graph DB native | Vector index for entry points, Cypher for expansion; text-to-Cypher | [Neo4j](../databases/neo4j/ai-integration.md), [FalkorDB](../databases/falkordb/index.md) |

## Trade-offs

* **Cost:** LLM extraction over every chunk is expensive; deterministic parsers (Graphify) avoid it for code.
* **Quality:** extraction errors become wrong edges — prefer systems that record provenance or confidence ([Graphify confidence tags](../memory/graphify/confidence-tags.md)).
* **Maintenance:** static indexes go stale; incremental or temporal designs fix that.
* **Not always better:** for simple factual lookup, hybrid vector search is cheaper and as accurate. Measure with [evals](evals.md).

## A hand-built example

This vault is itself a small, human-curated knowledge graph: notes are nodes, links are typed by context, and [Obsidian](../tools/obsidian/index.md)'s graph view renders it.

## Related

[Knowledge graphs](knowledge-graphs.md) · [RAG](rag.md) · [Agent memory](agent-memory.md) · [Memory alternatives](../memory/alternatives.md) · [Concepts index](index.md)
