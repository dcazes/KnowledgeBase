---
type: Concept
title: Claude Code Overview
description: How Claude Code works — the agentic loop over tools (read, edit, search, bash, web), permission modes and plan mode, subagents and background tasks, context management and compaction, and the many surfaces it runs on.
resource: https://code.claude.com/docs/en/overview
tags: [claude-code, overview, agent-loop, permissions, subagents]
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

# Claude Code — Overview

## The loop

Claude reads the request, gathers context with tools (file reads, glob/grep search, shell commands, web fetch), proposes and makes edits, runs checks, and iterates until done. Long sessions are **compacted** automatically to stay within the context window.

## Permissions and modes

* Each tool call is allowed, asked or denied by **permission rules** (e.g. allow `Bash(npm test:*)`, deny `Read(./.env)`).
* **Plan mode** explores read-only and proposes a plan before any change.
* **Auto-accept / bypass** modes trade safety for speed — use only in sandboxes.
* Sandboxed bash restricts filesystem and network access for commands.

## Extending it

| Mechanism | What it is |
|---|---|
| `CLAUDE.md` | Project and user memory loaded every session |
| [Skills](../../concepts/agent-skills.md) | `SKILL.md` folders loaded on demand when relevant |
| Subagents | Specialised agents with their own context, prompt and tools; run in parallel or background |
| Hooks | Shell commands run on events (before/after a tool, on stop, on prompt) — deterministic guardrails |
| [MCP](../../concepts/mcp.md) servers | External tools and data |
| Plugins | Bundles of commands, agents, skills, hooks and MCP servers, installed from marketplaces |

## Surfaces

Terminal, IDE extensions, a desktop app, the web (cloud sessions), Slack, and CI via GitHub Actions; programmatic use through headless mode and the Claude Agent SDK.

## Related

[Claude Code index](index.md) · [Configuration](configuration.md) · [Coding agents](../../concepts/coding-agents.md)
