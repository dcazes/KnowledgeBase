---
type: Reference
title: Graphiti — AI Integration
description: Using Graphiti as temporal memory for agents (Hermes/OpenCode), its MCP server, and how it relates to the rest of your stack (incl. the :4000 proxy).
resource: https://github.com/getzep/graphiti
tags: [graphiti, integration, agents, hermes, opencode, mcp, memory, openai-compatible]
generated: { by: "human:daniel", at: "2026-07-09T05:06:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T05:06:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: mcp-server
    resource: "mcp-server.md"
    title: "MCP server"
  - id: vs-graphify
    resource: "vs-graphify.md"
    title: "vs Graphify"
  - id: hermes
    resource: "/../../hermes/index.md"
    title: "Hermes"
  - id: opencode
    resource: "/../../opencode/index.md"
    title: "OpenCode"
---

# Agent memory

Graphiti's primary use is **agent memory**: ingest interactions/episodes, query what's true now or historically. In your stack:

* **Hermes** (`~/.hermes/`) — could use Graphiti as a memory backend via the MCP server, or a custom skill calling `graphiti_core`.
* **OpenCode** (`.opencode.json`) — register the Graphiti MCP server as an `mcpServers` entry.
* **Claude / Cursor / Windsurf** — any MCP client can consume Graphiti memory.

# LLM / embeddings provider

Graphiti defaults to **OpenAI** for LLM + embeddings. It supports Anthropic/Gemini/Groq and **OpenAI-compatible endpoints** — so you could point it at your local **`:4000` proxy** (OpenRouter/NIM failover) instead of OpenAI, provided the model supports Structured Output.

```python
from graphiti_core import Graphiti
from graphiti_core.llm import LLMClient  # configure your OpenAI-compatible endpoint
```

# Versus the rest of the stack

| Layer | Tool |
|-------|------|
| Temporal memory | **Graphiti** |
| Static graph | Graphify (`/../../graphify/index.md`) |
| Agent runtime | Hermes (`/../../hermes/index.md`), OpenCode (`/../../opencode/index.md`) |
| Chat/RAG | OpenWebUI (`/../../openwebui/index.md`), AnythingLLM (`/../../anythingllm/index.md`) |
| Search | SearXNG (`/../../searxng/index.md`), Firecrawl (`/../../firecrawl/index.md`) |

# Notes

* Graphiti needs a graph DB (Neo4j) — heavier than Graphify's file-based approach.
* MCP server is the cleanest integration path for your agents.
