---
type: Concept
title: LM Studio Overview
description: LM Studio's components — model discovery and download, llama.cpp and MLX runtimes, the chat UI with documents and MCP tools, the local API server, headless llmster, and LM Link for using models across devices.
resource: https://lmstudio.ai/docs
tags: [lmstudio, overview, mlx, mcp, headless]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: lmstudio-docs
    resource: "https://lmstudio.ai/docs"
    title: "LM Studio documentation"
    author: "site:lmstudio.ai"
  - id: lms-github
    resource: "https://github.com/lmstudio-ai/lms"
    title: "lmstudio-ai/lms (CLI)"
    author: "site:github.com"
---

# LM Studio — Overview

## Components

| Part | What it does |
|---|---|
| Discover | Search Hugging Face, see which quantisations fit your RAM/VRAM, download |
| Runtimes | [llama.cpp](../llamacpp/index.md) for GGUF everywhere; MLX for Apple Silicon (often faster on Macs) |
| Chat | Conversations, attached documents (simple local [RAG](../../concepts/rag.md)), system prompts, presets |
| MCP | The chat can use [MCP](../../concepts/mcp.md) servers configured in an `mcp.json` |
| Developer server | Local API on port 1234: [OpenAI-compatible](../../concepts/openai-compatible-api.md), Anthropic-compatible and native REST endpoints, with JIT model loading |
| `lms` CLI | Load/unload models, start the server, stream logs, scaffold SDK projects |
| llmster | Headless daemon for servers and CI — LM Studio without the GUI |
| LM Link | Use models on one of your devices from another; agentic use must be explicitly enabled |

## Strengths and limits

* **Strengths:** best GUI experience, clear hardware-fit guidance, MLX on Macs, structured output and tool calling exposed in the server.
* **Limits:** the app is closed source; single-user oriented — for multi-user serving use [vLLM](../vllm/index.md).

## Related

[LM Studio index](index.md) · [Snippets](snippets.md)
