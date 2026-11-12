---
type: Playbook
title: Codex AI Integration
description: Extending Codex — MCP servers, plugin marketplaces and hooks (used by Cognee and Honcho memory plugins), skills, local models through Ollama or LiteLLM, and launchers such as Tailscale Aperture.
resource: https://developers.openai.com/codex
tags: [codex, integration, mcp, plugins, memory]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: codex-docs
    resource: "https://developers.openai.com/codex"
    title: "Codex documentation"
    author: "site:developers.openai.com"
---

# Codex — AI Integration

| Need | Integration |
|---|---|
| Tools | [MCP](../../concepts/mcp.md) servers in `config.toml` ([Playwright MCP](../../browsers/playwright-mcp/index.md), [Graphiti](../../memory/graphiti/mcp-server.md), [Firecrawl](../../browsers/firecrawl/ai-integration.md)) |
| Memory | Plugins/hooks from [Cognee](../../memory/cognee/ai-integration.md), [Honcho](../../memory/honcho/ai-integration.md), [Supermemory](../../memory/supermemory/ai-integration.md), [Hindsight](../../memory/hindsight/ai-integration.md) |
| Skills | `SKILL.md` folders ([Agent skills](../../concepts/agent-skills.md)) — e.g. [Graphify](../../memory/graphify/installation.md) installs one for Codex |
| Local models | Profiles for [Ollama](../../runtime/ollama/ai-integration.md) (`ollama launch codex`) or [LM Studio](../../runtime/lmstudio/index.md) |
| Gateways | [LiteLLM](../../runtime/litellm/ai-integration.md), Tailscale [Aperture](../../runtime/tailscale/ai-integration.md) |

`codex exec` makes it easy to run Codex in CI or as a step in a larger [workflow](../../concepts/workflow-automation.md).

## Related

[Codex index](index.md) · [Coding agents](../../concepts/coding-agents.md) · [Agents alternatives](../alternatives.md)
