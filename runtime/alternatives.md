---
type: Comparison
title: Runtime Alternatives
description: Comparison of the runtime layer — local model servers (Ollama, llama.cpp, LM Studio, vLLM, Docker Model Runner), AI gateways (LiteLLM, Tailscale Aperture), containers (Docker) and private networking (Tailscale) — with a decision guide.
resource: https://github.com/topics/llm-inference
tags: [runtime, comparison, alternatives, local-inference, gateway]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ollama
    resource: "https://github.com/ollama/ollama"
    title: "Ollama"
    author: "site:github.com"
  - id: llamacpp
    resource: "https://github.com/ggml-org/llama.cpp"
    title: "llama.cpp"
    author: "site:github.com"
  - id: lmstudio
    resource: "https://lmstudio.ai"
    title: "LM Studio"
    author: "site:lmstudio.ai"
  - id: vllm
    resource: "https://github.com/vllm-project/vllm"
    title: "vLLM"
    author: "site:github.com"
  - id: litellm
    resource: "https://github.com/BerriAI/litellm"
    title: "LiteLLM"
    author: "site:github.com"
  - id: docker
    resource: "https://docs.docker.com"
    title: "Docker"
    author: "site:docs.docker.com"
  - id: tailscale
    resource: "https://tailscale.com"
    title: "Tailscale"
    author: "site:tailscale.com"
  - id: searxng
    resource: "https://docs.searxng.org"
    title: "SearXNG"
    author: "site:docs.searxng.org"
---

# Runtime Alternatives

The runtime layer is everything that sits *under* the apps and agents: where models run, how calls are routed, how services are packaged and how you reach them.

## Model servers

| | [Ollama](ollama/index.md) | [llama.cpp](llamacpp/index.md) | [LM Studio](lmstudio/index.md) | [vLLM](vllm/index.md) | Docker [Model Runner](docker/gpu-ai.md#docker-model-runner) |
|---|---|---|---|---|---|
| Best for | Easiest local use | Control, edge, CPU | GUI users, Macs (MLX) | Many concurrent users on GPUs | Docker-native workflows |
| Model format | GGUF (+ import) | GGUF | GGUF, MLX | Hugging Face (safetensors), many quant formats | OCI-packaged GGUF |
| API | Native + OpenAI + Anthropic | OpenAI | OpenAI + Anthropic + native | OpenAI + Anthropic + gRPC | OpenAI |
| Batching / throughput | Basic | Parallel slots | Basic | Continuous batching, PagedAttention | Depends on backend |
| Open source | MIT | MIT | CLI/SDK only | Apache-2.0 | Apache-2.0 |

Others worth knowing: SGLang and TensorRT-LLM (datacentre serving), MLX-LM (Apple), Jan and GPT4All (desktop apps). See [Local inference](../concepts/local-inference.md).

## Gateways

| | [LiteLLM](litellm/index.md) | Tailscale [Aperture](tailscale/ai-integration.md#aperture-alpha) |
|---|---|---|
| What | Self-hosted AI gateway + SDK for 100+ providers | LLM gateway tied to tailnet identity |
| Strengths | Virtual keys, budgets, fallbacks, MCP gateway, broad provider support | Identity without shared keys, hooks for guardrails, usage visibility |
| Maturity | Widely deployed | Alpha |

Alternatives: OpenRouter (hosted), Portkey, Kong AI Gateway, Cloudflare AI Gateway.

## Infrastructure

* [Docker](docker/index.md) — the packaging and runtime for almost every self-hosted tool here; Podman is the daemonless alternative.
* [Tailscale](tailscale/index.md) — private access; alternatives are Headscale (self-hosted control plane), plain WireGuard, ZeroTier, Cloudflare Tunnel (public exposure with auth).
* [SearXNG](searxng/index.md) — private web search for agents; alternatives are paid APIs such as Brave Search, Tavily, Exa and Serper.

## Decision guide

| Situation | Choice |
|---|---|
| First local model on a laptop | [Ollama](ollama/index.md) or [LM Studio](lmstudio/index.md) |
| Squeeze a big model onto small hardware | [llama.cpp](llamacpp/index.md) with partial offload |
| Serve a team or many agents from GPUs | [vLLM](vllm/index.md) |
| Mix local and hosted models behind one endpoint | [LiteLLM](litellm/index.md) |
| Reach it all from your phone, safely | [Tailscale](tailscale/index.md) |

## Related

[Local inference](../concepts/local-inference.md) · [OpenAI-compatible API](../concepts/openai-compatible-api.md) · [Self-hosting](../concepts/self-hosting.md) · [AI landscape](../landscape.md)
