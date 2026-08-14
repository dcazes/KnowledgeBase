---
type: Reference
title: Docker — GPU & AI in Containers
description: Run GPU-accelerated workloads (Frigate detection, LLM inference) in containers on the GTX 1060 via the NVIDIA Container Toolkit.
resource: https://docs.docker.com/engine/containers/resource_constraints/#gpu
tags: [docker, gpu, nvidia, ai, frigate, inference]
generated: { by: "human:daniel", at: "2026-07-08T22:35:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-08T22:35:00Z" } ]
status: stable
stale_after: 2027-01-04
sources:
  - id: docker-gpu-access
    resource: "https://docs.docker.com/engine/containers/resource_constraints/#gpu"
    title: "Docker GPU access"
    author: "site:docs.docker.com"
  - id: nvidia-container-toolkit
    resource: "https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/"
    title: "NVIDIA Container Toolkit"
    author: "site:docs.nvidia.com"
  - id: frigate-object-detectors-onnx
    resource: "https://docs.frigate.video/configuration/object_detectors"
    title: "Frigate object detectors (ONNX)"
    author: "site:docs.frigate.video"
  - id: local-frigate-compose-programs-frigate-docker-compose-yml
    resource: "/../../programs/frigate/docker-compose.yml"
    title: "Local Frigate compose - programs/frigate/docker-compose.yml"
  - id: detected-gpu-nvidia-smi-on-host
    resource: "/../../programs/"
    title: "Detected GPU - nvidia-smi on host"
---

# Docker — Overview

This machine has an **NVIDIA GeForce GTX 1060 6GB** (`nvidia-smi` reports 6144 MiB). To let a container use the GPU you need the **NVIDIA Container Toolkit** installed on the host and a device reservation in the container config. Without it, containers only see the CPU.

Two ways to grant GPU access:

1. **Compose `deploy.resources.reservations.devices`** (modern, used by Frigate here).
2. **`--gpus` flag** on `docker run`.

# How it works

```
container  ──(NVIDIA Container Toolkit / libnvidia)──>  host GPU driver  ──>  GTX 1060
```

The toolkit injects the NVIDIA driver libraries and a `/dev/nvidia*` device into the container at runtime. The host must have the proprietary NVIDIA driver + `nvidia-container-toolkit` installed; the container image just needs the CUDA/cuDNN runtime it was built against (e.g. Frigate's `:stable`).

# Real example — Frigate (from programs/frigate/docker-compose.yml)

Frigate reserves the single GPU for object detection via the ONNX detector (CUDA Graphs):

```yaml
services:
  frigate:
    image: ghcr.io/blakeblackshear/frigate:stable
    privileged: true
    shm_size: "256mb"
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

# Ad-hoc GPU container (docker run)

```bash
# List available GPUs
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi

# Restrict to a specific GPU by index
docker run --rm --gpus '"device=0"' nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi
```

# Running LLM inference in a container (your stack)

For local LLM serving you'd reserve the GPU similarly, e.g. with Ollama or vLLM:

```yaml
services:
  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

> **Your KB plan deliberately avoids heavy local models** (6 GB VRAM is tight). Inference is routed to cloud endpoints (OpenRouter / NVIDIA NIM) via a failover proxy on `:4000`. Use the GPU reservation primarily for **Frigate** detection and lighter local experiments.

# Verify GPU access inside a container

```bash
docker exec -it frigate nvidia-smi     # should show the GTX 1060
```

# Gotchas

| Problem | Cause / Fix |
|---------|-------------|
| `could not select device driver` | NVIDIA Container Toolkit not installed on host. |
| Container can't see GPU | Missing `deploy.resources.reservations.devices` / `--gpus` flag. |
| Out of memory on GPU | 6 GB is small — reduce model size or detection resolution; bump `shm_size`. |
| `privileged: true` needed | Frigate needs raw device access; only set for trusted images. |
