---
type: Reference
title: Letta Snippets
description: Letta Code command cheat sheet — slash commands for memory and dreaming, installing skills from GitHub, ClawHub or Hermes hub, remote computers, and headless prompts.
resource: https://docs.letta.com/letta-code/slash-commands
tags: [letta, snippets, cli, cheat-sheet, skills]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: letta-code-github
    resource: "https://github.com/letta-ai/letta-code"
    title: "letta-ai/letta-code on GitHub"
    author: "site:github.com"
  - id: letta-docs
    resource: "https://docs.letta.com"
    title: "Letta documentation"
    author: "site:docs.letta.com"
---

# Letta — Snippets

## Slash commands (inside `letta`)

| Command | What it does |
|---|---|
| `/connect`, `/model` | Add provider keys, switch model |
| `/search <text>` | Search messages across agents |
| `/memory-repository set git@github.com:me/agent-memory.git` | Sync MemFS to your repo |
| `/dream`, `/reflect`, `/sleeptime` | Trigger or configure sleep-time reflection |
| `/skills`, `/skill-creator` | List or create skills |
| `/login` | Access agents in your Letta account |

## Skills

```bash
letta skills install https://github.com/owner/repo                       # whole repo
letta skills install https://github.com/owner/repo/tree/main/path/to/skill
letta skills install <clawhub-slug>             # skills published on ClawHub
letta skills list   --agent <agent-id>
letta skills delete <skill-name> --agent <agent-id>
```

Skills use the same `SKILL.md` format as [OpenClaw](../../agents/openclaw/index.md), [Hermes](../../agents/hermes/index.md) and [Claude Code](../../agents/claude-code/index.md) — see [Agent skills](../../concepts/agent-skills.md).

## Remote computers and headless mode

```bash
letta computers list --online-only
letta computers current
letta -p --agent <agent-id> --computer "work-laptop" "summarise yesterday's commits"
letta -p --agent <agent-id> --computer cloud "run the nightly report"
```

## Related

[Letta index](index.md) · [Installation](installation.md)
