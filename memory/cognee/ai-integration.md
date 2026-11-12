---
type: Playbook
title: Cognee AI Integration
description: Connecting Cognee to agents — memory plugins for Claude Code, Codex and OpenClaw, the Cognee MCP server for Cursor and other clients, SDKs, and importing memory from Mem0, Letta, Zep or Graphiti.
resource: https://github.com/topoteretes/cognee-integrations
tags: [cognee, integration, mcp, claude-code, codex, openclaw]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: cognee-integrations
    resource: "https://github.com/topoteretes/cognee-integrations"
    title: "topoteretes/cognee-integrations"
    author: "site:github.com"
  - id: cognee-docs
    resource: "https://docs.cognee.ai"
    title: "Cognee documentation"
    author: "site:docs.cognee.ai"
---

# Cognee — AI Integration

| Interface | Use |
|---|---|
| Claude Code plugin | Session memory for [Claude Code](../../agents/claude-code/index.md), captured via hooks |
| Codex plugin | Same for [Codex](../../agents/codex/index.md) (requires hooks) |
| `@cognee/cognee-openclaw` | Memory plugin for [OpenClaw](../../agents/openclaw/index.md) |
| Cognee MCP server | [MCP](../../concepts/mcp.md) tools for [Cursor](../../editors/cursor/index.md), Cline and any MCP client |
| Python / TypeScript / Rust SDKs, REST API | Your own applications |

## Patterns

* **Coding agent memory.** Plugins capture decisions, fixes and learned rules during a session; `improve` turns accepted lessons into knowledge future sessions recall.
* **Company brain.** Ingest docs, tickets, code and database exports into shared memory, browse it in the UI, query it from coding agents.
* **Framework memory.** Integrations exist for common [agent frameworks](../../concepts/agent-frameworks.md); see the integrations repository.

## Migrating from other memory systems

Cognee can import memory from [Mem0](../mem0/index.md), [Letta](../letta/index.md), [Zep](../zep/index.md) and [Graphiti](../graphiti/index.md) using its COGX exchange format.

## Related

[Cognee index](index.md) · [Agent memory](../../concepts/agent-memory.md) · [Memory alternatives](../alternatives.md)
