---
type: Reference
title: Graphify — MCP Server
description: Serve a built graph over MCP (stdio or HTTP) so any MCP-capable agent can query it; flags, auth, and container deployment.
resource: https://github.com/Graphify-Labs/graphify
tags: [graphify, mcp, model-context-protocol, server, integration]
generated: { by: "human:daniel", at: "2026-07-09T00:16:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:16:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: graphify-github-mcp-section
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify GitHub (MCP section)"
    author: "site:github.com"
  - id: graphifyy-pypi-serve-transport-flags
    resource: "https://pypi.org/project/graphifyy/"
    title: "graphifyy PyPI (serve / transport flags)"
    author: "site:pypi.org"
---

# Why an MCP server

Graphify's graph is most useful when your agent can *query it live* rather than reading a static report. The MCP server exposes the graph as tools (e.g. `query_graph`) to any MCP-capable client — Hermes, Claude Code, OpenCode, Cursor, etc.

# Start the server

```bash
# Build a graph first (if you haven't):
graphify extract ./docs --backend openai

# Serve it (stdio is the default transport):
python -m graphify.serve --graph graphify-out/graph.json

# Or start it directly from a built graph via the CLI shortcut:
graphify ./raw --mcp          # stdio MCP server
```

# Transports

| Transport | When | Notes |
|-----------|------|-------|
| `stdio` (default) | Local, one dev per process | Spawns one server per client; no network exposure. |
| `http` | Shared single process | MCP Streamable HTTP; one server serves many clients. |

```bash
# HTTP transport:
python -m graphify.serve graphify-out/graph.json --transport http --port 8080

# Expose beyond localhost (REQUIRES api-key):
python -m graphify.serve graphify-out/graph.json \
  --transport http --host 0.0.0.0 --api-key "$SECRET"

# Container:
docker run -p 8080:8080 graphify \
  python -m graphify.serve /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

# Flags

| Flag | Default | Meaning |
|------|---------|---------|
| `--transport` | `stdio` | `stdio` or `http` |
| `--host` | `127.0.0.1` | HTTP bind host (`0.0.0.0` to expose) |
| `--port` | `8080` | HTTP bind port |
| `--api-key` | env `GRAPHIFY_API_KEY` | Require `Authorization: Bearer` (or `X-API-Key`) |
| `--path` | `/mcp` | HTTP mount path |
| `--json-response` | off | Plain JSON instead of SSE streams |
| `--stateless` | off | No per-session state (CI/load-balanced) |
| `--session-timeout` | `3600` | Reap idle stateful sessions (`0` disables) |

> The default `127.0.0.1` bind is **loopback-only**. Only set `--host 0.0.0.0` **together with** `--api-key`.

# Client wiring examples

```bash
# Kimi (stdio):
kimi mcp add --transport stdio graphify -- python -m graphify.serve graphify-out/graph.json

# Generic MCP client config (HTTP):
# { "mcpServers": { "graphify": { "url": "http://127.0.0.1:8080/mcp" } } }
```

# Tools exposed

* `query_graph` — natural-language question over the graph.
* (Plus the standard MCP surface Graphify registers; see the server's tool list at runtime.)

Every `query_graph` call is logged to `~/.cache/graphify-queries.log` (JSON Lines: timestamp, question, community…) — useful for auditing what the agent asked.

# Fit with this stack

* **Hermes** can consume the HTTP MCP endpoint (`http://127.0.0.1:8080/mcp`) so it grounds answers in your graph.
* Pair with the **SearXNG → Graphify** ingestion pattern (see SearXNG [AI Integration](../../runtime/searxng/ai-integration.md)): search → `graphify add <url>` → serve over MCP.
