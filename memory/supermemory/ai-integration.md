---
type: Playbook
title: Supermemory AI Integration
description: Supermemory's open-source memory plugins for Claude Code, Cursor, Codex, OpenCode, OpenClaw and Hermes, the hosted MCP server, and framework wrappers for app developers.
resource: https://github.com/supermemoryai/supermemory
tags: [supermemory, integration, mcp, claude-code, cursor, hermes]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: supermemory-github
    resource: "https://github.com/supermemoryai/supermemory"
    title: "supermemoryai/supermemory on GitHub"
    author: "site:github.com"
---

# Supermemory — AI Integration

## Plugins (open source)

| Assistant | Plugin |
|---|---|
| [Claude Code](../../agents/claude-code/index.md) | `supermemoryai/claude-supermemory` |
| [Cursor](../../editors/cursor/index.md) | `supermemoryai/cursor-supermemory` |
| [Codex](../../agents/codex/index.md) | `supermemoryai/codex-supermemory` |
| [OpenCode](../../agents/opencode/index.md) | `supermemoryai/opencode-supermemory` |
| [OpenClaw](../../agents/openclaw/index.md) | `supermemoryai/openclaw-supermemory` |
| [Hermes](../../agents/hermes/index.md) | Built-in Supermemory memory provider |

Once installed, the assistant saves worthwhile facts automatically and recalls them in later sessions.

## MCP clients

Claude Desktop, Cursor, [Windsurf](../../editors/windsurf/index.md), [VS Code](../../editors/vscode/index.md), Claude Code, OpenCode, OpenClaw and Hermes can use the hosted [MCP](../../concepts/mcp.md) server.

## For app developers

Framework wrappers cover the major [agent frameworks](../../concepts/agent-frameworks.md) and SDKs; the common pattern is one `profile()` call before generation and `add()` after. Because it combines documents and memory, Supermemory can replace a separate [RAG](../../concepts/rag.md) pipeline for small apps.

## Related

[Supermemory index](index.md) · [Agent memory](../../concepts/agent-memory.md) · [Memory alternatives](../alternatives.md)
