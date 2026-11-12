---
type: Playbook
title: MemOS AI Integration
description: MemOS integrations for agent harnesses — OpenClaw cloud and local plugins, the Hermes local plugin, DeepSeek Harness, and multi-agent memory sharing through cubes.
resource: https://github.com/MemTensor/MemOS
tags: [memos, integration, openclaw, hermes, multi-agent]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: memos-github
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemTensor/MemOS on GitHub"
    author: "site:github.com"
---

# MemOS — AI Integration

## Agent harness plugins

| Harness | Plugin | Notes |
|---|---|---|
| [OpenClaw](../../agents/openclaw/index.md) | Cloud plugin | Hosted memory, multi-agent sharing; MemTensor reports 72% lower token use |
| OpenClaw, [Hermes](../../agents/hermes/index.md) | `memos-local-plugin` 2.0 | 100% local, hybrid FTS5 + vector retrieval, skill evolution |
| DeepSeek Harness | Local and cloud plugins | Auto-recall before a task, retain after a successful turn, local Memory Viewer |

## Multi-agent memory

Give each agent a private cube and a shared team cube: agents write their own experience privately and promote useful facts to the shared cube. This maps onto [multi-agent orchestration](../../concepts/multi-agent-orchestration.md) patterns in [LangGraph](../../agents/langgraph/index.md) or [CrewAI](../../agents/crewai/index.md).

## Apps

Use the REST API with the store → retrieve → inject loop common to all [agent memory](../../concepts/agent-memory.md) systems.

## Related

[MemOS index](index.md) · [Memory alternatives](../alternatives.md)
