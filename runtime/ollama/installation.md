---
type: Playbook
title: Ollama Installation
description: Install Ollama on macOS, Windows or Linux with the official scripts or installers, run it in Docker with NVIDIA or AMD GPUs, and verify the server.
resource: https://docs.ollama.com/quickstart
tags: [ollama, installation, docker, gpu, linux]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ollama-github
    resource: "https://github.com/ollama/ollama"
    title: "ollama/ollama on GitHub"
    author: "site:github.com"
  - id: ollama-docker
    resource: "https://docs.ollama.com/docker"
    title: "Ollama Docker docs"
    author: "site:docs.ollama.com"
---

# Ollama — Installation

```bash
curl -fsSL https://ollama.com/install.sh | sh        # macOS and Linux
irm https://ollama.com/install.ps1 | iex             # Windows PowerShell
```

Installers (`Ollama.dmg`, `OllamaSetup.exe`) are also available. On Linux the script installs a `systemd` service.

## Docker

```bash
docker run -d --name ollama -p 127.0.0.1:11434:11434 -v ollama:/root/.ollama ollama/ollama            # CPU
docker run -d --gpus=all --name ollama -p 127.0.0.1:11434:11434 -v ollama:/root/.ollama ollama/ollama # NVIDIA
docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 ollama/ollama:rocm  # AMD
docker exec -it ollama ollama run gemma4
```

NVIDIA needs the Container Toolkit — see [Docker GPU & AI](../docker/gpu-ai.md).

## Verify

```bash
ollama --version
ollama run gemma4 "hello"
curl http://localhost:11434/api/tags
```

## Related

[Ollama index](index.md) · [Configuration](configuration.md) · [Docker](../docker/index.md)
