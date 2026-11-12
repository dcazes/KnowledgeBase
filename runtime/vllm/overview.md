---
type: Concept
title: vLLM Overview
description: How vLLM achieves high throughput — PagedAttention, continuous batching, chunked prefill, prefix caching, speculative decoding, tensor/pipeline/expert parallelism, disaggregated prefill/decode, quantisation formats and 200+ model architectures.
resource: https://docs.vllm.ai
tags: [vllm, overview, pagedattention, batching, quantization]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: vllm-github
    resource: "https://github.com/vllm-project/vllm"
    title: "vllm-project/vllm on GitHub"
    author: "site:github.com"
  - id: pagedattention
    resource: "https://arxiv.org/abs/2309.06180"
    title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
    author: "Kwon et al., arXiv 2309.06180"
---

# vLLM — Overview

## Why it is fast

| Technique | Effect |
|---|---|
| **PagedAttention** | KV cache stored in fixed-size blocks like OS memory pages — little fragmentation, more concurrent sequences per GPU (Kwon et al., 2023) |
| Continuous batching | New requests join the running batch at every step instead of waiting for the batch to finish |
| Chunked prefill | Long prompts are split so they do not stall ongoing decoding |
| Prefix caching | Shared prompt prefixes (system prompts, RAG context) are computed once |
| Speculative decoding | n-gram, suffix, EAGLE and DFlash drafters propose tokens the main model verifies |
| CUDA/HIP graphs, torch.compile | Lower per-step overhead |

## Scaling out

Tensor, pipeline, data, expert and context parallelism split large models across GPUs and nodes; **disaggregated** prefill, decode and encode let each phase run on separately sized hardware.

## Quantisation

FP8, MXFP8/MXFP4, NVFP4, INT8, INT4, GPTQ, AWQ, GGUF, compressed-tensors and more — see [Local inference](../../concepts/local-inference.md#quantization).

## Features for agents

* [Structured outputs](../../concepts/structured-output.md) via xgrammar or guidance
* [Tool calling](../../concepts/tool-calling.md) and reasoning parsers per model family
* Multi-LoRA serving (many fine-tunes on one base model)
* Embedding, reranking and classification models alongside chat models — useful for [RAG](../../concepts/rag.md)

## Models

200+ Hugging Face architectures: dense decoders (Llama, Qwen, Gemma), MoE (DeepSeek-V3, Qwen-MoE, gpt-oss), hybrid state-space models, multimodal models, embedding and retrieval models such as ColBERT.

## Related

[vLLM index](index.md) · [Snippets](snippets.md) · [Local inference](../../concepts/local-inference.md)
