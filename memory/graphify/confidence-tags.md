---
type: Reference
title: Graphify — Confidence Tags
description: What EXTRACTED / INFERRED / AMBIGUOUS mean on every graph edge, and how to read them when trusting the graph.
resource: https://github.com/Graphify-Labs/graphify
tags: [graphify, confidence, edges, extracted, inferred, ambiguous, trust]
generated: { by: "human:daniel", at: "2026-07-09T00:18:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:18:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: graphify-github-confidence-tags-in-readme
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify GitHub (confidence tags in README)"
    author: "site:github.com"
  - id: graphifyy-pypi-extracted-inferred-ambiguous-description
    resource: "https://pypi.org/project/graphifyy/"
    title: "graphifyy PyPI (EXTracted/INFERRED/AMBIGUOUS description)"
    author: "site:pypi.org"
---

# Graphify — Why confidence tags exist

A knowledge graph built by an LLM mixes two very different kinds of fact:

1. Something **explicitly stated** in your source (a function calls another; a doc says X depends on Y).
2. Something the model **derived** by resolving references, or **guessed** when resolution was uncertain.

Graphify labels every edge so you always know **what was found vs. guessed**. This is the core honesty feature — it's why the project claims to be "honest about what it found vs guessed."

# The three tags

| Tag | Meaning | Trust |
|-----|---------|-------|
| `EXTRACTED` | Relationship is **explicit in the source** (e.g. an `import`, a direct call, a sentence stating the link). | High — read directly. |
| `INFERRED` | Derived by **resolution** (e.g. matching a call site to its definition, following a type). Plausible but not literally stated. | Medium — usually right, verify for critical claims. |
| `AMBIGUOUS` | The model could not confidently resolve the link (name collision, missing context, weak signal). | Low — treat as a hypothesis. |

Example from upstream docs (Python extraction):

```
FastAPI --uses--> DefaultPlaceholder <--references-- get_request_handler() --references--> ModelField
RequestValidationError [uses] [INFERRED]
Dependant [uses] [INFERRED]
.get() [method] [EXTRACTED]
<-- __init__.py [imports] [EXTRACTED]
```

Here the `imports`/`method` edges are `EXTRACTED` (literally in code); the `uses` edges are `INFERRED` (resolved across files).

# How to use the tags

* **Trust EXTRACTED edges** as ground truth from your inputs.
* **Spot-check INFERRED edges** when a decision hinges on them.
* **Ignore or verify AMBIGUOUS edges** before relying on them.
* When querying, ask for provenance: a good answer cites which nodes/edges supported it, and their tags.

# Related controls

* `graphify extract ./docs --dedup-llm` — adds an LLM tiebreaker for ambiguous entity pairs (uses the same API key) to reduce `AMBIGUOUS` noise.
* `graphify extract ./docs --force` — rebuild cleanly after refactors (clears ghost duplicates that can produce false edges).
