---
type: Software
title: Ollama
description: The most popular way to run open-weight LLMs locally — one-command install, a model library, a REST API with OpenAI- and Anthropic-compatible endpoints, tool calling, structured output, vision, embeddings, and launchers for coding agents; plus optional Ollama Cloud models.
resource: https://ollama.com
tags: [ollama, local-inference, llm, gguf, openai-compatible, go]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ollama-github
    resource: "https://github.com/ollama/ollama"
    title: "ollama/ollama on GitHub"
    author: "site:github.com"
  - id: ollama-docs
    resource: "https://docs.ollama.com"
    title: "Ollama documentation"
    author: "site:docs.ollama.com"
  - id: ollama-library
    resource: "https://ollama.com/library"
    title: "Ollama model library"
    author: "site:ollama.com"
---

# Ollama

**Ollama** makes running open models feel like using Docker: `ollama run gemma4` downloads a quantised model and starts a chat; a background server on port **11434** exposes it to apps. Nearly every tool in this vault that supports local models supports Ollama, which makes it the default entry point to [local inference](../../concepts/local-inference.md).

| | |
|---|---|
| Category | [Local inference](../../concepts/local-inference.md) |
| License | MIT |
| Language | Go (engine built on [llama.cpp](../llamacpp/index.md) / GGML) |
| Latest release | v0.40.16 (2026-11-09) |
| Platforms | macOS, Windows, Linux, Docker (`ollama/ollama`) |
| APIs | Native `/api/*`, [OpenAI-compatible](../../concepts/openai-compatible-api.md) `/v1/*`, Anthropic-compatible messages API |

## Contents

* [Overview](overview.md) — architecture, model library, capabilities, Ollama Cloud
* [Installation](installation.md) — install scripts, Docker, GPUs
* [Configuration](configuration.md) — environment variables, context length, Modelfiles
* [Snippets](snippets.md) — CLI, REST, Python/JS, OpenAI client
* [AI Integration](ai-integration.md) — `ollama launch` for coding agents, using Ollama behind other tools

## Related

* Concepts: [Local inference](../../concepts/local-inference.md) · [OpenAI-compatible API](../../concepts/openai-compatible-api.md) · [Tool calling](../../concepts/tool-calling.md) · [Embeddings](../../concepts/embeddings.md)
* Peers: [llama.cpp](../llamacpp/index.md), [LM Studio](../lmstudio/index.md), [vLLM](../vllm/index.md), Docker [Model Runner](../docker/gpu-ai.md#docker-model-runner); gateway [LiteLLM](../litellm/index.md)
* Front ends: [Open WebUI](../../apps/openwebui/index.md), [AnythingLLM](../../apps/anythingllm/index.md)
* Comparison: [Runtime alternatives](../alternatives.md)
