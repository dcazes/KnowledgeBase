---
type: Concept
title: Hindsight Overview
description: Hindsight's memory model — banks, world facts, experiences, observations and mental models; the retain, recall and reflect operations; and its four-strategy retrieval with rank fusion and reranking.
resource: https://hindsight.vectorize.io
tags: [hindsight, overview, memory-types, retrieval, reflect]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hindsight-github
    resource: "https://github.com/vectorize-io/hindsight"
    title: "vectorize-io/hindsight on GitHub"
    author: "site:github.com"
  - id: hindsight-paper
    resource: "https://arxiv.org/abs/2512.12818"
    title: "Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects"
    author: "arXiv 2512.12818"
---

# Hindsight — Overview

## Memory types

| Type | Example |
|---|---|
| World facts | "The stove gets hot" |
| Experiences | "I touched the stove and it hurt" — the agent's own history |
| Observations | Consolidated, evidence-backed beliefs formed from many memories |
| Mental models | The agent's learned understanding of its world, synthesised from observations and facts |

Memories are stored per **bank** (one per user, agent or project) as entities, relationships and time series with sparse and dense vector representations.

## Operations

* **Retain** — an LLM extracts facts, time data, entities and relationships from the input and normalises them into canonical entities and indexes.
* **Recall** — runs **semantic**, **BM25 keyword**, **graph** (entity / temporal / causal links) and **temporal** (time-range) retrieval in parallel, merges with reciprocal rank fusion, reranks with a cross-encoder and trims to a token budget.
* **Reflect** — a deeper pass over existing memories to form new connections or answer questions that need reasoning across many memories, shaped by the bank's configured disposition.

This blends [RAG](../../concepts/rag.md), [knowledge-graph](../../concepts/knowledge-graphs.md) links and temporal reasoning into one [agent memory](../../concepts/agent-memory.md) service.

## Hindsight models (Nov 2026)

Vectorize released open-weight decision, rerank and embedding models built specifically for agent memory, published on Hugging Face, for use with self-hosted deployments.

## Related

[Hindsight index](index.md) · [Snippets](snippets.md) · [Memory alternatives](../alternatives.md)
