---
type: Concept
title: Cognee Overview
description: How Cognee works — remember, recall, improve and forget; graph, vector and code memory; session distillation; ontologies; and its no-LLM local extraction mode.
resource: https://docs.cognee.ai/core-concepts/architecture
tags: [cognee, overview, architecture, knowledge-graph, sessions]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cognee-docs
    resource: "https://docs.cognee.ai"
    title: "Cognee documentation"
    author: "site:docs.cognee.ai"
  - id: cognee-paper
    resource: "https://arxiv.org/abs/2505.24478"
    title: "Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning"
    author: "Markovic et al., arXiv 2505.24478"
---

# Cognee — Overview

## Four operations

| Operation | What it does |
|---|---|
| `remember` | Store content or code in permanent memory, or in a session when a session id is supplied |
| `recall` | Retrieve context (and optionally a generated answer) using automatic routing or a chosen search strategy |
| `improve` | Enrich memory, apply feedback, and bridge session knowledge into the permanent graph |
| `forget` | Remove an item or a whole dataset |

Earlier releases exposed the pipeline steps directly (`add` → `cognify` → `search`); the 2026 API wraps them in these higher-level verbs.

## What gets built

* **Text** → entities and relationships in a [knowledge graph](../../concepts/knowledge-graphs.md), plus embedded chunks in a [vector store](../../concepts/vector-databases.md).
* **Code** → a graph of symbols and dependencies (similar in spirit to [Graphify](../graphify/index.md)).
* **Sessions** → short-term memory per conversation; `improve` distils accepted lessons into durable knowledge another session can retrieve.

Retrieval combines graph traversal and vector similarity, so Cognee belongs to the [GraphRAG](../../concepts/graphrag.md) family. Its research paper (arXiv 2505.24478) studies how to tune the graph-to-LLM interface for multi-hop reasoning.

## Ontologies

You can ground extraction in your domain with custom data models and ontology files, so the graph uses your entity and relationship types rather than generic ones.

## Running without an LLM

With no LLM key configured, Cognee extracts entities with a small local model (GLiNER) and embeds with a local embedding model. Ingestion, retrieval and sessions work; generated answers and LLM-based enrichment are skipped. Add a key (or a local LLM) for answer generation.

## Related

[Cognee index](index.md) · [Snippets](snippets.md) · [Agent memory](../../concepts/agent-memory.md)
