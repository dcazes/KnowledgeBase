---
type: Reference
title: Graphiti MCP Server
description: Graphiti's reference Model Context Protocol server — Docker setup with FalkorDB or Neo4j, HTTP and stdio transports, config.yaml, the full tool list, and its security limits.
resource: https://github.com/getzep/graphiti/tree/main/mcp_server
tags: [graphiti, mcp, mcp-server, falkordb, neo4j, agent-memory]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphiti-mcp
    resource: "https://github.com/getzep/graphiti/tree/main/mcp_server"
    title: "Graphiti MCP Server README"
    author: "site:github.com"
  - id: mcp-spec
    resource: "https://modelcontextprotocol.io"
    title: "Model Context Protocol"
    author: "site:modelcontextprotocol.io"
---

# Graphiti — MCP Server

The `mcp_server/` folder in the Graphiti repo is a **reference** [MCP](../../concepts/mcp.md) server that lets any MCP client — [Claude Code](../../agents/claude-code/index.md), [Cursor](../../editors/cursor/index.md), [OpenCode](../../agents/opencode/index.md), [Hermes](../../agents/hermes/index.md) — use a Graphiti graph as long-term memory.

## Run it

```bash
git clone https://github.com/getzep/graphiti && cd graphiti/mcp_server
docker compose up                                        # FalkorDB + MCP server in one container
docker compose -f docker/docker-compose-neo4j.yml up     # or: Neo4j in a separate container
```

Point HTTP-capable clients at `http://localhost:8000/mcp/`. For stdio-only clients, run the server with `uv` and `transport: stdio`.

## Configuration (`config.yaml`)

* `server.transport`: `http` (default) or `stdio`
* `database.provider`: `falkordb` (default) or `neo4j`
* LLM providers: OpenAI, Anthropic, Gemini, Groq, Azure OpenAI; Ollama via `api_base: http://localhost:11434/v1`
* Embedders: OpenAI, Voyage, Sentence Transformers, Gemini
* `entity_types`: built-in types such as Organization, Document and Object, which you can extend
* `structured_output_mode`: `json_schema` or `json_object` — use `json_object` if a local endpoint returns objects missing required fields

## Tools

| Tool | Purpose |
|---|---|
| `add_memory` | Add an episode (text, JSON or messages) with reference time and optional saga |
| `add_triplet` | Add one fact directly, bypassing extraction |
| `search_nodes` | Hybrid search over entities |
| `search_memory_facts` | Search facts, with `valid_at` / `invalid_at` date filters |
| `get_episodes` · `get_episode_entities` | Read episodes and trace what each produced |
| `summarize_saga` · `build_communities` | Higher-level summaries |
| `get_entity_edge` · `delete_entity_edge` · `delete_episode` · `clear_graph` | Inspect and delete |
| `get_status` | Server and database health |

## Security limits

The reference servers have **no authentication, no authorization and no prompt-injection filtering**, and since v0.31.2 listen on localhost only by default. Any caller can read or delete any `group_id`. Do not expose them to an untrusted network; for production, wrap `graphiti-core` in your own service or use [Zep](../zep/index.md). See [Agent security](../../concepts/agent-security.md).

## Related

[Graphiti index](index.md) · [AI Integration](ai-integration.md) · [MCP](../../concepts/mcp.md)
