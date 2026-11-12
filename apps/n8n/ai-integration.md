---
type: Playbook
title: n8n AI Integration
description: n8n with the rest of an AI stack — local models via Ollama or LiteLLM, vector stores, MCP client tools and MCP server triggers, memory services, calling Dify or LangGraph services, web data via Firecrawl and SearXNG, and tracing.
resource: https://docs.n8n.io/advanced-ai/
tags: [n8n, integration, mcp, ollama, rag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: n8n-ai
    resource: "https://docs.n8n.io/advanced-ai/"
    title: "n8n advanced AI"
    author: "site:docs.n8n.io"
---

# n8n — AI Integration

| Need | How |
|---|---|
| Models | Ollama chat model node, OpenAI node with custom base URL → [LiteLLM](../../runtime/litellm/index.md) / [vLLM](../../runtime/vllm/index.md) |
| RAG | Vector store nodes for [Qdrant](../../databases/qdrant/index.md), [pgvector](../../databases/pgvector/index.md); document loaders; [Docling](../../ingestion/docling/index.md) via HTTP |
| Web | HTTP nodes to [SearXNG](../../runtime/searxng/ai-integration.md) and [Firecrawl](../../browsers/firecrawl/ai-integration.md) |
| Tools in | MCP Client tool → any [MCP](../../concepts/mcp.md) server |
| Tools out | MCP Server Trigger → workflows callable from [Claude Code](../../agents/claude-code/index.md), [Cursor](../../editors/cursor/index.md), [Hermes](../../agents/hermes/index.md) |
| Memory | Postgres/Redis chat memory; [Zep](../../memory/zep/index.md), [Hindsight](../../memory/hindsight/ai-integration.md) integrations |
| Other agent services | HTTP calls to [Dify](../../agents/dify/api.md) apps or [LangGraph](../../agents/langgraph/ai-integration.md) servers |

## Related

[n8n index](index.md) · [Workflow automation](../../concepts/workflow-automation.md)
