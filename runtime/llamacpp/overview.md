---
type: Concept
title: llama.cpp Overview
description: Core llama.cpp ideas — the GGUF single-file format, k-quants and i-quants from 1.5 to 8 bits plus FP8, partial GPU offload for models larger than VRAM, broad hardware backends, multimodal and audio support, and the unified llama CLI.
resource: https://github.com/ggml-org/llama.cpp
tags: [llamacpp, overview, gguf, quantization, offload]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: llamacpp-github
    resource: "https://github.com/ggml-org/llama.cpp"
    title: "ggml-org/llama.cpp on GitHub"
    author: "site:github.com"
  - id: ggml
    resource: "https://github.com/ggml-org/ggml"
    title: "ggml tensor library"
    author: "site:github.com"
---

# llama.cpp — Overview

## GGUF

A single file containing weights, tokenizer, chat template and metadata. Hugging Face hosts thousands of GGUF conversions (often under `ggml-org/`, `unsloth/`, `bartowski/`), and `-hf <repo>` downloads them directly.

## Quantisation

Weights can be stored at 1.5, 2, 3, 4, 5, 6 or 8 bits (k-quants such as `Q4_K_M`, importance-matrix i-quants such as `IQ3_XXS`), and since late 2026 OCP FP8 E4M3. Rough guide:

| Quant | Quality | Use |
|---|---|---|
| Q8_0 | Near-lossless | When memory allows |
| Q5_K_M / Q6_K | Very good | Quality-sensitive tasks |
| Q4_K_M | Good default | Most local use |
| IQ3 / Q2 | Noticeable loss | Very large models on small hardware |

See [Local inference](../../concepts/local-inference.md#quantization).

## Hybrid inference

`--n-gpu-layers` offloads as many layers as fit in VRAM and runs the rest on CPU, so models larger than your GPU still run — slower, but they run. MoE models can keep experts on CPU while attention runs on GPU.

## Beyond text

Vision-language models via multimodal projectors, speech-to-text and text-to-speech models, embeddings and rerankers.

## Recent direction (2026)

* A unified `llama` command (`llama cli`, `llama serve`) and a one-line installer (llama.app), alongside the classic `llama-cli` / `llama-server` binaries.
* Multi-node tensor parallelism via NCCL in ggml, unified KV cache improvements, and day-one support for new architectures.

## Related

[llama.cpp index](index.md) · [Snippets](snippets.md) · [Ollama overview](../ollama/overview.md)
