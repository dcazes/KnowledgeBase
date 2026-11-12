---
type: Reference
title: Codex Snippets
description: Codex cheat sheet — interactive and one-shot runs, codex exec for CI, sandbox and approval flags, config.toml with profiles, MCP servers and features.
resource: https://developers.openai.com/codex
tags: [codex, snippets, cli, config-toml, cheat-sheet]
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

# Codex — Snippets

```bash
codex                                        # interactive
codex "write tests for utils/date.ts"
codex exec "fix the failing lint errors"     # non-interactive, for scripts and CI
codex --sandbox workspace-write --ask-for-approval on-request
codex resume                                 # continue a previous session
codex mcp add playwright -- npx @playwright/mcp@latest
codex features enable hooks
```

## `~/.codex/config.toml`

```toml
model = "gpt-5-codex"
sandbox_mode = "workspace-write"
approval_policy = "on-request"

[sandbox_workspace_write]
network_access = false

[mcp_servers.graphiti]
url = "http://localhost:8000/mcp/"

[profiles.local]
model_provider = "ollama"
model = "qwen3-coder:30b"

[features]
hooks = true
```

Model names are examples; check your account's current models.

## Related

[Codex index](index.md) · [Overview](overview.md)
