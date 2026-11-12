---
type: Reference
title: OpenCode Configuration
description: OpenCode's opencode.json — model and provider selection including local OpenAI-compatible servers, permissions for edits and shell commands, MCP servers, formatters and LSP, with global and per-project scopes.
resource: https://opencode.ai/docs/config
tags: [opencode, configuration, opencode-json, permissions, mcp]
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

# OpenCode — Configuration

Config merges from a global file (`~/.config/opencode/opencode.json`) and the project's `opencode.json`.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-5",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "options": { "baseURL": "http://localhost:11434/v1" },
      "models": { "qwen3-coder:30b": {} }
    }
  },
  "permission": {
    "edit": "ask",
    "bash": { "git push*": "ask", "rm *": "deny", "*": "allow" }
  },
  "mcp": {
    "playwright": { "type": "local", "command": ["npx", "@playwright/mcp@latest"] },
    "graphiti":   { "type": "remote", "url": "http://localhost:8000/mcp/" }
  }
}
```

* **Models:** `provider/model` ids; providers come from the models.dev catalogue, plus any [OpenAI-compatible](../../concepts/openai-compatible-api.md) endpoint ([Ollama](../../runtime/ollama/index.md), [vLLM](../../runtime/vllm/index.md), [LiteLLM](../../runtime/litellm/index.md)).
* **Permissions:** `allow` / `ask` / `deny` for edits, shell (with glob patterns) and web fetch — your main safety lever ([Agent security](../../concepts/agent-security.md)).
* **MCP:** local (stdio) or remote (HTTP) [MCP](../../concepts/mcp.md) servers.
* **Formatters and LSP** are auto-detected and configurable.

Model ids above are examples; use whatever your providers currently offer.

## Related

[OpenCode index](index.md) · [Agents, commands & rules](hierarchical-structure.md)
