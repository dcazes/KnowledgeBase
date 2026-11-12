---
type: Concept
title: Ollama Overview
description: How Ollama works — a local server that manages GGUF models and runs them on a llama.cpp-based engine; the model library and tags; capabilities such as tools, structured outputs, thinking, vision, embeddings, web search and speech; and Ollama Cloud.
resource: https://docs.ollama.com
tags: [ollama, overview, architecture, capabilities, cloud]
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
---

# Ollama — Overview

## Architecture

* A long-running **server** (`ollama serve`, started automatically by the desktop apps and the Linux service) listens on `127.0.0.1:11434`.
* Models are stored as content-addressed blobs (GGUF weights plus a Modelfile: template, parameters, system prompt) in `~/.ollama/models`.
* Inference runs on an engine built on [llama.cpp](../llamacpp/index.md)/GGML, with CUDA, ROCm, Metal and Vulkan acceleration. Models are loaded on demand and unloaded after `OLLAMA_KEEP_ALIVE` (default 5 min).

## Model library

`ollama pull <name>:<tag>` fetches from ollama.com/library. Tags pick size and quantisation (e.g. `qwen3:8b`, `gemma4:31b`, `-q4_K_M`). Late-2026 library highlights include Gemma 4, Qwen 3.x, gpt-oss, DeepSeek, Kimi, GLM, MiniMax, Liquid LFM3 and NVIDIA Nemotron. You can also import any GGUF or Safetensors model with a Modelfile. See [Quantization in local inference](../../concepts/local-inference.md#quantization).

## Capabilities

| Capability | Notes |
|---|---|
| [Tool calling](../../concepts/tool-calling.md) | Function calls for models that support them |
| [Structured outputs](../../concepts/structured-output.md) | JSON Schema-constrained responses via `format` |
| Thinking | Separate reasoning trace for reasoning models |
| Vision | Image inputs for multimodal models |
| [Embeddings](../../concepts/embeddings.md) | `/api/embed` with models like `nomic-embed-text`, `bge-m3` |
| Web search | Built-in web search for agents (Ollama account) |
| Speech | Text-to-speech on macOS, `/v1/audio/speech` |

## Ollama Cloud

Larger models can run on Ollama's servers with the same API (`https://ollama.com/api/*`, `OLLAMA_API_KEY`), useful when a model does not fit locally. Set `OLLAMA_NO_CLOUD=1` to disable cloud features entirely.

## Strengths and limits

* **Strengths:** easiest setup, huge ecosystem, sensible defaults, good Apple Silicon support.
* **Limits:** built for one user or a small team; for high-throughput serving with batching across many users, use [vLLM](../vllm/index.md) or SGLang.

## Related

[Ollama index](index.md) · [Configuration](configuration.md) · [Local inference](../../concepts/local-inference.md)
