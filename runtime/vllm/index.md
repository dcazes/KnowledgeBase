---
type: Software
title: vLLM
description: High-throughput LLM inference and serving engine from UC Berkeley's Sky Lab — PagedAttention, continuous batching, prefix caching, speculative decoding, broad quantisation and hardware support, and an OpenAI- and Anthropic-compatible server.
resource: https://github.com/vllm-project/vllm
tags: [vllm, inference, serving, pagedattention, gpu, openai-compatible, python]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: vllm-github
    resource: "https://github.com/vllm-project/vllm"
    title: "vllm-project/vllm on GitHub"
    author: "site:github.com"
  - id: vllm-docs
    resource: "https://docs.vllm.ai"
    title: "vLLM documentation"
    author: "site:docs.vllm.ai"
  - id: pagedattention
    resource: "https://arxiv.org/abs/2309.06180"
    title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
    author: "Kwon et al., arXiv 2309.06180"
---

# vLLM

**vLLM** is the standard open-source engine for *serving* LLMs to many concurrent users. Where [Ollama](../ollama/index.md) and [llama.cpp](../llamacpp/index.md) optimise for one person on consumer hardware, vLLM optimises throughput on GPUs: PagedAttention manages the KV cache like virtual memory, and continuous batching keeps the GPU busy across requests.

| | |
|---|---|
| Category | [Local inference](../../concepts/local-inference.md) · serving |
| License | Apache-2.0 |
| Language | Python + CUDA/C++ kernels |
| Latest release | v0.33.0 (2026-11-02; PyTorch 2.14, CUDA 13.0 only) |
| Hardware | NVIDIA, AMD, Intel GPUs, x86/ARM/PowerPC CPUs; plugins for TPU, Gaudi, Ascend and others |
| Server | `vllm serve` — [OpenAI-compatible](../../concepts/openai-compatible-api.md) + Anthropic Messages API + gRPC |

## Contents

* [Overview](overview.md) — PagedAttention, batching, parallelism, quantisation, features
* [Installation](installation.md) — pip/uv, Docker, hardware notes
* [Snippets](snippets.md) — serve, query, offline inference, structured output, tool calling
* [AI Integration](ai-integration.md) — as a backend for agents, RAG and gateways

## Related

* Concepts: [Local inference](../../concepts/local-inference.md) · [Structured output](../../concepts/structured-output.md) · [Tool calling](../../concepts/tool-calling.md)
* Peers: [Ollama](../ollama/index.md), [llama.cpp](../llamacpp/index.md), [LM Studio](../lmstudio/index.md); front with [LiteLLM](../litellm/index.md)
* Comparison: [Runtime alternatives](../alternatives.md)
