---
type: Reference
title: Graphify — Usage
description: Core Graphify commands — add, extract, query, update, cluster-only, export, obsidian/wiki output, and the git hook — with the most useful flags.
resource: https://github.com/Graphify-Labs/graphify#usage
tags: [graphify, usage, cli, commands, extract, query, export]
generated: { by: "human:daniel", at: "2026-07-09T00:14:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:14:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: usage-github-readme
    resource: "https://github.com/Graphify-Labs/graphify#usage"
    title: "Usage (GitHub README)"
    author: "site:github.com"
  - id: graphifyy-pypi-command-reference
    resource: "https://pypi.org/project/graphifyy/"
    title: "graphifyy PyPI (command reference)"
    author: "site:pypi.org"
---

# Graphify — Two entry points

* **Slash command** (inside a supported agent like Hermes/Claude Code): `/graphify ./raw`
* **CLI** (terminal, any agent): `graphify <subcommand> <args>`

Both build into `graphify-out/` in the target project.

# Ingest: `add` (fetch remote content)

Pulls a URL into the graph — papers, tweets, videos, web pages:

```bash
graphify add https://arxiv.org/abs/1706.03762     # a paper
graphify add https://x.com/karpathy/status/...    # a tweet
graphify add <youtube-url>                         # transcribe + add a video
graphify add https://... --author "Name" --contributor "Name"
```

# Build: `extract`

The main graph builder over a local path:

```bash
graphify extract ./docs                  # default extraction + clustering
graphify extract ./docs --mode deep     # richer semantic extraction (extended prompt)
graphify extract ./docs --update        # re-extract only changed files
graphify extract ./docs --force         # overwrite even if fewer nodes (after refactors)
graphify extract ./docs --no-cluster    # raw extraction only, skip clustering
graphify extract ./docs --directed      # preserve edge direction
graphify extract ./docs --obsidian      # also emit an Obsidian vault
graphify extract ./docs --wiki          # build an agent-crawlable markdown wiki
graphify extract ./docs --no-viz        # skip the HTML visualization
graphify extract ./docs --token-budget 30000   # smaller chunks for small/local models
graphify extract ./docs --max-concurrency 2     # fewer parallel LLM calls (local inference)
graphify extract ./docs --api-timeout 900       # longer timeout for slow models
graphify extract ./docs --backend openai        # explicit backend
```

Optional inputs/introspection:
```bash
graphify extract --postgres "postgresql://user:pass@host/db"   # introspect a live DB schema
graphify extract ./my-workspace --cargo                        # Rust Cargo workspace deps
graphify extract ./docs --google-workspace                     # .gdoc/.gsheet/.gslides (needs gws auth)
graphify extract ./docs --global --as myrepo                  # register into the cross-project global graph
```

# Query

```bash
graphify query "what connects attention to the optimizer?"
graphify query "show the auth flow"
graphify query "..." --dfs --budget 1500        # depth-first traversal w/ token budget
graphify query "..." --graph graphify-out/graph.json
```

# Rebuild pieces: `cluster-only` / `update`

```bash
graphify update ./src --no-cluster        # raw AST graph only
graphify update ./src --force
graphify cluster-only ./my-project         # rerun clustering on existing graph
graphify cluster-only ./my-project --resolution 1.5      # more, smaller communities
graphify cluster-only ./my-project --exclude-hubs 99     # suppress super-hubs from rankings
graphify cluster-only ./my-project --no-label            # keep "Community N" placeholders
graphify cluster-only ./my-project --backend=gemini      # backend for community naming
```

# Export

```bash
graphify export callflow-html                      # Mermaid arch/call-flow HTML
graphify export callflow-html --output docs/arch.html
graphify export callflow-html --max-sections 8
graphify . --svg                  # graph.svg
graphify . --graphml             # for Gephi / yEd
graphify . --neo4j               # cypher.txt for Neo4j
graphify . --neo4j-push bolt://localhost:7687
graphify . --falkordb            # cypher.txt for FalkorDB
graphify . --falkordb-push falkordb://localhost:6379
```

# Git hook (auto-rebuild)

```bash
graphify hook install     # post-commit hook rebuilds the graph on every commit
```
No background process; triggers once per commit; safe alongside existing hooks.

# PR triage (GitHub)

```bash
graphify prs --triage       # AI ranks your review queue
graphify prs --conflicts    # PRs sharing graph communities (merge-order risk)
graphify prs --worktrees
graphify prs --base main
graphify prs --repo owner/repo
```

# Global graph (cross-project)

```bash
graphify global add graphify-out/graph.json --as myrepo   # register a project graph
```

# Useful env vars

| Var | Effect |
|-----|--------|
| `GRAPHIFY_MAX_WORKERS` | AST parallelism thread count |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Raise output cap for dense corpora |
| `GRAPHIFY_API_TIMEOUT` | Per-call timeout (default 600s) |
| `GRAPHIFY_FORCE` | Force rebuild even with fewer nodes |
| `GRAPHIFY_OLLAMA_NUM_CTX` | KV-cache window for Ollama |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Unload model after chunk (VRAM saving) |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend for `prs --triage` |

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `No solution found` on `uvx graphify` | `graphify` ≠ package `graphifyy` | use `uvx --from graphifyy graphify …` |
| `command not found` after pip/uv | not on PATH | add `~/.local/bin`; `uv tool update-shell` |
| Graph lost nodes after refactor | stale nodes linger | `graphify extract . --force` |
| Output truncated mid-string | model hit output-token limit | `GRAPHIFY_MAX_OUTPUT_TOKENS=32768` |
| Slow on local model | default timeouts/concurrency | `--api-timeout 900 --max-concurrency 2` |
