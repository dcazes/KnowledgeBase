---
type: Playbook
title: llama.cpp AI Integration
description: Using llama.cpp directly in an AI stack — llama-server as an OpenAI-compatible backend for agents and UIs, tool calling with --jinja, embeddings and rerankers for RAG, and when to choose it over Ollama or vLLM.
resource: https://github.com/ggml-org/llama.cpp
tags: [llamacpp, integration, agents, rag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: llamacpp-server
    resource: "https://github.com/ggml-org/llama.cpp/tree/master/tools/server"
    title: "llama.cpp server README"
    author: "site:github.com"
---

# llama.cpp — AI Integration

## As a backend

`llama-server` speaks the [OpenAI API](../../concepts/openai-compatible-api.md), so it plugs into [LiteLLM](../litellm/index.md), [Open WebUI](../../apps/openwebui/index.md), [Graphiti](../../memory/graphiti/snippets.md), [PydanticAI](../../agents/pydanticAI/index.md) and coding agents such as [OpenCode](../../agents/opencode/index.md) and [Aider](../../agents/aider/index.md) by base URL.

* Start with `--jinja` so the model's chat template handles [tool calling](../../concepts/tool-calling.md).
* Run a second instance with `--embedding` (or `--reranking`) to serve [embeddings](../../concepts/embeddings.md) and rerankers for [RAG](../../concepts/rag.md).

## llama.cpp vs Ollama vs vLLM

| Choose | When |
|---|---|
| llama.cpp directly | You want maximum control over flags, the newest features first, or minimal footprint (edge devices, CPU-only servers) |
| [Ollama](../ollama/index.md) / [LM Studio](../lmstudio/index.md) | You want model management and a friendly UX on top of the same engine |
| [vLLM](../vllm/index.md) | Many concurrent users on datacentre GPUs |

## Related

[llama.cpp index](index.md) · [Local inference](../../concepts/local-inference.md)
