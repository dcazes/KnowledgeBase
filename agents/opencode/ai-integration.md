---
type: Reference
title: OpenCode AI Integration
description: How OpenCode integrates with SearXNG (custom tool), Graphify (MCP), AnythingLLM (shared kb), Hermes co-existence, and the :4000 proxy.
resource: https://opencode.ai/docs/integrations
tags: [opencode, searxng, graphify, anythingllm, hermes, mcp, integrations]
generated: { by: "human:daniel", at: "2026-07-09T03:25:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:25:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: opencode-integrations-docs
    resource: "https://opencode.ai/docs/integrations"
    title: "OpenCode Integrations Docs"
    author: "site:opencode.ai"
  - id: opencode-github-repository-anomalyco
    resource: "https://github.com/anomalyco/opencode"
    title: "OpenCode GitHub repository (anomalyco)"
    author: "site:github.com"
  - id: searxng-project
    resource: "https://github.com/searxng/searxng"
    title: "SearXNG project"
    author: "site:github.com"
---

# OpenCode AI Integration

OpenCode plugs into a surrounding AI toolchain through custom tools, MCP servers, and shared knowledge folders.

## SearXNG — custom tool

SearXNG runs locally at `http://localhost:8080`. Expose it as a custom tool in `.opencode.json`:

```json
{
  "tools": {
    "web-search": {
      "command": "curl -s 'http://localhost:8080/search?q=$QUERY&format=json'",
      "description": "Search the web via local SearXNG instance",
      "env": {}
    }
  }
}
```

Then invoke in-session: `opencode "@TOOLS.md search for X"` or let the agent call `web-search`.

## Graphify — MCP server

Graphify is registered as an MCP server (see [configuration](configuration.md)):

```json
{ "mcpServers": { "graphify": { "url": "http://127.0.0.1:8000" } } }
```

Reference the Graphify MCP server doc: [/../../graphify/mcp-server.md](/../../graphify/mcp-server.md).

## AnythingLLM — shared knowledge

AnythingLLM shares a `kb/` folder with OpenCode. Point OpenCode context files at shared knowledge with the `@` syntax:

```bash
opencode "@kb/graphify/graph.json find orphaned nodes"
```

Keep the shared `kb/` folder as the single source of truth across tools.

## Hermes co-existence

OpenCode (interactive, per-project, supervised) and Hermes (background daemon, global, autonomous) complement each other. Use OpenCode for hands-on sessions and Hermes for background/scheduled work. See the [Hermes bundle](/../../hermes/index.md) and the [overview comparison](overview.md).

## The `:4000` proxy

An OpenAI-compatible failover proxy runs at `http://localhost:4000/v1` (OpenRouter/NIM). Point OpenCode's model at it for resilient model access:

```json
{
  "model": "openai/gpt-4o",
  "provider": { "openai": { "baseURL": "http://localhost:4000/v1", "apiKey": "sk-local" } }
}
```

## Verify

```bash
curl -s 'http://localhost:8080/search?q=test&format=json' | head   # SearXNG up?
curl -s http://127.0.0.1:8000 | head                              # Graphify MCP up?
curl -s http://localhost:4000/v1/models | head                    # :4000 proxy up?
```
