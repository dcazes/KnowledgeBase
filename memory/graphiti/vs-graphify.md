---
type: Comparison
title: Graphiti vs Graphify
description: Graphiti and Graphify both build knowledge graphs but solve different problems — temporal agent memory over evolving data versus a one-shot structural map of a codebase or document folder.
resource: https://github.com/getzep/graphiti
tags: [graphiti, graphify, comparison, knowledge-graph]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphiti-github
    resource: "https://github.com/getzep/graphiti"
    title: "getzep/graphiti on GitHub"
    author: "site:github.com"
  - id: graphify-github
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify-Labs/graphify on GitHub"
    author: "site:github.com"
---

# Graphiti vs Graphify

Both produce [knowledge graphs](../../concepts/knowledge-graphs.md), which makes them easy to confuse.

| | Graphiti | [Graphify](../graphify/index.md) |
|---|---|---|
| Input | A continuous stream of episodes (messages, records, text) | A folder: code, docs, SQL schemas, configs, PDFs |
| Output | A live temporal graph in Neo4j / FalkorDB / Neptune | A graph file plus a report you can query |
| Time | Bi-temporal facts; old facts invalidated, not deleted | A snapshot of the folder; rebuild to refresh |
| Typical user | An application giving agents long-term memory | A developer or coding agent trying to understand a codebase |
| Interface | Python library, reference MCP/REST servers | Coding-assistant skill, CLI, MCP server |

## When to use which

* "Remember what the user told me last month, and notice when it changed" → **Graphiti**.
* "Map this repository so my coding agent stops re-reading every file" → **Graphify**.

They can coexist: Graphify for codebase structure, Graphiti for what happens over time.

## Related

[Graphiti index](index.md) · [Graphify index](../graphify/index.md) · [GraphRAG](../../concepts/graphrag.md) · [Memory alternatives](../alternatives.md)
