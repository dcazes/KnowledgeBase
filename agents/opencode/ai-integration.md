---
type: Playbook
title: OpenCode AI Integration
description: Pairing OpenCode with the rest of the stack — local models through Ollama or LM Studio, gateways like LiteLLM and Tailscale Aperture, memory plugins, MCP servers for graphs, browsers and search, and skills.
resource: https://opencode.ai/docs
tags: [opencode, integration, local-models, memory, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: opencode-docs
    resource: "https://opencode.ai/docs"
    title: "OpenCode documentation"
    author: "site:opencode.ai"
---

# OpenCode — AI Integration

| Need | Integration |
|---|---|
| Local models | [Ollama](../../runtime/ollama/ai-integration.md) (`ollama launch opencode`), [LM Studio](../../runtime/lmstudio/ai-integration.md), [vLLM](../../runtime/vllm/index.md) |
| One endpoint for all models | [LiteLLM](../../runtime/litellm/ai-integration.md); Tailscale [Aperture](../../runtime/tailscale/ai-integration.md) launcher |
| Memory across sessions | [Honcho](../../memory/honcho/ai-integration.md), [Supermemory](../../memory/supermemory/ai-integration.md), [Hindsight](../../memory/hindsight/ai-integration.md) plugins |
| Codebase understanding | [Graphify](../../memory/graphify/ai-integration.md) skill or MCP |
| Browser and web | [Playwright MCP](../../browsers/playwright-mcp/index.md), [Firecrawl](../../browsers/firecrawl/ai-integration.md) |
| Observability | Route through LiteLLM to [Langfuse](../../observability/langfuse/index.md) |

Local models need strong [tool calling](../../concepts/tool-calling.md) and long context for agentic coding; coder-tuned open models in the 30B+ range work best.

## Related

[OpenCode index](index.md) · [Coding agents](../../concepts/coding-agents.md)
