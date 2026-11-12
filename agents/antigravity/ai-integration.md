---
type: Playbook
title: Antigravity AI Integration
description: Where Antigravity sits among AI tools — compared with Claude Code, Codex and OpenCode, MCP support, memory plugins such as Hindsight's coding-agent installer, and using Playwright MCP from its settings.
resource: https://antigravity.google
tags: [antigravity, integration, coding-agents, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: antigravity-site
    resource: "https://antigravity.google/"
    title: "Antigravity — official site"
    author: "site:antigravity.google"
---

# Antigravity — AI Integration

* **Versus other coding agents:** [Claude Code](../claude-code/index.md) (Anthropic models, deep extensibility), [Codex](../codex/index.md) (open source, strict sandbox), [OpenCode](../opencode/index.md) (any model, open source). Antigravity's strengths are parallel agent orchestration and tight Gemini/Google Cloud integration.
* **MCP:** Antigravity supports [MCP](../../concepts/mcp.md) servers — [Playwright MCP](../../browsers/playwright-mcp/installation.md) documents an Antigravity config.
* **Memory:** [Hindsight](../../memory/hindsight/ai-integration.md)'s coding-agent installer supports the Antigravity CLI.
* **Delegation:** community tools let Claude Code or Codex hand sub-tasks to `agy` as a fast Gemini worker — an example of cross-vendor [multi-agent orchestration](../../concepts/multi-agent-orchestration.md).

## Related

[Antigravity index](index.md) · [Agents alternatives](../alternatives.md)
