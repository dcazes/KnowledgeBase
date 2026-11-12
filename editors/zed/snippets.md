---
type: Reference
title: Zed Snippets
description: Zed settings.json snippets — language model providers including Ollama, MCP context servers, external ACP agents, and agent tool permissions.
resource: https://zed.dev/docs/ai/overview
tags: [zed, snippets, settings, mcp, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: zed-docs
    resource: "https://zed.dev/docs"
    title: "Zed documentation"
    author: "site:zed.dev"
---

# Zed — Snippets

Settings live in `~/.config/zed/settings.json` (or the project's `.zed/settings.json`). Key names evolve quickly; check the docs for your version.

```jsonc
{
  "language_models": {
    "ollama": { "api_url": "http://localhost:11434" }
  },
  "context_servers": {
    "playwright": { "command": "npx", "args": ["@playwright/mcp@latest"] }
  },
  "agent_servers": {
    "claude-code": { "type": "registry" }
  }
}
```

Open the agent panel with the command palette (`agent: new thread`) and pick Zed's agent or an external one.

## Related

[Zed index](index.md) · [AI Integration](ai-integration.md)
