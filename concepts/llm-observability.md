---
type: Concept
title: LLM Observability
description: Observing LLM applications and agents — traces of model calls, tools and retrieval, token and cost accounting, latency, prompt versions, OpenTelemetry GenAI conventions, gateways as a collection point, and the tools in this vault.
resource: https://opentelemetry.io/docs/specs/semconv/gen-ai/
tags: [concept, observability, tracing, opentelemetry, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: otel-genai
    resource: "https://opentelemetry.io/docs/specs/semconv/gen-ai/"
    title: "OpenTelemetry semantic conventions for generative AI"
    author: "OpenTelemetry"
  - id: langfuse
    resource: "https://langfuse.com/docs"
    title: "Langfuse documentation"
    author: "site:langfuse.com"
---

# LLM Observability

When an agent gives a bad answer, you need to see *why*: which documents were retrieved, which tools ran with what arguments, what each model call cost. **LLM observability** captures that as traces.

## What to capture

* **Traces and spans** — one per request/agent run, nested spans for each model call, tool call and retrieval.
* **Generations** — prompts, outputs, model, tokens, cost, latency.
* **Context** — user, session, prompt version, feature flags.
* **Quality signals** — scores from [evals](evals.md), user feedback.

**OpenTelemetry's GenAI semantic conventions** standardise these attributes, so frameworks ([Pydantic AI](../agents/pydanticAI/ai-integration.md), [CrewAI](../agents/crewai/ai-integration.md), [Claude Code](../agents/claude-code/ai-integration.md)) can export to any backend.

## Collection points

| Where | Tools |
|---|---|
| In the app | SDKs and OTel instrumentation → [Langfuse](../observability/langfuse/index.md), Logfire, Phoenix |
| At the gateway | [LiteLLM](../runtime/litellm/overview.md) callbacks, Tailscale [Aperture](../runtime/tailscale/ai-integration.md) hooks, Langfuse gateway |
| In platforms | [Dify](../agents/dify/ai-integration.md) tracing providers, [LightRAG](../memory/lightrag/ai-integration.md), [Open WebUI](../apps/openwebui/ai-integration.md) pipelines |
| Memory inspection | [OpenConcho](../memory/openconcho/index.md) for Honcho |

## Privacy

Traces contain user data and sometimes secrets: redact, set retention, and self-host where required ([Self-hosting](self-hosting.md)).

## Related

[Evals](evals.md) · [Observability alternatives](../observability/alternatives.md) · [Concepts index](index.md)
