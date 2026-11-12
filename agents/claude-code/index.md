---
type: Software
title: Claude Code
description: Anthropic's agentic coding tool for the terminal, IDEs, desktop and web — reads and edits code, runs commands, and extends through CLAUDE.md memory, skills, subagents, hooks, MCP servers and plugins; also available programmatically via the Claude Agent SDK.
resource: https://code.claude.com
tags: [claude-code, anthropic, coding-agents, mcp, agent-skills, hooks]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: claude-code-docs
    resource: "https://code.claude.com/docs/en/overview"
    title: "Claude Code documentation"
    author: "site:code.claude.com"
  - id: claude-code-github
    resource: "https://github.com/anthropics/claude-code"
    title: "anthropics/claude-code on GitHub"
    author: "site:github.com"
  - id: claude-plugins
    resource: "https://github.com/anthropics/claude-plugins-official"
    title: "anthropics/claude-plugins-official"
    author: "site:github.com"
---

# Claude Code

**Claude Code** is Anthropic's agent for software work. Started in a project directory, it explores the codebase, plans, edits files, runs tests and commands, and manages git — asking permission according to rules you set. It popularised several conventions now shared across the ecosystem: project memory files, [skills](../../concepts/agent-skills.md), hooks and plugin marketplaces.

| | |
|---|---|
| Category | [Coding agents](../../concepts/coding-agents.md) |
| License | Proprietary (source-available repo for issues, plugins and examples) |
| Latest release | v2.1.322 (2026-11-10) |
| Surfaces | Terminal CLI · VS Code / JetBrains extensions · desktop app · web · Slack · GitHub Actions |
| Models | Anthropic Claude models; Bedrock, Vertex and Foundry; gateways via `ANTHROPIC_BASE_URL` |

## Contents

* [Overview](overview.md) — agent loop, tools, permissions, modes
* [Installation](installation.md) — native installer, Homebrew, WinGet
* [Configuration](configuration.md) — CLAUDE.md, settings, permissions, hooks, MCP, subagents, skills, plugins
* [Snippets](snippets.md) — CLI flags, slash commands, headless use
* [AI Integration](ai-integration.md) — Agent SDK, local and gateway models, memory and tool plugins

## Related

* Concepts: [Coding agents](../../concepts/coding-agents.md) · [Agent skills](../../concepts/agent-skills.md) · [MCP](../../concepts/mcp.md) · [Context engineering](../../concepts/context-engineering.md) · [Agent security](../../concepts/agent-security.md)
* Peers: [Codex](../codex/index.md), [OpenCode](../opencode/index.md), [Aider](../aider/index.md), [Antigravity](../antigravity/index.md), [Cursor](../../editors/cursor/index.md)
* Comparison: [Agents alternatives](../alternatives.md)
