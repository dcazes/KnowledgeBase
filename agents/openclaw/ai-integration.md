---
type: Playbook
title: OpenClaw AI Integration
description: Extending OpenClaw — memory plugins (Honcho, MemOS, Cognee, Supermemory, Hindsight), browser plugins (Camofox), local models via Ollama, and skills shared with Hermes and Letta.
resource: https://docs.openclaw.ai/plugins
tags: [openclaw, integration, plugins, memory, browser]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openclaw-docs
    resource: "https://docs.openclaw.ai"
    title: "OpenClaw documentation"
    author: "site:docs.openclaw.ai"
---

# OpenClaw — AI Integration

| Need | Plugin / route |
|---|---|
| Long-term memory | [Honcho](../../memory/honcho/ai-integration.md), [MemOS](../../memory/memos/ai-integration.md), [Cognee](../../memory/cognee/ai-integration.md), [Supermemory](../../memory/supermemory/ai-integration.md), [Hindsight](../../memory/hindsight/ai-integration.md) |
| Stealth browsing | [Camofox](../../browsers/camofox/ai-integration.md) plugin |
| Local models | [Ollama](../../runtime/ollama/ai-integration.md) (`ollama launch openclaw`), [LM Studio](../../runtime/lmstudio/index.md), [vLLM](../../runtime/vllm/index.md) |
| Tools from elsewhere | [MCP](../../concepts/mcp.md) servers and ClawHub skills |

Skills from ClawHub install into [Letta](../../memory/letta/snippets.md) and [Hermes](../hermes/skills-plugins.md) too, and Hermes can import an OpenClaw setup wholesale.

## Related

[OpenClaw index](index.md) · [Agents alternatives](../alternatives.md)
