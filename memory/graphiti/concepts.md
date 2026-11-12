---
type: Concept
title: Graphiti Concepts
description: Graphiti's data model — episodes, entity nodes, fact edges with bi-temporal validity, sagas, communities, group ids and custom Pydantic ontologies.
resource: https://help.getzep.com/graphiti
tags: [graphiti, concepts, episodes, ontology, temporal, knowledge-graph]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphiti-github
    resource: "https://github.com/getzep/graphiti"
    title: "getzep/graphiti on GitHub"
    author: "site:github.com"
  - id: graphiti-docs
    resource: "https://help.getzep.com/graphiti"
    title: "Graphiti documentation"
    author: "site:help.getzep.com"
---

# Graphiti — Concepts

## Episodes

An **episode** is one unit of ingested data: a chat message, a paragraph of text, or a JSON record. Each has a `reference_time` (when it happened). Episodes are the ground truth: entities and facts derived from them keep a link back, so you can always ask "where did this come from?" and delete an episode to cascade-remove what only it created.

Episode types: `text`, `message` (speaker-prefixed chat lines) and `json` (structured records).

## Entities and facts

* **Entity nodes** have a name, a type, an evolving summary and an embedding.
* **Fact edges** connect two entities with a relationship and a natural-language fact ("Alice manages the payments team"). They carry `valid_at` / `invalid_at` (world time) plus creation/expiry timestamps (system time) — this is the *bi-temporal* model.

When a new episode contradicts an existing fact, Graphiti sets `invalid_at` on the old edge rather than deleting it.

## Sagas and communities

* A **saga** groups a sequence of related episodes (for example one long conversation) and can keep a running summary.
* **Communities** are clusters of closely connected entities with LLM-written summaries, useful for high-level questions — the same idea used by [Microsoft GraphRAG](../graphrag/index.md).

## Group ids

`group_id` partitions the graph — per user, per tenant, per project. Searches and deletes are scoped by group. Graphiti itself does not enforce access control; your service must map callers to groups.

## Ontology

Pass custom entity and edge types as [Pydantic](../../tools/pydantic/index.md) models to steer extraction (a *prescribed* ontology), or omit them and let types emerge (a *learned* ontology). You can also exclude entity types per episode.

## Related

[Graphiti index](index.md) · [Overview](overview.md) · [Snippets](snippets.md) · [Knowledge graphs](../../concepts/knowledge-graphs.md)
