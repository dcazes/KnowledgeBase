---
type: Playbook
title: SurfSense AI Integration
description: Choosing models for SurfSense (local or any OpenAI-compatible API), extending it with MCP plugins, and where it fits next to chat UIs, memory layers and document parsers.
resource: https://github.com/MODSetter/SurfSense
tags: [surfsense, integration, local-models, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: surfsense-github
    resource: "https://github.com/MODSetter/SurfSense"
    title: "MODSetter/SurfSense on GitHub"
    author: "site:github.com"
---

# SurfSense — AI Integration

## Models

SurfSense works with any [OpenAI-compatible](../../concepts/openai-compatible-api.md) API or a local model — [Ollama](../../runtime/ollama/index.md), [LM Studio](../../runtime/lmstudio/index.md), [llama.cpp](../../runtime/llamacpp/index.md), [vLLM](../../runtime/vllm/index.md), or a [LiteLLM](../../runtime/litellm/index.md) gateway. With a local model nothing leaves your machine; editing Office files and long documents benefits from strong [tool calling](../../concepts/tool-calling.md) and a large context.

## Plugins

Add [MCP](../../concepts/mcp.md) servers to extend research sources — for example a [Playwright MCP](../playwright-mcp/index.md) browser or a Notion connector. Treat third-party plugins as code you trust with your documents ([Agent security](../../concepts/agent-security.md)).

## Where it fits

| Need | Tool |
|---|---|
| Private research and editing over your own files | **SurfSense** |
| Team chat UI over many models | [Open WebUI](../../apps/openwebui/index.md) |
| Workspaces with RAG and agents for a team | [AnythingLLM](../../apps/anythingllm/index.md) |
| A memory API for your own app | [Supermemory](../../memory/supermemory/index.md), [Mem0](../../memory/mem0/index.md) |

## Related

[SurfSense index](index.md) · [RAG](../../concepts/rag.md)
