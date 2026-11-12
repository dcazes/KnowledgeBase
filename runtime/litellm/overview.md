---
type: Concept
title: LiteLLM Overview
description: What LiteLLM provides — a unified SDK, a self-hosted AI gateway with virtual keys, budgets, rate limits, load balancing, fallbacks and auto-routing, guardrails, MCP and A2A gateways, and observability callbacks.
resource: https://docs.litellm.ai
tags: [litellm, overview, gateway, routing, budgets]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: litellm-github
    resource: "https://github.com/BerriAI/litellm"
    title: "BerriAI/litellm on GitHub"
    author: "site:github.com"
  - id: litellm-docs
    resource: "https://docs.litellm.ai"
    title: "LiteLLM documentation"
    author: "site:docs.litellm.ai"
---

# LiteLLM — Overview

## Two products in one repo

| | Python SDK | AI Gateway (proxy) |
|---|---|---|
| Use | `litellm.completion(model="anthropic/...")` in code | A server on port 4000 that any OpenAI client can call |
| Adds | Provider translation, retries, `Router` | Virtual keys, teams, budgets, rate limits, admin UI, logging |
| State | None | PostgreSQL (keys, spend), optional Redis (caching, rate limits) |

## Core ideas

* **Provider prefixes.** `openai/…`, `anthropic/…`, `gemini/…`, `bedrock/…`, `ollama/…`, `hosted_vllm/…` select the backend; LiteLLM translates requests and responses into the OpenAI format (and exposes Anthropic's `/messages` format too).
* **Router.** Load-balance across deployments of the same model, retry, and fall back to other models on errors, timeouts or context-window overflow.
* **Auto-routing.** A complexity router can send simple prompts to a cheap model and hard ones to a strong model.
* **Virtual keys and budgets.** Issue per-user or per-team keys with model allow-lists, spend limits and rate limits; track cost per key.
* **Guardrails.** Plug-in checks (PII masking, prompt-injection detection, content moderation) before and after calls.
* **MCP gateway.** Register [MCP](../../concepts/mcp.md) servers once and let any model call their tools through `/chat/completions`, with per-key access control.
* **A2A.** An `/a2a` endpoint fronts [A2A](../../concepts/a2a.md) agents.
* **Observability.** Callbacks send traces and spend to [Langfuse](../../observability/langfuse/index.md), OpenTelemetry and others — see [LLM observability](../../concepts/llm-observability.md).

## When to use it

* Several apps or people share models and you want one endpoint, one place for keys, and cost visibility.
* You mix local and hosted models and want automatic fallback between them.
* You want to swap providers without touching application code.

## Related

[LiteLLM index](index.md) · [Configuration](configuration.md) · [OpenAI-compatible API](../../concepts/openai-compatible-api.md)
