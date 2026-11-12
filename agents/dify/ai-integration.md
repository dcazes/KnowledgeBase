---
type: Playbook
title: Dify AI Integration
description: Dify in a wider AI stack — local models via Ollama or LiteLLM, web data from Firecrawl and SearXNG, MCP in both directions, memory via Hindsight, tracing to Langfuse, and when to choose Dify over n8n or code frameworks.
resource: https://docs.dify.ai
tags: [dify, integration, mcp, langfuse, n8n]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: dify-docs
    resource: "https://docs.dify.ai"
    title: "Dify documentation"
    author: "site:docs.dify.ai"
---

# Dify — AI Integration

| Need | Integration |
|---|---|
| Models | [Ollama](../../runtime/ollama/index.md), [vLLM](../../runtime/vllm/index.md), [LiteLLM](../../runtime/litellm/index.md) via provider plugins |
| Web data | [Firecrawl](../../browsers/firecrawl/ai-integration.md) and [SearXNG](../../runtime/searxng/ai-integration.md) tools |
| Tools | [MCP](../../concepts/mcp.md) servers as tools; publish Dify apps as MCP servers for [Claude Code](../claude-code/index.md) and others |
| Memory | Conversation variables; [Hindsight](../../memory/hindsight/ai-integration.md) integration for long-term memory |
| Observability | Langfuse, LangSmith, Opik and others — [Langfuse](../../observability/langfuse/index.md), [LLM observability](../../concepts/llm-observability.md) |
| Automation | Trigger Dify workflows from [n8n](../../apps/n8n/index.md) via the API |

## Choosing

* **Dify** — LLM-centric apps and RAG built by mixed technical/non-technical teams.
* [n8n](../../apps/n8n/index.md) — integration-heavy automations across hundreds of SaaS apps.
* [LangGraph](../langgraph/index.md) / [Pydantic AI](../pydanticAI/index.md) — when you need code-level control and testing.

## Related

[Dify index](index.md) · [Agents alternatives](../alternatives.md)
