---
type: Playbook
title: Crawl4AI AI Integration
description: Using Crawl4AI in AI pipelines — RAG ingestion into vector stores and GraphRAG tools, crawling as an agent tool, the hosted MCP server, and safety practices.
resource: https://docs.crawl4ai.com
tags: [crawl4ai, integration, rag, mcp, agents]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: crawl4ai-github
    resource: "https://github.com/unclecode/crawl4ai"
    title: "unclecode/crawl4ai on GitHub"
    author: "site:github.com"
---

# Crawl4AI — AI Integration

* **RAG ingestion:** crawl a docs site to fit-Markdown → chunk → embed → [Qdrant](../../databases/qdrant/index.md) / [pgvector](../../databases/pgvector/index.md), or feed [LightRAG](../../memory/lightrag/index.md) / [Cognee](../../memory/cognee/index.md) to build a graph. See [RAG](../../concepts/rag.md).
* **Agent tool:** wrap `arun()` as a tool in [PydanticAI](../../agents/pydanticAI/index.md), [LangGraph](../../agents/langgraph/index.md) or [CrewAI](../../agents/crewai/index.md); pair it with [SearXNG](../../runtime/searxng/index.md) for search-then-read.
* **MCP:** the cloud offers a hosted [MCP](../../concepts/mcp.md) server: `claude mcp add --transport http crawl4ai https://api.crawl4ai.com/mcp --header "Authorization: Bearer $CRAWL4AI_KEY"`.
* **Local models** for LLM extraction via Ollama or any LiteLLM provider string.

Scraped content is untrusted input; respect site terms and robots rules ([Agent security](../../concepts/agent-security.md)).

## Related

[Crawl4AI index](index.md) · [Web scraping & search](../../concepts/web-scraping.md)
