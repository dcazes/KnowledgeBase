---
type: Playbook
title: Hermes Agent AI Integration
description: Connecting Hermes to the rest of an AI stack — MCP servers, external memory providers, local models via Ollama or LiteLLM, and launchers such as Tailscale Aperture.
resource: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
tags: [hermes, integration, mcp, memory, local-models]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hermes-docs
    resource: "https://hermes-agent.nousresearch.com/docs/"
    title: "Hermes Agent documentation"
    author: "site:hermes-agent.nousresearch.com"
---

# Hermes Agent — AI Integration

| Integration | How |
|---|---|
| [MCP](../../concepts/mcp.md) servers | Add any server — [Graphiti](../../memory/graphiti/mcp-server.md), [Graphify](../../memory/graphify/mcp-server.md), [Firecrawl](../../browsers/firecrawl/ai-integration.md), [Playwright MCP](../../browsers/playwright-mcp/index.md) |
| Memory | Built in, or [Honcho](../../memory/honcho/ai-integration.md), [Supermemory](../../memory/supermemory/ai-integration.md), [MemOS](../../memory/memos/ai-integration.md), [Hindsight](../../memory/hindsight/ai-integration.md) |
| Local models | [Ollama](../../runtime/ollama/index.md), [vLLM](../../runtime/vllm/index.md), [LM Studio](../../runtime/lmstudio/index.md) via OpenAI-compatible endpoints |
| Gateways | [LiteLLM](../../runtime/litellm/index.md); Tailscale [Aperture](../../runtime/tailscale/ai-integration.md) launches Hermes preconfigured |
| Browser tasks | [browser-use](../../browsers/browser-use/index.md) skill or cloud browser |

## Hermes vs OpenClaw

Both are always-on personal agents with chat-app gateways and skills. Hermes emphasises self-improvement and a Python codebase; [OpenClaw](../openclaw/index.md) emphasises device nodes, many channels and a TypeScript plugin ecosystem. Hermes can import an OpenClaw setup.

## Related

[Hermes index](index.md) · [Agent frameworks](../../concepts/agent-frameworks.md) · [Agents alternatives](../alternatives.md)
