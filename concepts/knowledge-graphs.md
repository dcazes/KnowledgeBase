---
type: Concept
title: Knowledge Graphs
description: Knowledge graphs for AI — entities and relationships, property graphs versus RDF, ontologies, construction by LLM extraction or parsing, temporal and provenance-aware graphs, graph databases, and how they power GraphRAG, agent memory and human knowledge bases.
resource: https://neo4j.com/docs/
tags: [concept, knowledge-graph, ontology, graph-database, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: neo4j-docs
    resource: "https://neo4j.com/docs/"
    title: "Neo4j documentation"
    author: "site:neo4j.com"
  - id: opencypher
    resource: "https://opencypher.org"
    title: "openCypher"
    author: "site:opencypher.org"
---

# Knowledge Graphs

A **knowledge graph** represents knowledge as **entities** (nodes) connected by **relationships** (edges), each with properties. It makes structure explicit — who works where, what depends on what, which fact came from which source — so both people and programs can traverse it.

## Models

| Model | Notes |
|---|---|
| Property graph | Labelled nodes and typed edges with properties; queried with Cypher/GQL — [Neo4j](../databases/neo4j/index.md), [FalkorDB](../databases/falkordb/index.md) |
| RDF / triples | Subject–predicate–object, SPARQL, formal ontologies (OWL) — common in enterprise and science |

## Building one

* **LLM extraction** from text: [Graphiti](../memory/graphiti/index.md), [LightRAG](../memory/lightrag/index.md), [Cognee](../memory/cognee/index.md), [Microsoft GraphRAG](../memory/graphrag/index.md), [Mem0](../memory/mem0/index.md) entity linking.
* **Deterministic parsing** of structured sources: [Graphify](../memory/graphify/index.md) (code via tree-sitter).
* **By hand**: linked notes in [Obsidian](../tools/obsidian/index.md) — like this vault.

An **ontology** (allowed entity and edge types) improves consistency; Graphiti and Zep define it with [Pydantic](../tools/pydantic/index.md) models, Cognee with ontology files.

## Properties that matter for AI

* **Provenance** — link each fact to its source ([Graphiti](../memory/graphiti/concepts.md) episodes, [Graphify](../memory/graphify/confidence-tags.md) tags).
* **Time** — validity windows so the graph knows what is true *now* ([Zep](../memory/zep/index.md)).
* **Communities** — clusters summarised for high-level questions.
* **Hybrid indexes** — vectors on nodes for semantic entry points.

## Uses

[GraphRAG](graphrag.md) retrieval, long-term [agent memory](agent-memory.md), codebase understanding for [coding agents](coding-agents.md), and human exploration.

## Related

[GraphRAG](graphrag.md) · [Vector databases](vector-databases.md) · [Databases alternatives](../databases/alternatives.md) · [Concepts index](index.md)
