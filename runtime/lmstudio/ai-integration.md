---
type: Playbook
title: LM Studio AI Integration
description: Pointing agents, editors and RAG tools at LM Studio's local server, using its MCP support in chat, and choosing between LM Studio, Ollama and llama.cpp.
resource: https://lmstudio.ai/docs
tags: [lmstudio, integration, agents, editors]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: lmstudio-docs
    resource: "https://lmstudio.ai/docs"
    title: "LM Studio documentation"
    author: "site:lmstudio.ai"
---

# LM Studio — AI Integration

## As a backend

Any tool that accepts an [OpenAI-compatible](../../concepts/openai-compatible-api.md) base URL works with `http://localhost:1234/v1`: [Continue](../../editors/continue/index.md), [Zed](../../editors/zed/index.md), [Aider](../../agents/aider/index.md), [OpenCode](../../agents/opencode/index.md), [AnythingLLM](../../apps/anythingllm/index.md), [Open WebUI](../../apps/openwebui/index.md), [Graphiti](../../memory/graphiti/snippets.md), [LiteLLM](../litellm/index.md). Anthropic-format clients can use its Anthropic-compatible endpoint.

## Tools in chat

Add [MCP](../../concepts/mcp.md) servers (for example [Playwright MCP](../../browsers/playwright-mcp/index.md) or a memory server) so local models can browse or recall. Pick models with good [tool calling](../../concepts/tool-calling.md).

## LM Studio vs Ollama

| | LM Studio | [Ollama](../ollama/index.md) |
|---|---|---|
| Interface | GUI first, CLI second | CLI and API first |
| Mac performance | MLX engine | llama.cpp/GGML (Metal) |
| Open source | CLI/SDKs only | Fully (MIT) |
| Servers | llmster | Native service / Docker |

## Related

[LM Studio index](index.md) · [Local inference](../../concepts/local-inference.md)
