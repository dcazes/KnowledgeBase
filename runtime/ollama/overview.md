---
type: Concept
title: Ollama Overview
description: What Ollama is — model registry pull/run, OpenAI-compatible REST API on :11434, embeddings endpoint, GPU/CPU support.
resource: https://docs.ollama.com
tags: [ollama, overview, llm, api]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: ollama-docs-api
    resource: "https://docs.ollama.com/api"
    title: "Ollama docs — API"
    author: "site:docs.ollama.com"
  - id: ollama-github
    resource: "https://github.com/ollama/ollama"
    title: "Ollama GitHub"
    author: "site:github.com"
---

# Ollama — Overview

Ollama is the easiest way to run open-weight LLMs locally: `ollama pull llama3.1` then `ollama run llama3.1`. It handles quantization, model files, GPU offload (CUDA/ROCm) with CPU fallback, and serves an OpenAI-compatible API on `:11434`.

## Model workflow

* `ollama pull <model>` — download (registry of ~100k tags, e.g. `llama3.1`, `qwen2.5`, `gemma3`, `mistral`, `phi4`, `deepseek-r1`, `nomic-embed-text` for embeddings).
* `ollama run <model>` — interactive REPL.
* Models persist under `OLLAMA_MODELS` (default `~/.ollama/models`).

## API (OpenAI-compatible)

* `POST /api/generate` — raw generation (`{"model": "llama3.1", "prompt": "…", "stream": false}`).
* `POST /api/chat` — chat messages.
* `POST /api/embed` — embeddings (e.g. `nomic-embed-text`).
* `POST /v1/chat/completions` + `/v1/embeddings` — OpenAI-compatible surface for existing SDKs/tools.
* `GET /api/tags`, `POST /api/pull` — model management.

## Why it fits this stack

Single local inference point for [Mem0](../../memory/mem0/index.md), [LightRAG](../../memory/lightrag/index.md), [AnythingLLM](../../apps/anythingllm/index.md), [OpenWebUI](../../apps/openwebui/index.md), and the [agent stack](../../agents/agent-stack/index.md) (via LiteLLM proxy) — no cloud keys, `:11434` shared.
