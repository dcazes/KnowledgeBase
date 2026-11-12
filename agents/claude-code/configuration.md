---
type: Reference
title: Claude Code Configuration
description: Claude Code configuration surfaces — CLAUDE.md memory files, settings.json scopes and permission rules, hooks, MCP servers, custom subagents, skills, slash commands and plugin marketplaces.
resource: https://code.claude.com/docs/en/settings
tags: [claude-code, configuration, claude-md, settings, hooks, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: claude-code-docs
    resource: "https://code.claude.com/docs/en/overview"
    title: "Claude Code documentation"
    author: "site:code.claude.com"
  - id: claude-plugins
    resource: "https://github.com/anthropics/claude-plugins-official"
    title: "anthropics/claude-plugins-official"
    author: "site:github.com"
---

# Claude Code — Configuration

## Memory files

`CLAUDE.md` in the project (shared via git), `CLAUDE.local.md` (personal), and `~/.claude/CLAUDE.md` (global). Keep them short and specific: commands to build and test, conventions, gotchas. `/init` drafts one. They can `@import` other files such as `AGENTS.md`.

## Settings

`settings.json` at user (`~/.claude/`), project (`.claude/settings.json`) and local (`.claude/settings.local.json`) scope; enterprise managed settings override all.

```json
{
  "permissions": {
    "allow": ["Bash(npm run test:*)", "Bash(git diff:*)"],
    "deny":  ["Read(./.env)", "Bash(curl:*)"]
  },
  "hooks": {
    "PostToolUse": [{ "matcher": "Edit|Write",
                      "hooks": [{ "type": "command", "command": "npx prettier --write \"$CLAUDE_FILE_PATHS\"" }] }]
  }
}
```

## MCP, subagents, skills, commands

* MCP: `claude mcp add <name> <command>` or `.mcp.json` in the repo for team-shared servers.
* Subagents: Markdown files in `.claude/agents/` with frontmatter (description, tools, model).
* Skills: `.claude/skills/<name>/SKILL.md` (or user scope).
* Commands: `.claude/commands/<name>.md` → `/name`.
* Plugins: `/plugin marketplace add <owner/repo>` then `/plugin install <name>@<marketplace>`.

## Related

[Claude Code index](index.md) · [Snippets](snippets.md) · [Agent skills](../../concepts/agent-skills.md)
