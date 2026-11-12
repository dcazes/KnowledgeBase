---
type: Concept
title: OpenCode Overview
description: How OpenCode works — built-in build and plan agents, the general subagent, tools for files, shell and web, LSP diagnostics, session management and sharing, and its client/server architecture that allows remote and programmatic control.
resource: https://opencode.ai/docs
tags: [opencode, overview, agents, lsp, client-server]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: opencode-docs
    resource: "https://opencode.ai/docs"
    title: "OpenCode documentation"
    author: "site:opencode.ai"
  - id: opencode-github
    resource: "https://github.com/anomalyco/opencode"
    title: "anomalyco/opencode on GitHub"
    author: "site:github.com"
---

# OpenCode — Overview

## Built-in agents

| Agent | Behaviour |
|---|---|
| **build** (default) | Full access: edits files, runs commands |
| **plan** | Read-only analysis; denies edits, asks before shell commands |
| **general** (subagent) | Multi-step searches and tasks, invoked with `@general` |

Switch between primary agents with **Tab**. Custom agents and subagents are Markdown or JSON definitions — see [Agents, commands & rules](hierarchical-structure.md).

## Tools and context

* File read/write/edit, glob and grep, shell, web fetch, todo lists, and [MCP](../../concepts/mcp.md) tools.
* **LSP integration**: language servers feed diagnostics back to the model after edits, catching errors without running the build.
* Project rules from `AGENTS.md`; `/init` generates one by exploring the repo.
* Session history, undo/redo, compaction of long sessions, and shareable session links.

## Client/server

The TUI is a client of a local server. `opencode serve` runs the server headless, and the SDK drives it programmatically — useful for CI, bots and custom front ends.

## Why people choose it

Open source, any model (including local), no vendor lock-in, and a strong plugin ecosystem — memory plugins from [Honcho](../../memory/honcho/ai-integration.md), [Supermemory](../../memory/supermemory/ai-integration.md) and [Hindsight](../../memory/hindsight/ai-integration.md) all target it.

## Related

[OpenCode index](index.md) · [Configuration](configuration.md) · [Coding agents](../../concepts/coding-agents.md)
