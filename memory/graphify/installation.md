---
type: Playbook
title: Graphify Installation
description: Install the graphifyy package with uv or pipx, register the skill with your coding assistant (user or project scope), and add optional extras for MCP, watch mode, Neo4j and SVG export.
resource: https://docs.graphify.com/quickstart
tags: [graphify, installation, uv, pipx, agent-skills]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphify-github
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify-Labs/graphify on GitHub"
    author: "site:github.com"
  - id: graphify-pypi
    resource: "https://pypi.org/project/graphifyy/"
    title: "graphifyy on PyPI"
    author: "site:pypi.org"
---

# Graphify — Installation

Requires Python 3.10+ and uv (recommended) or pipx.

```bash
uv tool install graphifyy          # or: pipx install graphifyy
graphify install                   # detects your assistant and registers the /graphify skill
graphify install --project                    # install the skill into this repo instead of your profile
graphify install --project --platform codex   # target a specific assistant
```

> The official package is **`graphifyy`**. Other `graphify*` packages on PyPI are unaffiliated — a classic typosquatting risk, see [Agent security](../../concepts/agent-security.md).

If `graphify` is not on PATH after a uv install, run `uv tool update-shell`.

## Extras

| Extra | Adds |
|---|---|
| `mcp` | MCP stdio server |
| `watch` | `graphify watch` auto-rebuild on file changes |
| `neo4j` | Push the graph to [Neo4j](../../databases/neo4j/index.md) |
| `svg` | SVG graph export |

```bash
uv tool install "graphifyy[mcp,watch]"
```

## Related

[Graphify index](index.md) · [Usage](usage.md) · [MCP server](mcp-server.md)
