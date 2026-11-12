---
type: Reference
title: OpenCode Snippets
description: OpenCode cheat sheet — launching, non-interactive runs, headless server, model listing, and in-session commands and shortcuts.
resource: https://opencode.ai/docs/cli
tags: [opencode, snippets, cli, cheat-sheet]
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

# OpenCode — Snippets

```bash
opencode                                   # TUI in the current directory
opencode run "add input validation to the signup handler"   # non-interactive
opencode serve --port 4096                 # headless server for the SDK / remote clients
opencode models                            # list available models
opencode upgrade
```

| In session | Effect |
|---|---|
| `Tab` | Switch build ↔ plan |
| `@general …`, `@<agent>` | Call a subagent |
| `/init` | Create or update AGENTS.md |
| `/connect`, `/models` | Add provider, switch model |
| `/undo`, `/redo` | Revert or reapply changes |
| `/compact` | Summarise long sessions |
| `/share` | Share a session link |

## Related

[OpenCode index](index.md) · [Configuration](configuration.md)
