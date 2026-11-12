---
type: Playbook
title: llama.cpp Installation
description: Install llama.cpp with the official installer, prebuilt release binaries, package managers or Docker images, or build from source with CUDA, Metal or Vulkan.
resource: https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md
tags: [llamacpp, installation, build, docker, cuda]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: llamacpp-github
    resource: "https://github.com/ggml-org/llama.cpp"
    title: "ggml-org/llama.cpp on GitHub"
    author: "site:github.com"
  - id: llamacpp-build
    resource: "https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md"
    title: "llama.cpp build guide"
    author: "site:github.com"
---

# llama.cpp — Installation

## Installer or binaries

```bash
curl -LsSf https://llama.app/install.sh | sh        # macOS / Linux
irm https://llama.app/install.ps1 | iex             # Windows
brew install llama.cpp                              # Homebrew
```

Prebuilt archives for each platform and backend are attached to every GitHub release.

## Docker

```bash
docker run --gpus all -p 127.0.0.1:8080:8080 -v ~/models:/models \
  ghcr.io/ggml-org/llama.cpp:server-cuda -m /models/model.gguf --host 0.0.0.0 -c 16384 -ngl 99
```

Variants include `server`, `server-cuda`, `server-rocm`, `server-vulkan`.

## Build from source

```bash
git clone https://github.com/ggml-org/llama.cpp && cd llama.cpp
cmake -B build -DGGML_CUDA=ON        # or -DGGML_VULKAN=ON, -DGGML_HIP=ON; Metal is on by default on macOS
cmake --build build --config Release -j
./build/bin/llama-server --help
```

## Related

[llama.cpp index](index.md) · [Snippets](snippets.md) · [Docker GPU & AI](../docker/gpu-ai.md)
