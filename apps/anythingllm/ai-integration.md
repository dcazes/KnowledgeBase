---
type: Reference
title: AnythingLLM — AI Integration
description: Connecting AnythingLLM to your stack — SearXNG web search, Firecrawl extract, Graphify MCP, and the :4000 inference proxy.
resource: https://docs.anythingllm.com
tags: [anythingllm, integration, searxng, firecrawl, graphify, mcp, openai-compatible]
timestamp: 2026-07-09T02:35:00Z
---

# Models via the :4000 proxy

Like OpenWebUI, AnythingLLM can use any **OpenAI-compatible** endpoint. Since no Ollama runs locally here, point it at your `:4000` proxy:
```
Settings → AI Providers → OpenAI-compatible
Base URL:  http://localhost:4000/v1
API Key:   <proxy-accepted value>
```
The agent then reasons through cloud models via the proxy.

# Web search via SearXNG

Configure the Web Search skill (see [Agent Skills](agent-skills.md)):
```
Provider: SearXNG
URL:      http://searxng:8080   (or http://localhost:8080)
```
Private metasearch results feed RAG/chat — no third-party search API needed.

# Extraction via Firecrawl

Firecrawl isn't a built-in AnythingLLM skill, but you can:
* Add a **custom API skill** that calls `http://localhost:3002/v1/scrape` (or `/v1/search`) — Firecrawl returns clean Markdown/JSON.
* Or pre-scrape with Firecrawl and drop the Markdown into a workspace for RAG.

# Knowledge graph via Graphify (MCP)

Register Graphify's MCP server so the agent queries your graph:
```
MCP: graphify  (stdio: python -m graphify.serve)
```
(See [Graphify MCP](/../../graphify/mcp-server.md).)

# Summary of wiring

| Need | Tool | Endpoint |
|------|------|----------|
| Inference | `:4000` proxy | `http://localhost:4000/v1` |
| Web search | SearXNG | `http://localhost:8080` |
| Deep extract | Firecrawl | `http://localhost:3002` |
| Graph RAG | Graphify MCP | `python -m graphify.serve` |

# Citations

[1] [Overview](overview.md)
[2] [SearXNG](/../../searxng/index.md)
[3] [Firecrawl](/../../firecrawl/index.md)
[4] [Graphify](/../../graphify/index.md)
