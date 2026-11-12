---
type: Playbook
title: Docker GPU & AI
description: Using Docker for AI workloads — NVIDIA Container Toolkit for GPUs, Docker Model Runner for local LLMs with an OpenAI-compatible API, the MCP Toolkit and Gateway for tool servers, and Docker Agent for YAML-defined multi-agent systems.
resource: https://docs.docker.com/ai/
tags: [docker, gpu, nvidia, model-runner, mcp, docker-agent, local-inference]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docker-docs
    resource: "https://docs.docker.com"
    title: "Docker documentation"
    author: "site:docs.docker.com"
  - id: dmr
    resource: "https://github.com/docker/model-runner"
    title: "Docker Model Runner"
    author: "site:github.com"
  - id: docker-agent
    resource: "https://github.com/docker/docker-agent"
    title: "Docker Agent"
    author: "site:github.com"
  - id: mcp-gateway
    resource: "https://github.com/docker/mcp-gateway"
    title: "Docker MCP Gateway"
    author: "site:github.com"
  - id: nvidia-ctk
    resource: "https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html"
    title: "NVIDIA Container Toolkit install guide"
    author: "site:docs.nvidia.com"
---

# Docker — GPU & AI

## GPUs in containers

Install the NVIDIA driver on the host and the **NVIDIA Container Toolkit**, then:

```bash
sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker
docker run --rm --gpus all nvidia/cuda:12.6.0-base-ubuntu24.04 nvidia-smi
docker run --gpus '"device=0"' ...           # a specific GPU
```

In Compose, reserve devices under `deploy.resources.reservations.devices` (see [Compose](compose.md)). AMD GPUs use ROCm images with `--device /dev/kfd --device /dev/dri`.

## Docker Model Runner

Runs LLMs locally, managed by Docker, with an [OpenAI-compatible API](../../concepts/openai-compatible-api.md). Models are pulled from registries as OCI artifacts. Backends include [llama.cpp](../llamacpp/index.md) (default, CPU / CUDA / Vulkan / ROCm) and [vLLM](../vllm/index.md).

```bash
docker model pull ai/gemma3
docker model run ai/gemma3 "Explain RAG in one sentence"
docker model ls
```

Desktop exposes the API on port 12434 when TCP access is enabled. Compose's `models:` element wires a model into services. It overlaps with [Ollama](../ollama/index.md) and [LM Studio](../lmstudio/index.md) — see [Local inference](../../concepts/local-inference.md).

## MCP Toolkit and Gateway

A catalog of containerised [MCP](../../concepts/mcp.md) servers and a gateway that exposes the ones you enable to any MCP client through one endpoint, running each server isolated in a container.

```bash
docker mcp catalog pull mcp/docker-mcp-catalog
docker mcp profile create --name dev-tools ...
docker mcp --help
```

Running MCP servers in containers limits what a compromised or malicious tool can reach — see [Agent security](../../concepts/agent-security.md).

## Docker Agent

`docker agent` (formerly cagent) runs agents defined in YAML: model, instructions, MCP toolsets, sub-agents, RAG settings. Agents can be pushed to and pulled from OCI registries.

```yaml
agents:
  root:
    model: openai/gpt-5-mini
    instruction: You are a helpful research assistant.
    toolsets:
      - type: mcp
        ref: docker:duckduckgo
```

```bash
docker agent run agent.yaml
```

Compare with code-first [agent frameworks](../../concepts/agent-frameworks.md) such as [LangGraph](../../agents/langgraph/index.md) and [PydanticAI](../../agents/pydanticAI/index.md).

## Related

[Docker index](index.md) · [Local inference](../../concepts/local-inference.md) · [MCP](../../concepts/mcp.md)
