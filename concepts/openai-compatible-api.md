---
type: Concept
title: OpenAI-Compatible API
description: The OpenAI Chat Completions format as the de facto interface for LLMs — which servers and gateways implement it, the Anthropic Messages and Responses APIs, base-URL configuration, and the portability it gives every tool in the stack.
resource: https://platform.openai.com/docs/api-reference
tags: [concept, openai-compatible, api, gateway, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openai-api
    resource: "https://platform.openai.com/docs/api-reference"
    title: "OpenAI API reference"
    author: "OpenAI"
---

# OpenAI-Compatible API

The request/response shape of OpenAI's `/v1/chat/completions` (messages, tools, streaming) became the lingua franca of LLMs. Almost every model server and gateway implements it, so most tools only need a **base URL** and a key to switch models.

## Who speaks it

| Kind | Examples |
|---|---|
| Local servers | [Ollama](../runtime/ollama/snippets.md) (`/v1`), [vLLM](../runtime/vllm/index.md), [llama.cpp](../runtime/llamacpp/snippets.md) server, [LM Studio](../runtime/lmstudio/snippets.md), Docker [Model Runner](../runtime/docker/gpu-ai.md#docker-model-runner) |
| Gateways | [LiteLLM](../runtime/litellm/index.md), OpenRouter, Tailscale [Aperture](../runtime/tailscale/ai-integration.md), [Langfuse](../observability/langfuse/overview.md) gateway |
| Apps exposing it | [Open WebUI](../apps/openwebui/api.md), [AnythingLLM](../apps/anythingllm/snippets.md) |

## Other common shapes

* **Anthropic Messages API** (`/v1/messages`) — used by [Claude Code](../agents/claude-code/ai-integration.md); now also offered by Ollama, vLLM, LM Studio and LiteLLM.
* **OpenAI Responses API** — newer stateful format with built-in tools.
* **Native APIs** such as Ollama's `/api/chat`.

## Practical notes

* `api_key` is often ignored by local servers but must be non-empty in many SDKs.
* "Compatible" rarely means identical: tool calling, structured output and streaming details vary — test before relying on them.
* From inside Docker, `localhost` means the container; use service names or `host.docker.internal` ([Docker networks](../runtime/docker/volumes-networks.md)).

## Related

[Local inference](local-inference.md) · [Tool calling](tool-calling.md) · [Runtime alternatives](../runtime/alternatives.md) · [Concepts index](index.md)
