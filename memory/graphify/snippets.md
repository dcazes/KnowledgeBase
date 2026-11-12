---
type: Reference
title: Graphify Snippets
description: Graphify command cheat sheet — install, build, query, path, explain, hooks, watch, PR review, merge and export.
resource: https://docs.graphify.com/reference/overview
tags: [graphify, snippets, cli, cheat-sheet]
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

# Graphify — Snippets

```bash
# install
uv tool install graphifyy && graphify install

# build (inside the assistant)
/graphify .

# query from the shell
graphify query "how is a request authenticated?" --budget 3000 --depth 3
graphify path "FastAPI" "ModelField"
graphify explain "APIRouter"

# freshness
graphify hook install
graphify update .
graphify watch

# PRs
graphify prs
graphify prs --conflicts

# combine / export
graphify merge-graphs frontend.json backend.json
graphify export callflow-html
```

## Related

[Graphify index](index.md) · [Usage](usage.md)
