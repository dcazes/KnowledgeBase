---
type: Playbook
title: Langfuse AI Integration
description: Where to plug Langfuse into an AI stack — LiteLLM callbacks, LangGraph and LangChain handlers, Pydantic AI and CrewAI via OpenTelemetry, Dify and Open WebUI pipelines, LightRAG tracing, and pairing with Ragas and promptfoo for evals.
resource: https://langfuse.com/docs/integrations
tags: [langfuse, integration, litellm, langgraph, opentelemetry]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langfuse-docs
    resource: "https://langfuse.com/docs"
    title: "Langfuse documentation"
    author: "site:langfuse.com"
---

# Langfuse — AI Integration

| Source | How |
|---|---|
| [LiteLLM](../../runtime/litellm/configuration.md) | `success_callback: ["langfuse"]` — every call through the gateway traced |
| [LangGraph](../../agents/langgraph/ai-integration.md) / LangChain | Langfuse callback handler |
| [Pydantic AI](../../agents/pydanticAI/ai-integration.md), [CrewAI](../../agents/crewai/ai-integration.md), OpenAI Agents SDK | OpenTelemetry instrumentation |
| [Dify](../../agents/dify/ai-integration.md) | Built-in tracing provider |
| [Open WebUI](../../apps/openwebui/ai-integration.md) | Pipelines filter |
| [LightRAG](../../memory/lightrag/ai-integration.md) | Built-in Langfuse tracing |

## Workflow

1. Trace production traffic.
2. Turn interesting traces into **dataset** items.
3. Run experiments with LLM-as-judge or [Ragas](../ragas/index.md) metrics; gate releases with [promptfoo](../promptfoo/index.md) in CI.
4. Version prompts and skills; compare scores across versions.

## Related

[Langfuse index](index.md) · [LLM observability](../../concepts/llm-observability.md)
