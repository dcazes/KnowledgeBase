---
type: Playbook
title: Zed AI Integration
description: Running agents in Zed — the native agent with hosted or local models, external agents over ACP (Claude Code, Codex, Gemini CLI), MCP context servers, and AGENTS.md rules.
resource: https://zed.dev/docs/ai/overview
tags: [zed, integration, acp, local-models]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: zed-docs
    resource: "https://zed.dev/docs"
    title: "Zed documentation"
    author: "site:zed.dev"
  - id: acp
    resource: "https://agentclientprotocol.com"
    title: "Agent Client Protocol"
    author: "site:agentclientprotocol.com"
---

# Zed — AI Integration

| Need | Option |
|---|---|
| Local models | [Ollama](../../runtime/ollama/index.md), [LM Studio](../../runtime/lmstudio/index.md), OpenAI-compatible endpoints ([LiteLLM](../../runtime/litellm/index.md)) |
| External agents | [Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md), Gemini CLI and others via ACP |
| Tools | [MCP](../../concepts/mcp.md) context servers — [Playwright MCP](../../browsers/playwright-mcp/index.md), [Graphiti](../../memory/graphiti/mcp-server.md) |
| Project rules | `AGENTS.md` shared with other agents ([Context engineering](../../concepts/context-engineering.md)) |

## Related

[Zed index](index.md) · [Editors alternatives](../alternatives.md)
