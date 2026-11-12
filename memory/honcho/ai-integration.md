---
type: Playbook
title: Honcho AI Integration
description: First-party Honcho memory plugins for coding agents — Claude Code, Codex, Cursor, OpenCode, Kilo Code, OpenClaw, Hermes — plus remote MCP, a shared config file, and the integration skill for your own apps.
resource: https://github.com/plastic-labs/honcho
tags: [honcho, integration, mcp, claude-code, codex, openclaw, hermes]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: honcho-github
    resource: "https://github.com/plastic-labs/honcho"
    title: "plastic-labs/honcho on GitHub"
    author: "site:github.com"
  - id: honcho-docs
    resource: "https://honcho.dev/docs/v3"
    title: "Honcho documentation (v3)"
    author: "site:honcho.dev"
---

# Honcho — AI Integration

All plugins read `~/.honcho/config.json`, so one `honcho init` configures every agent — and pointing two agents at the same workspace gives them **one shared memory**.

| Agent | Install |
|---|---|
| [Claude Code](../../agents/claude-code/index.md) | `/plugin marketplace add plastic-labs/claude-honcho` then `/plugin install honcho@honcho` |
| [Codex](../../agents/codex/index.md) | `npm install -g @honcho-ai/codex-honcho && codex-honcho install` (hooks + MCP + skill) |
| [Cursor](../../editors/cursor/index.md) | Install **Honcho** from the Cursor Marketplace, then `/honcho-setup` |
| [OpenCode](../../agents/opencode/index.md) | `opencode plugin "@honcho-ai/opencode-honcho" --global` |
| Kilo Code | `kilo plugin @honcho-ai/kilo-honcho --global` (CLI, VS Code and JetBrains) |
| [OpenClaw](../../agents/openclaw/index.md) | `openclaw plugins install @honcho-ai/openclaw-honcho && openclaw honcho setup` — can migrate `MEMORY.md` / `USER.md` / `IDENTITY.md` |
| [Hermes](../../agents/hermes/index.md) | `hermes memory setup` and choose `honcho` (built in) |

## Any MCP client

```bash
claude mcp add honcho --transport http --url "https://mcp.honcho.dev" \
  --header "Authorization: Bearer hch-..." --header "X-Honcho-User-Name: YourName"
```

The same form works in Cline, Windsurf and other [MCP](../../concepts/mcp.md) clients.

## Your own application

`npx skills add plastic-labs/honcho` installs an integration [skill](../../concepts/agent-skills.md): run `/honcho-integration` in a coding agent and it wires the SDK into your codebase and verifies it.

## Inspecting memory

Use [OpenConcho](../openconcho/index.md) to browse peers, conclusions, sessions and dream passes.

## Related

[Honcho index](index.md) · [Agent memory](../../concepts/agent-memory.md) · [Memory alternatives](../alternatives.md)
