---
type: Reference
title: Dify Model Providers
description: How Dify connects to models — provider plugins for OpenAI, Anthropic, Gemini and others, local models through Ollama, vLLM, LM Studio or any OpenAI-compatible API, gateways like LiteLLM, and system default models.
resource: https://docs.dify.ai
tags: [dify, model-providers, ollama, openai-compatible]
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

# Dify — Model Providers

Model providers are **plugins** installed from the marketplace. Configure them in *Settings → Model Provider*.

| Type | Examples |
|---|---|
| Hosted | OpenAI, Anthropic, Google Gemini, Azure OpenAI, Bedrock, Mistral, DeepSeek, OpenRouter |
| Local | [Ollama](../../runtime/ollama/index.md) (`http://host.docker.internal:11434` from Docker), [vLLM](../../runtime/vllm/index.md), [LM Studio](../../runtime/lmstudio/index.md), Xinference, LocalAI |
| Generic | "OpenAI-API-compatible" provider for any [compatible endpoint](../../concepts/openai-compatible-api.md), including a [LiteLLM](../../runtime/litellm/index.md) gateway |

Set **system default models** for reasoning, embeddings, reranking and speech; knowledge bases need an embedding model (see [Embeddings](../../concepts/embeddings.md)).

## Related

[Dify index](index.md) · [RAG pipeline](rag-pipeline.md)
