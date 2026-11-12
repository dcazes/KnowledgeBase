---
type: Playbook
title: Cursor AI Integration
description: Connecting Cursor to the wider stack — model choices and BYO keys, MCP servers for browsers, graphs and memory, marketplace memory plugins, Graphify for structure, and local models through gateways.
resource: https://cursor.com/docs
tags: [cursor, integration, mcp, memory]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cursor-docs
    resource: "https://cursor.com/docs"
    title: "Cursor documentation"
    author: "site:cursor.com"
---

# Cursor — AI Integration

| Need | Option |
|---|---|
| Browser | [Playwright MCP](../../browsers/playwright-mcp/index.md) |
| Codebase structure | [Graphify](../../memory/graphify/ai-integration.md) skill/MCP |
| Memory | [Honcho](../../memory/honcho/ai-integration.md), [Supermemory](../../memory/supermemory/ai-integration.md), [Hindsight](../../memory/hindsight/ai-integration.md), [Cognee](../../memory/cognee/ai-integration.md) via MCP |
| Web data | [Firecrawl](../../browsers/firecrawl/ai-integration.md) MCP |
| Workflows as tools | [n8n](../../apps/n8n/ai-integration.md) MCP Server Trigger |
| Other agents in the editor | [Codex](../../agents/codex/index.md) and [Claude Code](../../agents/claude-code/index.md) extensions run inside Cursor |

Custom OpenAI-compatible endpoints (e.g. [LiteLLM](../../runtime/litellm/index.md)) can be configured for chat; Tab and some features use Cursor's own models.

## Related

[Cursor index](index.md) · [Editors alternatives](../alternatives.md)
