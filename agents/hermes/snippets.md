---
type: Reference
title: Hermes Agent Snippets
description: Hermes command cheat sheet — CLI subcommands, in-chat slash commands for models, personalities, retries, context compression, usage and skills, and gateway commands.
resource: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
tags: [hermes, snippets, cli, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hermes-github
    resource: "https://github.com/NousResearch/hermes-agent"
    title: "NousResearch/hermes-agent on GitHub"
    author: "site:github.com"
---

# Hermes Agent — Snippets

```bash
hermes                      # chat
hermes model | tools | setup | doctor | update
hermes gateway setup && hermes gateway start
hermes portal info
hermes memory setup
hermes import-agent codex
```

| In chat | Effect |
|---|---|
| `/new`, `/reset` | Fresh conversation |
| `/model provider:model` | Switch model |
| `/personality <name>` | Change persona |
| `/retry`, `/undo` | Redo or undo the last turn |
| `/compress`, `/usage`, `/insights 7` | Shrink context, show usage, weekly insights |
| `/skills`, `/<skill-name>` | List or run skills |
| `/stop` (chat) or Ctrl+C (CLI) | Interrupt |

## Related

[Hermes index](index.md) · [Configuration](configuration.md)
