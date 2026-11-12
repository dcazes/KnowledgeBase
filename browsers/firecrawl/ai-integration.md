---
type: Playbook
title: Firecrawl AI Integration
description: Connecting Firecrawl to agents and RAG — the firecrawl-mcp server, framework loaders and tools, search-then-scrape loops with SearXNG, and ingestion into vector stores and memory.
resource: https://docs.firecrawl.dev
tags: [firecrawl, integration, mcp, rag, agents]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: firecrawl-github
    resource: "https://github.com/firecrawl/firecrawl"
    title: "firecrawl/firecrawl on GitHub"
    author: "site:github.com"
  - id: firecrawl-mcp
    resource: "https://github.com/firecrawl/firecrawl-mcp-server"
    title: "firecrawl-mcp-server"
    author: "site:github.com"
---

# Firecrawl — AI Integration

## MCP

```json
{ "mcpServers": { "firecrawl-mcp": {
    "command": "npx", "args": ["-y", "firecrawl-mcp"],
    "env": { "FIRECRAWL_API_KEY": "fc-...", "FIRECRAWL_API_URL": "http://localhost:3002" } } } }
```

Gives [Claude Code](../../agents/claude-code/index.md), [Cursor](../../editors/cursor/index.md), [Hermes](../../agents/hermes/index.md) and any [MCP](../../concepts/mcp.md) client scrape, search, crawl, map and extract tools. `FIRECRAWL_API_URL` points it at a self-hosted instance.

## Agent patterns

* **Search, then read:** `/search` already returns page content, collapsing the [SearXNG](../../runtime/searxng/index.md) + fetch loop into one call.
* **Research agents:** map a docs site, scrape the relevant pages, answer with citations.
* **Interact** for pages behind search boxes or pagination instead of a full [browser agent](../../concepts/browser-automation.md).

## RAG ingestion

Crawl a site to Markdown → chunk → embed → store in [Qdrant](../../databases/qdrant/index.md) or [pgvector](../../databases/pgvector/index.md), or hand the Markdown to [LightRAG](../../memory/lightrag/index.md), [Cognee](../../memory/cognee/index.md) or [Supermemory](../../memory/supermemory/index.md). Loaders exist for LangChain/[LangGraph](../../agents/langgraph/index.md), LlamaIndex, [CrewAI](../../agents/crewai/index.md) and [Dify](../../agents/dify/index.md); [n8n](../../apps/n8n/index.md) and [Open WebUI](../../apps/openwebui/index.md) can use it as their web loader.

## Caveats

Scraped pages are untrusted input and may contain prompt injections — see [Agent security](../../concepts/agent-security.md). Respect site terms and robots rules.

## Related

[Firecrawl index](index.md) · [RAG](../../concepts/rag.md) · [Web scraping & search](../../concepts/web-scraping.md)
