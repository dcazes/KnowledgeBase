---
type: Concept
title: Graphify Overview
description: How Graphify works — deterministic tree-sitter parsing for ~40 languages, an optional semantic pass for docs and media, Leiden communities, god nodes, rationale nodes, and why it is a graph rather than a vector index.
resource: https://docs.graphify.com/concepts/architecture
tags: [graphify, overview, tree-sitter, leiden, code-graph]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphify-github
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify-Labs/graphify on GitHub"
    author: "site:github.com"
  - id: graphify-docs
    resource: "https://docs.graphify.com"
    title: "Graphify documentation"
    author: "site:docs.graphify.com"
---

# Graphify — Overview

## What it builds

| Capability | Detail |
|---|---|
| Cross-file links | `calls`, `imports`, `inherits`, `mixes_in` resolved across ~40 languages via tree-sitter AST |
| Communities | The graph split into subsystems with Leiden clustering, labelled without an LLM |
| God nodes | The most-connected concepts — what everything flows through |
| Rationale nodes | `# NOTE:` / `# WHY:` comments and ADR/RFC citations become nodes linked to the code |
| Beyond code | Docs, PDFs, images and audio/video join the same graph via a semantic pass |

## Local-first by design

Code is parsed **deterministically** with tree-sitter: no LLM, nothing leaves the machine, no token cost. Only the semantic pass over docs and media calls a model — your assistant's model or a configured API key.

## Not a vector index

There are no embeddings and no vector store. Graphify gives you a graph to traverse: ask a question, find the shortest path between two symbols, or explain one concept and its neighbours. This is the [GraphRAG](../../concepts/graphrag.md) idea applied to code, contrasting with embedding-based codebase search in editors like [Cursor](../../editors/cursor/index.md).

## Benchmarks (self-reported)

On LoCoMo (n=300) Graphify reports recall@10 of 0.497 versus 0.149 for Supermemory and 0.048 for Mem0, with 45.3% QA accuracy; on LongMemEval-S (n=50) 76% QA accuracy, tied with dense RAG; all with zero LLM credits for graph building. These are the vendor's numbers on its own harness — treat them as indicative. See [Evals](../../concepts/evals.md).

## Related

[Graphify index](index.md) · [Usage](usage.md) · [Confidence tags](confidence-tags.md)
