---
type: Software
title: LM Studio
description: Desktop app for discovering, downloading and running local LLMs with llama.cpp and Apple MLX engines — chat UI, OpenAI- and Anthropic-compatible local server, lms CLI, Python and TypeScript SDKs, MCP support, and headless llmster for servers.
resource: https://lmstudio.ai
tags: [lmstudio, local-inference, desktop, mlx, gguf, openai-compatible]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: lmstudio-site
    resource: "https://lmstudio.ai"
    title: "LM Studio — official site"
    author: "site:lmstudio.ai"
  - id: lmstudio-docs
    resource: "https://lmstudio.ai/docs"
    title: "LM Studio documentation"
    author: "site:lmstudio.ai"
  - id: lms-github
    resource: "https://github.com/lmstudio-ai/lms"
    title: "lmstudio-ai/lms (CLI)"
    author: "site:github.com"
  - id: mlx-engine
    resource: "https://github.com/lmstudio-ai/mlx-engine"
    title: "LM Studio MLX engine"
    author: "site:github.com"
---

# LM Studio

**LM Studio** is a polished desktop application for local models: browse Hugging Face, download a GGUF or MLX build that fits your hardware, chat with it, and expose it to other apps through a local server. It is the most approachable on-ramp to [local inference](../../concepts/local-inference.md) for people who prefer a GUI to a terminal.

| | |
|---|---|
| Category | [Local inference](../../concepts/local-inference.md) |
| Licence | App: free, proprietary; `lms` CLI, SDKs and MLX engine: MIT |
| Latest | App 0.4.26 · Python SDK `lmstudio` 1.5.0 · JS SDK `@lmstudio/sdk` 2.1.0 |
| Engines | [llama.cpp](../llamacpp/index.md) (GGUF, all platforms), MLX (Apple Silicon) |
| Server | `localhost:1234` — OpenAI-compatible and Anthropic-compatible endpoints plus a native REST API |

## Contents

* [Overview](overview.md) — app, engines, server, MCP, headless llmster, LM Link
* [Installation](installation.md) — desktop app, `lms` CLI, llmster
* [Snippets](snippets.md) — CLI, API calls, SDKs
* [AI Integration](ai-integration.md) — using LM Studio as a backend for agents and tools

## Related

* Concepts: [Local inference](../../concepts/local-inference.md) · [MCP](../../concepts/mcp.md) · [OpenAI-compatible API](../../concepts/openai-compatible-api.md)
* Peers: [Ollama](../ollama/index.md), [llama.cpp](../llamacpp/index.md), [vLLM](../vllm/index.md)
* Comparison: [Runtime alternatives](../alternatives.md)
