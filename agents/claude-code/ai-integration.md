---
type: Playbook
title: Claude Code AI Integration
description: Building on and around Claude Code — the Claude Agent SDK, gateways and local models via ANTHROPIC_BASE_URL (LiteLLM, Ollama), memory plugins (Honcho, Supermemory, Cognee, Hindsight), graph and browser tools over MCP, and observability.
resource: https://code.claude.com/docs/en/overview
tags: [claude-code, integration, agent-sdk, mcp, memory]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: claude-code-docs
    resource: "https://code.claude.com/docs/en/overview"
    title: "Claude Code documentation"
    author: "site:code.claude.com"
  - id: agent-sdk
    resource: "https://docs.claude.com/en/docs/agent-sdk/overview"
    title: "Claude Agent SDK"
    author: "site:docs.claude.com"
---

# Claude Code — AI Integration

## Claude Agent SDK

The harness behind Claude Code is available as the **Claude Agent SDK** (Python and TypeScript): the same tool loop, permissions, subagents, skills, hooks and MCP support, embedded in your own agents. Use it when you want Claude Code's behaviour without the terminal UI — see [Agent frameworks](../../concepts/agent-frameworks.md).

## Models and gateways

* `ANTHROPIC_BASE_URL` points Claude Code at a gateway that speaks the Anthropic Messages API — [LiteLLM](../../runtime/litellm/ai-integration.md), Tailscale [Aperture](../../runtime/tailscale/ai-integration.md), or [Ollama](../../runtime/ollama/ai-integration.md) (`ollama launch claude`) for local models.
* Quality depends heavily on the model's agentic tool use; local models work for simpler tasks.

## Plugins and MCP for the stack

| Need | Option |
|---|---|
| Memory across sessions | [Honcho](../../memory/honcho/ai-integration.md), [Supermemory](../../memory/supermemory/ai-integration.md), [Cognee](../../memory/cognee/ai-integration.md), [Hindsight](../../memory/hindsight/ai-integration.md), [Mem0](../../memory/mem0/ai-integration.md) skills |
| Codebase graph | [Graphify](../../memory/graphify/ai-integration.md) |
| Temporal knowledge graph | [Graphiti MCP](../../memory/graphiti/mcp-server.md) |
| Browser | [Playwright MCP](../../browsers/playwright-mcp/index.md), [browser-use](../../browsers/browser-use/index.md) skill |
| Web data | [Firecrawl](../../browsers/firecrawl/ai-integration.md), [Crawl4AI](../../browsers/crawl4ai/ai-integration.md) |
| Tracing | OpenTelemetry export; [Langfuse](../../observability/langfuse/index.md) |

## Related

[Claude Code index](index.md) · [Coding agents](../../concepts/coding-agents.md) · [Agents alternatives](../alternatives.md)
