---
type: Software
title: llama.cpp
description: Dependency-free C/C++ LLM inference engine built on ggml — the GGUF format, 1.5- to 8-bit quantisation, CPU+GPU hybrid inference across CUDA, Metal, Vulkan, ROCm, SYCL and more, and an OpenAI-compatible server. The engine under Ollama, LM Studio and many others.
resource: https://github.com/ggml-org/llama.cpp
tags: [llamacpp, gguf, quantization, local-inference, cpp, openai-compatible]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: llamacpp-github
    resource: "https://github.com/ggml-org/llama.cpp"
    title: "ggml-org/llama.cpp on GitHub"
    author: "site:github.com"
  - id: llamacpp-server
    resource: "https://github.com/ggml-org/llama.cpp/tree/master/tools/server"
    title: "llama.cpp server README"
    author: "site:github.com"
  - id: ggml
    resource: "https://github.com/ggml-org/ggml"
    title: "ggml tensor library"
    author: "site:github.com"
---

# llama.cpp

**llama.cpp** is the project that made running LLMs on laptops practical. It is a plain C/C++ implementation with no dependencies, built on the **ggml** tensor library, and it defined the **GGUF** model format that most local tools now use. [Ollama](../ollama/index.md), [LM Studio](../lmstudio/index.md), Docker [Model Runner](../docker/gpu-ai.md#docker-model-runner) and many desktop apps embed it.

| | |
|---|---|
| Category | [Local inference](../../concepts/local-inference.md) |
| License | MIT |
| Language | C/C++ |
| Releases | Continuous build tags (`bNNNNN`, several per day); ggml v0.29 as of Nov 2026 |
| Backends | CPU (AVX/AMX/NEON/RVV), CUDA, HIP (AMD), Metal, Vulkan, SYCL, MUSA, CANN, OpenCL, WebGPU, RPC and more |

## Contents

* [Overview](overview.md) — GGUF, quantisation types, hybrid offload, what is new
* [Installation](installation.md) — installer, binaries, Docker, building from source
* [Snippets](snippets.md) — `llama cli` / `llama serve`, server flags, API calls, grammars
* [AI Integration](ai-integration.md) — using `llama-server` behind agents and UIs

## Related

* Concepts: [Local inference](../../concepts/local-inference.md) · [Structured output](../../concepts/structured-output.md) · [OpenAI-compatible API](../../concepts/openai-compatible-api.md)
* Built on it: [Ollama](../ollama/index.md), [LM Studio](../lmstudio/index.md); alternative for GPU servers: [vLLM](../vllm/index.md)
* Comparison: [Runtime alternatives](../alternatives.md)
