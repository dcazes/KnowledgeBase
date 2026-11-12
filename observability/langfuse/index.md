---
type: Software
title: Langfuse
description: Open-source AI engineering platform for agent observability and evals — OpenTelemetry-based tracing of LLM calls, tools and agents, prompt and skill management, LLM-as-judge and human evaluation, datasets and experiments, dashboards, and a beta AI gateway. Self-hosted or cloud; part of ClickHouse since 2026.
resource: https://langfuse.com
tags: [langfuse, observability, tracing, evals, prompt-management, opentelemetry]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langfuse-github
    resource: "https://github.com/langfuse/langfuse"
    title: "langfuse/langfuse on GitHub"
    author: "site:github.com"
  - id: langfuse-docs
    resource: "https://langfuse.com/docs"
    title: "Langfuse documentation"
    author: "site:langfuse.com"
---

# Langfuse

**Langfuse** records what your LLM application actually did: every model call, tool call, retrieval and agent step as a **trace**, with inputs, outputs, latency and cost. On top of traces it adds evaluation (LLM-as-judge, human annotation, custom scores), datasets and experiments, prompt versioning, and dashboards. It is the most popular open-source [LLM observability](../../concepts/llm-observability.md) platform.

| | |
|---|---|
| Category | [LLM observability](../../concepts/llm-observability.md) · [Evals](../../concepts/evals.md) |
| License | MIT (except `ee/` directories) |
| Language | TypeScript (web, worker); SDKs for Python (`langfuse` 5.2) and JS/TS |
| Latest release | v4.79.0 (2026-11-12) |
| Ownership | Part of ClickHouse since January 2026 |
| Deployment | Langfuse Cloud · self-hosted Docker Compose, Kubernetes (Helm), Terraform |

## Contents

* [Overview](overview.md) — traces, observations, scores, prompts, skills, gateway
* [Installation](installation.md) — Docker Compose, components
* [Snippets](snippets.md) — Python SDK, OpenAI drop-in, OpenTelemetry
* [AI Integration](ai-integration.md) — framework integrations and where to plug it in

## Related

* Concepts: [LLM observability](../../concepts/llm-observability.md) · [Evals](../../concepts/evals.md)
* Peers: [Ragas](../ragas/index.md), [promptfoo](../promptfoo/index.md); gateways [LiteLLM](../../runtime/litellm/index.md)
* Comparison: [Observability alternatives](../alternatives.md)
