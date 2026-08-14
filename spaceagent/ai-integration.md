---
type: Concept
title: Space Agent AI Integration
description: Integrate Space Agent — live workspace reshaping (UI/tools/widgets), SKILL.md capabilities, server API for agents, vs terminal agents.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, integration, skills, agents]
timestamp: 2026-08-13T00:00:00Z
---

# AI Integration

Space Agent is unique among this vault's agents: it doesn't just call tools — **it builds them into the workspace live**.

## Live reshaping

While you work, the agent can construct new **pages, tools, widgets, and workflows** directly in the running workspace (browser/desktop runtime). The workspace's capability surface grows with use.

## SKILL.md system

* Capabilities = plain-text `SKILL.md` files the agent authors and extends itself.
* This is the integration surface for other agents too: adding a `SKILL.md` to the space grants the agent that skill (same convention as Hermes/OpenCode skills).

## Server mode

`node space serve` exposes the workspace server-side (port 3000) — enables **team/hierarchical** usage and programmatic access for external tooling.

## vs the other agents here

| Agent | Runtime | Model |
|---|---|---|
| **Space Agent** | browser/desktop (frontend runtime) | reshapes UI/tools live |
| [OpenClaw](../openclaw/index.md) | local daemon | orchestration, skills, memory |
| [OpenCode](../opencode/index.md) | terminal | code agent, delegation |
| [Hermes](../hermes/index.md) | terminal | skills, tools, cron |

Complementary: Space Agent for in-workspace UI/tool building; the terminal agents for code/dev workflows.

# Citations

[1] [Space Agent GitHub](https://github.com/agent0ai/space-agent)
