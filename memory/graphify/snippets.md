---
type: Playbook
title: Graphify — Snippets & Cheat Sheet
description: Copy-paste commands for install, extract, query, MCP serve, Obsidian output, and the :4000 OpenRouter backend — the majority of daily Graphify use cases.
resource: https://github.com/Graphify-Labs/graphify
tags: [graphify, snippets, cheat-sheet, cli, mcp, obsidian]
generated: { by: "human:daniel", at: "2026-07-09T00:24:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:24:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: graphify-github
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify GitHub"
    author: "site:github.com"
  - id: graphifyy-pypi
    resource: "https://pypi.org/project/graphifyy/"
    title: "graphifyy PyPI"
    author: "site:pypi.org"
  - id: mcp-server-details
    resource: "mcp-server.md"
    title: "MCP server details"
  - id: backend-4000-proxy
    resource: "ai-integration.md"
    title: "Backend / :4000 proxy"
---

# Install

```bash
pip install graphifyy                 # package is graphifyy; command is graphify
uv tool install graphifyy             # recommended
graphify install --platform hermes    # register skill into Hermes
graphify --version
```

# Backend (this machine → :4000 OpenRouter/NIM proxy)

```bash
export OPENAI_BASE_URL=http://localhost:4000/v1
export OPENAI_API_KEY=sk-any-nonempty
graphify extract ./docs --backend openai
```

# Build a graph

```bash
graphify extract ./docs                       # default
graphify extract ./docs --mode deep           # richer extraction
graphify extract ./docs --update              # changed files only
graphify extract ./docs --obsidian            # emit Obsidian vault
graphify extract ./docs --wiki                # markdown wiki
graphify extract ./docs --no-viz              # skip HTML viz
graphify extract ./docs --force               # overwrite after refactor
```

# Ingest remote content

```bash
graphify add https://arxiv.org/abs/1706.03762
graphify add <youtube-url>
graphify add https://... --author "Name"
```

# Query

```bash
graphify query "what connects attention to the optimizer?"
graphify query "show the auth flow" --graph graphify-out/graph.json
```

# MCP server

```bash
# stdio (default, local)
python -m graphify.serve graphify-out/graph.json

# HTTP (shared)
python -m graphify.serve graphify-out/graph.json --transport http --port 8080

# Expose (requires api-key)
python -m graphify.serve graphify-out/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"

# CLI shortcut
graphify ./raw --mcp
```

Client config (HTTP):
```json
{ "mcpServers": { "graphify": { "url": "http://127.0.0.1:8080/mcp" } } }
```

# Rebuild pieces

```bash
graphify cluster-only ./my-project --resolution 1.5
graphify cluster-only ./my-project --exclude-hubs 99
graphify update ./src --force
```

# Export

```bash
graphify export callflow-html --output docs/arch.html
graphify . --svg
graphify . --neo4j-push bolt://localhost:7687
```

# Git hook (auto-rebuild on commit)

```bash
graphify hook install
```

# Global graph (cross-project)

```bash
graphify global add graphify-out/graph.json --as myrepo
```

# Env vars (quick ref)

| Var | Effect |
|-----|--------|
| `OPENAI_BASE_URL` | OpenAI-compatible endpoint (`:4000/v1`) |
| `ANTHROPIC_API_KEY` / `ANTHROPIC_BASE_URL` | Claude backend |
| `GEMINI_API_KEY` | Gemini backend |
| `OLLAMA_BASE_URL` / `OLLAMA_MODEL` | local Ollama |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | raise cap for dense corpora |
| `GRAPHIFY_API_TIMEOUT` | per-call timeout (default 600) |
| `GRAPHIFY_FORCE` | force rebuild even if fewer nodes |

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `uvx graphify` → No solution | package is `graphifyy` | `uvx --from graphifyy graphify …` |
| `command not found` | not on PATH | add `~/.local/bin`; `uv tool update-shell` |
| No API key error | backend needs creds | set `OPENAI_BASE_URL=:4000/v1` + key |
| Lost nodes after refactor | stale nodes | `graphify extract . --force` |
| Output truncated | output-token limit | `GRAPHIFY_MAX_OUTPUT_TOKENS=32768` |
