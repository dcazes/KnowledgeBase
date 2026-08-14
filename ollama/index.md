---
type: Reference
title: Ollama
description: Local LLM runtime — pull/run open models on :11434 with an OpenAI-compatible API; compose file present but not running on this machine as of 2026-08-13.
resource: https://ollama.com
tags: [ollama, llm, local, inference, docker]
timestamp: 2026-08-13T00:00:00Z
---

# Ollama

**Local LLM runtime** — downloads and runs open-weight models (Llama, Qwen, Mistral, Gemma, Phi, …) with a simple CLI and an **OpenAI-compatible REST API** on `:11434`. The natural local inference backend for the rest of this stack (Mem0, LightRAG, AnythingLLM, LiteLLM, OpenWebUI).

On this machine: only `programs/ollama/docker-compose.yaml` exists (image `ollama/ollama:latest`, host port `11434:11434`, `restart: "no"`). **No binary, no running container** as of 2026-08-13.

## Contents

* [Overview](overview.md) — what Ollama is, model pull/run model, OpenAI-compatible API, GPU/CPU
* [Installation](installation.md) — Docker compose or native binary; pull + run; verify
* [Configuration](configuration.md) — model defaults, OLLAMA_HOST/OLLAMA_MODELS, keep_alive, embeddings
* [AI Integration](ai-integration.md) — OpenAI-compatible endpoint for LiteLLM/OpenWebUI/Mem0/LightRAG/AnythingLLM; Ollama embeddings
* [Snippets](snippets.md) — pull / run / list / ps / curl / python cheat sheet
* [Alternatives](alternatives.md) — llama.cpp, LM Studio, vLLM, GPT4All, LocalAI vs Ollama

## Related

* [LiteLLM](../agent-stack/index.md) — proxy in front of Ollama for unified API
* [AnythingLLM](../anythingllm/index.md), [OpenWebUI](../openwebui/index.md) — chat UIs that use Ollama as provider
* [Mem0](../mem0/index.md), [LightRAG](../lightrag/index.md) — can use Ollama as their local LLM/embedder

# Citations

[1] [Ollama docs](https://docs.ollama.com)
[2] [Ollama GitHub](https://github.com/ollama/ollama)
[3] [Docker Hub — ollama/ollama](https://hub.docker.com/r/ollama/ollama)

## Last verified

**2026-08-13** — Only `programs/ollama/docker-compose.yaml` present (compose, image `ollama/ollama:latest`); no binary, not running. Grounded on local compose file + upstream docs.
