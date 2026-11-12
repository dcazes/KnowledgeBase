---
type: Concept
title: Local Inference
description: Running LLMs on your own hardware — memory sizing, quantization formats (GGUF k-quants, AWQ, GPTQ, FP8, MXFP4), CPU/GPU offload, context length and KV cache, choosing between Ollama, llama.cpp, LM Studio, vLLM and Docker Model Runner, and open-weight model families.
resource: https://github.com/ggml-org/llama.cpp
tags: [concept, local-inference, quantization, gguf, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: llamacpp
    resource: "https://github.com/ggml-org/llama.cpp"
    title: "llama.cpp"
    author: "site:github.com"
  - id: vllm-docs
    resource: "https://docs.vllm.ai"
    title: "vLLM documentation"
    author: "site:docs.vllm.ai"
---

# Local Inference

Running models on your own machine gives privacy, offline operation, no per-token cost and full control — at the price of hardware limits. Open-weight models in 2026 (Qwen 3.x, Gemma 4, Llama, gpt-oss, DeepSeek, Mistral, GLM, Kimi, Liquid LFM) make local models genuinely useful for chat, RAG, extraction and, at the larger end, coding agents.

## Will it fit?

Rough memory need ≈ parameters × bytes per weight + KV cache. An 8B model at 4-bit ≈ 5 GB; a 32B model at 4-bit ≈ 20 GB; long contexts add gigabytes of KV cache (quantise it — `OLLAMA_KV_CACHE_TYPE`, vLLM FP8 KV). Mixture-of-experts models need memory for all experts but compute only the active ones.

## Quantization

| Format | Used by | Notes |
|---|---|---|
| GGUF k-/i-quants (Q4_K_M, Q5_K_M, Q8_0, IQ3…) | [llama.cpp](../runtime/llamacpp/overview.md), [Ollama](../runtime/ollama/index.md), [LM Studio](../runtime/lmstudio/index.md) | Q4_K_M is the usual sweet spot |
| AWQ, GPTQ, INT8/INT4 | [vLLM](../runtime/vllm/overview.md) | GPU serving |
| FP8, MXFP4/NVFP4 | vLLM, newer llama.cpp | Hardware-accelerated on recent GPUs |
| MLX | LM Studio on Apple Silicon | Apple-native |

Lower bits lose quality; small models suffer more than large ones.

## Choosing a runtime

| Situation | Runtime |
|---|---|
| Easiest start | [Ollama](../runtime/ollama/index.md) or [LM Studio](../runtime/lmstudio/index.md) |
| Max control, CPU/edge, partial offload | [llama.cpp](../runtime/llamacpp/index.md) |
| Many users, GPUs | [vLLM](../runtime/vllm/index.md) |
| Docker-native | Docker [Model Runner](../runtime/docker/gpu-ai.md#docker-model-runner) |
| Mix local and hosted | [LiteLLM](../runtime/litellm/index.md) in front |

## Beyond chat

Local embeddings and rerankers ([Embeddings](embeddings.md)), speech, and vision — e.g. [Frigate](../tools/frigate/index.md)'s detectors and vision-language descriptions.

## Related

[OpenAI-compatible API](openai-compatible-api.md) · [Self-hosting](self-hosting.md) · [Runtime alternatives](../runtime/alternatives.md) · [Concepts index](index.md)
