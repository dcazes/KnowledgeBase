---
type: Playbook
title: Letta AI Integration
description: Where Letta fits — always-on personal and team agents with self-managed memory, shared skills with other harnesses, subagents, messaging channels, the Letta Agent SDK, and GitHub Actions.
resource: https://docs.letta.com
tags: [letta, integration, agents, skills, multi-agent]
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

# Letta — AI Integration

## Good fits

* **Long-lived assistants** that should accumulate knowledge about a person, team or codebase over months.
* **Always-on agents** driven by crons and heartbeats that report through Slack or Telegram.
* **Coding work** with memory: Letta Code is also a terminal [coding agent](../../concepts/coding-agents.md), comparable to [Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md) and [OpenCode](../../agents/opencode/index.md), but with persistent self-edited memory.

## Building on it

* **Letta Agent SDK** (TypeScript) embeds Letta agents in your own applications.
* **letta-code-action** runs Letta agents in GitHub Actions.
* Bring any model with `/connect`, including [OpenAI-compatible](../../concepts/openai-compatible-api.md) endpoints.

## Interoperability

* Skills install straight from GitHub, ClawHub ([OpenClaw](../../agents/openclaw/index.md)) and the [Hermes](../../agents/hermes/index.md) skills hub, so skill libraries are portable across harnesses.
* Agents call other agents as subagents — see [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md).

## Letta vs a memory service

| Choose | When |
|---|---|
| Letta | The agent should own and reorganise its memory |
| [Mem0](../mem0/index.md) / [Supermemory](../supermemory/index.md) | Your app controls the agent loop and needs a fact store |
| [Zep](../zep/index.md) / [Graphiti](../graphiti/index.md) | You need temporal relationships and provenance |
| [Honcho](../honcho/index.md) | You need models of users (peers) built from conversations |

## Related

[Letta index](index.md) · [Agent memory](../../concepts/agent-memory.md) · [Memory alternatives](../alternatives.md)
