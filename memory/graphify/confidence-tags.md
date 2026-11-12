---
type: Concept
title: Graphify Confidence Tags
description: Why every Graphify edge carries an EXTRACTED or INFERRED tag, how to read them, and how this provenance helps agents avoid acting on guessed relationships.
resource: https://github.com/Graphify-Labs/graphify
tags: [graphify, provenance, confidence, knowledge-graph]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphify-github
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify-Labs/graphify on GitHub"
    author: "site:github.com"
---

# Graphify — Confidence Tags

Every edge is tagged:

* **`EXTRACTED`** — explicit in the source (an import statement, a direct call, a method defined on a class).
* **`INFERRED`** — derived by Graphify's resolution (a call resolved through a re-export, a type relationship worked out across files).

```text
Connections (47):
  --> RequestValidationError [uses] [INFERRED]
  --> .get() [method] [EXTRACTED]
```

## Why it matters

Graphs built by LLMs often mix facts with guesses invisibly. Tagging each edge lets a human or agent:

* trust `EXTRACTED` edges for refactors and impact analysis;
* double-check `INFERRED` edges against the source before acting;
* weigh answers by provenance — the same principle behind [Graphiti](../graphiti/index.md)'s episodes and this vault's own `sources:` frontmatter.

Provenance is a recurring theme across [knowledge graphs](../../concepts/knowledge-graphs.md) and [agent memory](../../concepts/agent-memory.md): know what was observed versus concluded.

## Related

[Graphify index](index.md) · [Overview](overview.md)
