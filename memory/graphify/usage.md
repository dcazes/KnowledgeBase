---
type: Playbook
title: Graphify Usage
description: Day-to-day Graphify workflow — building a graph, the three output files, querying from the assistant or CLI, ignore rules, git hooks for automatic rebuilds, PR review commands and graph merging.
resource: https://docs.graphify.com/guides/querying
tags: [graphify, usage, workflow, git-hooks, pr-review]
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

# Graphify — Usage

## Build

In your assistant: `/graphify .`. Output lands in `graphify-out/`:

```
graphify-out/
├── graph.html        interactive graph: click nodes, filter, search
├── GRAPH_REPORT.md   key concepts, surprising connections, suggested questions
└── graph.json        the full graph, with schema and graphify version fields
```

Graphify honours `.gitignore`, a project `.graphifyignore` and `--exclude` patterns.

## Query

From the assistant or the shell:

```bash
graphify query "what connects auth to the database?"   # scoped subgraph, default budget 2000, depth 2
graphify path "UserService" "DatabasePool"             # shortest path between two nodes
graphify explain "RateLimiter"                          # one node, its community and connections
```

An ambiguous name is refused with the candidate list instead of guessed.

## Keep it fresh

```bash
graphify hook install     # rebuild on commit and branch checkout
graphify update .         # after git pull
graphify watch            # rebuild on file changes (watch extra)
```

## Review pull requests

```bash
graphify prs              # dashboard: CI state, review status, worktrees
graphify prs 42           # graph impact of PR #42
graphify prs --conflicts  # PRs touching the same communities: merge-order risk
graphify prs --triage     # AI-ranked review queue
```

## Combine and export

```bash
graphify merge-graphs a.json b.json
graphify export callflow-html     # Mermaid call-flow HTML
```

Queries are logged to `~/.cache/graphify-queries.log` (JSON Lines).

## Related

[Graphify index](index.md) · [Snippets](snippets.md) · [Confidence tags](confidence-tags.md)
