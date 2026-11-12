---
type: Reference
title: Continue Snippets
description: A Continue config.yaml using local Ollama models for chat, autocomplete and embeddings, a hosted model, rules, and an MCP server.
resource: https://docs.continue.dev
tags: [continue, snippets, config-yaml, ollama, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: continue-docs
    resource: "https://docs.continue.dev"
    title: "Continue documentation"
    author: "site:docs.continue.dev"
---

# Continue — Snippets

```yaml
name: local-assistant
version: 1.0.0
schema: v1
models:
  - name: Qwen Coder
    provider: ollama
    model: qwen3-coder:30b
    roles: [chat, edit, apply]
  - name: Autocomplete
    provider: ollama
    model: qwen2.5-coder:1.5b-base
    roles: [autocomplete]
  - name: Embedder
    provider: ollama
    model: nomic-embed-text
    roles: [embed]
rules:
  - Prefer small, tested changes.
mcpServers:
  - name: playwright
    command: npx
    args: ["@playwright/mcp@latest"]
```

## Related

[Continue index](index.md) · [Overview](overview.md)
