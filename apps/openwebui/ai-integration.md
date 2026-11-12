---
type: Playbook
title: Open WebUI AI Integration
description: Wiring Open WebUI into an AI stack — model backends, SearXNG and Firecrawl for web, MCP and OpenAPI tool servers, Pipelines for filters and agents, LightRAG and memory, and SSO over Tailscale.
resource: https://docs.openwebui.com
tags: [open-webui, integration, mcp, pipelines, searxng]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openwebui-docs
    resource: "https://docs.openwebui.com"
    title: "Open WebUI documentation"
    author: "site:docs.openwebui.com"
---

# Open WebUI — AI Integration

| Layer | Options |
|---|---|
| Models | [Ollama](../../runtime/ollama/index.md), [vLLM](../../runtime/vllm/index.md), [llama.cpp](../../runtime/llamacpp/index.md), [LM Studio](../../runtime/lmstudio/index.md), [LiteLLM](../../runtime/litellm/index.md) |
| Web | [SearXNG](../../runtime/searxng/ai-integration.md) search, [Firecrawl](../../browsers/firecrawl/ai-integration.md) loader |
| Tools | [MCP](../../concepts/mcp.md) servers (via MCP support or the `mcpo` OpenAPI proxy), e.g. [Playwright MCP](../../browsers/playwright-mcp/index.md) |
| Agents and filters | Pipelines server: rate limits, PII filters, Langfuse tracing, custom agent pipelines ([LangGraph](../../agents/langgraph/index.md)) |
| Graph RAG | [LightRAG](../../memory/lightrag/ai-integration.md) as a model |
| Access | SSO and private reach via [Tailscale](../../runtime/tailscale/ai-integration.md) |

## Related

[Open WebUI index](index.md) · [Apps alternatives](../alternatives.md)
