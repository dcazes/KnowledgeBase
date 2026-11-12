---
type: Software
title: OpenCode
description: Open-source terminal coding agent (also desktop app) that works with 75+ model providers including local models — build and plan agents, subagents, LSP integration, MCP, custom agents and commands, plugins, and a client/server architecture with an SDK.
resource: https://opencode.ai
tags: [opencode, coding-agents, terminal, open-source, mcp, typescript]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: opencode-github
    resource: "https://github.com/anomalyco/opencode"
    title: "anomalyco/opencode on GitHub"
    author: "site:github.com"
  - id: opencode-docs
    resource: "https://opencode.ai/docs"
    title: "OpenCode documentation"
    author: "site:opencode.ai"
---

# OpenCode

**OpenCode** is the leading open-source, provider-agnostic alternative to [Claude Code](../claude-code/index.md) and [Codex](../codex/index.md): a terminal UI (plus a beta desktop app) where an agent reads, edits and runs your code with any model — Anthropic, OpenAI, Google, open models via OpenRouter, or local [Ollama](../../runtime/ollama/index.md) / [LM Studio](../../runtime/lmstudio/index.md).

| | |
|---|---|
| Category | [Coding agents](../../concepts/coding-agents.md) |
| License | MIT |
| Language | TypeScript (Bun) |
| Latest release | v1.19.5 (2026-10-28); v2 installers rolling out (`opencode.ai/v2/install`) |
| Interfaces | TUI · desktop app (beta) · headless server + SDK · IDE integration |

## Contents

* [Overview](overview.md) — agents, tools, LSP, sessions, client/server design
* [Installation](installation.md) — installers and package managers
* [Configuration](configuration.md) — `opencode.json`, providers, permissions, MCP
* [Agents, commands & rules](hierarchical-structure.md) — how config, agents and AGENTS.md layer
* [Snippets](snippets.md) — CLI and in-session commands
* [AI Integration](ai-integration.md) — local models, memory plugins, MCP servers

## Related

* Concepts: [Coding agents](../../concepts/coding-agents.md) · [MCP](../../concepts/mcp.md) · [Agent skills](../../concepts/agent-skills.md) · [Context engineering](../../concepts/context-engineering.md)
* Peers: [Claude Code](../claude-code/index.md), [Codex](../codex/index.md), [Aider](../aider/index.md), [Hermes](../hermes/index.md); editors [Cursor](../../editors/cursor/index.md), [Zed](../../editors/zed/index.md)
* Comparison: [Agents alternatives](../alternatives.md)
