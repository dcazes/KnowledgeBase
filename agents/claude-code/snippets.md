---
type: Reference
title: Claude Code Snippets
description: Claude Code cheat sheet — launching and resuming, print/headless mode with JSON output, useful slash commands, MCP management, and running in CI.
resource: https://code.claude.com/docs/en/cli-reference
tags: [claude-code, snippets, cli, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: claude-code-docs
    resource: "https://code.claude.com/docs/en/overview"
    title: "Claude Code documentation"
    author: "site:code.claude.com"
---

# Claude Code — Snippets

```bash
claude                                  # interactive
claude "explain the auth flow"          # start with a prompt
claude -c                               # continue the last session
claude -r                               # pick a session to resume
claude -p "list TODOs in src/" --output-format json     # headless, scriptable
git diff | claude -p "review this diff for bugs"
claude mcp add playwright npx @playwright/mcp@latest
claude mcp list
```

| Slash command | Purpose |
|---|---|
| `/init` | Draft CLAUDE.md |
| `/model` | Switch model |
| `/compact`, `/clear` | Shrink or reset context |
| `/permissions`, `/hooks`, `/mcp` | Inspect configuration |
| `/agents` | Manage subagents |
| `/plugin` | Marketplaces and plugins |
| `/cost`, `/context` | Usage and context breakdown |

## Related

[Claude Code index](index.md) · [Configuration](configuration.md)
