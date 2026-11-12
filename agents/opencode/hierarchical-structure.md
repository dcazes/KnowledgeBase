---
type: Concept
title: OpenCode Agents, Commands & Rules
description: How OpenCode layers configuration — global and project config, AGENTS.md rules, custom primary agents and subagents in Markdown, custom slash commands, and skills — and how this compares with Claude Code and Codex conventions.
resource: https://opencode.ai/docs/agents
tags: [opencode, agents, rules, agents-md, commands]
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

# OpenCode — Agents, Commands & Rules

| Layer | Location | Purpose |
|---|---|---|
| Global config | `~/.config/opencode/opencode.json` | Defaults for every project |
| Project config | `opencode.json` | Models, permissions, MCP for this repo |
| Rules | `AGENTS.md` (project), global rules file | Always-loaded instructions |
| Agents | `.opencode/agent/*.md` (or global) | Custom primary agents and subagents with their own prompt, model, tools and permissions |
| Commands | `.opencode/command/*.md` | Reusable prompts invoked as `/name` |
| Skills | `SKILL.md` folders | On-demand procedures ([Agent skills](../../concepts/agent-skills.md)) |

## Example subagent

```markdown
---
description: Reviews diffs for security problems
mode: subagent
model: anthropic/claude-sonnet-4-5
tools: { write: false, edit: false }
---
You are a security reviewer. Inspect the changes and report injection, auth and secrets issues.
```

Invoke with `@security-reviewer`.

## Shared conventions

`AGENTS.md` is read by OpenCode, [Codex](../codex/index.md), [Cursor](../../editors/cursor/index.md), [Zed](../../editors/zed/index.md) and others; [Claude Code](../claude-code/index.md) uses `CLAUDE.md` (and can import `AGENTS.md`). Keeping one `AGENTS.md` per repo makes instructions portable — see [Context engineering](../../concepts/context-engineering.md).

## Related

[OpenCode index](index.md) · [Configuration](configuration.md)
