---
type: Reference
title: Ollama Configuration
description: Ollama server environment variables (host, origins, keep-alive, context length, parallelism, KV-cache type, flash attention, model directory, cloud opt-out) and Modelfile customisation.
resource: https://docs.ollama.com/faq
tags: [ollama, configuration, env, modelfile, context-length]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ollama-docs
    resource: "https://docs.ollama.com"
    title: "Ollama documentation"
    author: "site:docs.ollama.com"
  - id: ollama-modelfile
    resource: "https://docs.ollama.com/modelfile"
    title: "Ollama Modelfile reference"
    author: "site:docs.ollama.com"
---

# Ollama — Configuration

## Server environment variables

| Variable | Purpose |
|---|---|
| `OLLAMA_HOST` | Bind address, default `127.0.0.1:11434`; `0.0.0.0` exposes it to the network |
| `OLLAMA_ORIGINS` | Extra allowed CORS origins for browser apps |
| `OLLAMA_MODELS` | Model storage directory |
| `OLLAMA_KEEP_ALIVE` | How long models stay loaded (`5m` default, `-1` forever) |
| `OLLAMA_CONTEXT_LENGTH` | Default context window for all models |
| `OLLAMA_NUM_PARALLEL` | Parallel requests per model |
| `OLLAMA_MAX_LOADED_MODELS` | Models kept in memory at once |
| `OLLAMA_MAX_QUEUE` | Queued requests before rejecting |
| `OLLAMA_FLASH_ATTENTION` | Enable flash attention (less memory, faster) |
| `OLLAMA_KV_CACHE_TYPE` | `f16`, `q8_0` or `q4_0` — quantised KV cache saves memory for long contexts |
| `OLLAMA_NO_CLOUD` | Disable cloud models and features |

On Linux set them in the systemd unit (`systemctl edit ollama`), then restart.

## Context length

Many agent tools (RAG, coding agents) need far more than a small default context. Raise `OLLAMA_CONTEXT_LENGTH` or set `num_ctx` per request — memory use grows with context; a quantised KV cache helps.

## Modelfile

```
FROM qwen3:8b
PARAMETER num_ctx 32768
PARAMETER temperature 0.2
SYSTEM You are a concise senior engineer.
```

```bash
ollama create my-coder -f Modelfile
```

## Security

Ollama has **no authentication**. Never expose `0.0.0.0:11434` to the internet; use a reverse proxy with auth or a private network like [Tailscale](../tailscale/index.md).

## Related

[Ollama index](index.md) · [Snippets](snippets.md) · [Self-hosting](../../concepts/self-hosting.md)
