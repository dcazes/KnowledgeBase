---
type: Playbook
title: CrewAI AI Integration
description: CrewAI with the rest of the stack — any model through its LiteLLM-based LLM class, tools including MCP servers and web scrapers, external memory, and tracing to Langfuse or the AMP control plane.
resource: https://docs.crewai.com
tags: [crewai, integration, litellm, mcp, memory]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: crewai-docs
    resource: "https://docs.crewai.com"
    title: "CrewAI documentation"
    author: "site:docs.crewai.com"
---

# CrewAI — AI Integration

| Need | How |
|---|---|
| Models | `LLM(model="provider/model")` uses [LiteLLM](../../runtime/litellm/index.md) routing — OpenAI, Anthropic, [Ollama](../../runtime/ollama/index.md), [vLLM](../../runtime/vllm/index.md) |
| Tools | `crewai[tools]`, [MCP](../../concepts/mcp.md) servers, [Firecrawl](../../browsers/firecrawl/ai-integration.md), [Crawl4AI](../../browsers/crawl4ai/ai-integration.md), [SearXNG](../../runtime/searxng/ai-integration.md) |
| Memory | Built-in, or [Mem0](../../memory/mem0/ai-integration.md), [Zep](../../memory/zep/ai-integration.md), [Hindsight](../../memory/hindsight/ai-integration.md) integrations |
| Knowledge | Docs via [Docling](../../ingestion/docling/index.md) into knowledge sources |
| Tracing | [Langfuse](../../observability/langfuse/index.md) via OpenTelemetry, or CrewAI AMP |

## Related

[CrewAI index](index.md) · [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md)
