---
type: Playbook
title: Pydantic AI AI Integration
description: Pydantic AI in a wider stack — MCP tools and A2A exposure, memory layers as tools, Logfire and Langfuse tracing via OpenTelemetry, Pydantic Evals and Ragas, local models, and projects built on it.
resource: https://pydantic.dev/docs/ai/
tags: [pydantic-ai, integration, mcp, a2a, observability, evals]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: pydantic-ai-docs
    resource: "https://pydantic.dev/docs/ai/"
    title: "Pydantic AI documentation"
    author: "site:pydantic.dev"
---

# Pydantic AI — AI Integration

| Need | How |
|---|---|
| External tools | [MCP](../../concepts/mcp.md) servers as toolsets — [Playwright MCP](../../browsers/playwright-mcp/index.md), [Graphiti](../../memory/graphiti/mcp-server.md), [Firecrawl](../../browsers/firecrawl/ai-integration.md) |
| Agent-to-agent | Expose an agent over [A2A](../../concepts/a2a.md) |
| Memory | [Mem0](../../memory/mem0/ai-integration.md), [Zep](../../memory/zep/ai-integration.md), [Graphiti](../../memory/graphiti/ai-integration.md) as tools |
| Web search | [SearXNG](../../runtime/searxng/snippets.md) tool or the WebSearch capability |
| Observability | OpenTelemetry → Logfire or [Langfuse](../../observability/langfuse/index.md) ([LLM observability](../../concepts/llm-observability.md)) |
| Evals | Pydantic Evals (outputs and tool trajectories), [Ragas](../../observability/ragas/index.md), [promptfoo](../../observability/promptfoo/index.md) |
| Local models | [Ollama](../../runtime/ollama/index.md), [vLLM](../../runtime/vllm/index.md), [LiteLLM](../../runtime/litellm/index.md) |

Projects built on it include [browser-use](../../browsers/browser-use/index.md) 1.0 and Zep's reference agents.

## Related

[Pydantic AI index](index.md) · [Agent frameworks](../../concepts/agent-frameworks.md)
