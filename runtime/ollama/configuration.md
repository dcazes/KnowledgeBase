---
type: HowTo
title: Ollama Configuration
description: Configure Ollama — OLLAMA_HOST / OLLAMA_MODELS / keep_alive, model defaults, concurrency, embeddings; OpenAI-compatible settings.
resource: https://docs.ollama.com
tags: [ollama, configuration, env, models]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: ollama-docs-configuration
    resource: "https://docs.ollama.com"
    title: "Ollama docs — configuration"
    author: "site:docs.ollama.com"
  - id: ollama-github
    resource: "https://github.com/ollama/ollama"
    title: "Ollama GitHub"
    author: "site:github.com"
---

# Configuration

## Key env vars

| Var | Default | Notes |
|---|---|---|
| `OLLAMA_HOST` | `127.0.0.1:11434` | bind address; `0.0.0.0` to expose to containers |
| `OLLAMA_MODELS` | `~/.ollama/models` | model storage |
| `OLLAMA_KEEP_ALIVE` | `5m` | model unload idle time; `0` = keep loaded |
| `OLLAMA_NUM_PARALLEL` | auto | parallel requests per model |
| `OLLAMA_MAX_LOADED_MODELS` | 1 (GPU) / 3 (CPU) | concurrent loaded models |
| `OLLAMA_FLASH_ATTENTION` | off | enable FA for supported GPUs |

Set via `environment:` in compose or `export` before `ollama serve`.

## Model-level defaults

`ollama create` with a Modelfile can bake in temperature, context, system prompt:

```
FROM llama3.1
PARAMETER temperature 0.7
PARAMETER num_ctx 8192
SYSTEM "You are a concise assistant."
```

## API parameters

Passed per request: `options: {"temperature": 0.2, "num_ctx": 8192, "seed": 42}`, plus `keep_alive` to override unload.

## Embeddings

`ollama pull nomic-embed-text` then `POST /api/embed {"model": "nomic-embed-text", "input": "…"}` — used by [Mem0](../../memory/mem0/index.md)/[LightRAG](../../memory/lightrag/index.md) as local embedder.
