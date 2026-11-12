---
type: Playbook
title: AnythingLLM AI Integration
description: AnythingLLM in a wider stack — local and gateway model providers, model routing, web search via SearXNG, MCP tools, shared vector databases, memory, and when to choose it over Open WebUI or SurfSense.
resource: https://docs.anythingllm.com
tags: [anythingllm, integration, models, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: anythingllm-docs
    resource: "https://docs.anythingllm.com"
    title: "AnythingLLM documentation"
    author: "site:docs.anythingllm.com"
---

# AnythingLLM — AI Integration

| Layer | Options |
|---|---|
| Models | Built-in engine, [Ollama](../../runtime/ollama/index.md), [LM Studio](../../runtime/lmstudio/index.md), [llama.cpp](../../runtime/llamacpp/index.md) models, generic OpenAI for [LiteLLM](../../runtime/litellm/index.md) or [vLLM](../../runtime/vllm/index.md), hosted providers |
| Web | [SearXNG](../../runtime/searxng/ai-integration.md) or search APIs |
| Tools | [MCP](../../concepts/mcp.md) servers |
| Vectors | Shared [Qdrant](../../databases/qdrant/index.md) or [pgvector](../../databases/pgvector/index.md) with other apps |

## Choosing

* **AnythingLLM** — least setup, desktop-friendly, workspaces, agents and embeddable widgets.
* [Open WebUI](../openwebui/index.md) — best multi-model chat for teams and extensibility.
* [SurfSense](../../browsers/surfsense/index.md) — editing and transforming your own documents privately.

## Related

[AnythingLLM index](index.md) · [Apps alternatives](../alternatives.md)
