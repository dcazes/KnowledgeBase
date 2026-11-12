---
type: Playbook
title: vLLM Installation
description: Install vLLM with uv or pip, run the official Docker image with GPUs, and know the hardware constraints of recent releases.
resource: https://docs.vllm.ai/en/latest/getting_started/installation/
tags: [vllm, installation, docker, cuda]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: vllm-docs
    resource: "https://docs.vllm.ai"
    title: "vLLM documentation"
    author: "site:docs.vllm.ai"
---

# vLLM — Installation

```bash
uv venv && source .venv/bin/activate
uv pip install vllm            # NVIDIA, CUDA 13.0 wheels by default
```

Since v0.33 release wheels and images are **CUDA 13.0 only**; make sure your driver supports it. AMD (ROCm), Intel, CPU and accelerator backends have their own install paths in the docs.

## Docker

```bash
docker run --gpus all -p 127.0.0.1:8000:8000 --ipc=host \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  -e HF_TOKEN=$HF_TOKEN \
  vllm/vllm-openai:latest --model Qwen/Qwen3-8B
```

`--ipc=host` (or a large `--shm-size`) is needed for multi-GPU communication. Mount the Hugging Face cache so models are not re-downloaded.

## Sizing

Weights plus KV cache must fit in GPU memory. vLLM pre-allocates `--gpu-memory-utilization` (default 0.9) of each GPU; lower it if other processes share the card, or use a quantised checkpoint.

## Related

[vLLM index](index.md) · [Snippets](snippets.md) · [Docker GPU & AI](../docker/gpu-ai.md)
