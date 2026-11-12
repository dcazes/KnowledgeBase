---
type: Concept
title: Multi-Agent Orchestration
description: Coordinating several AI agents — supervisor, hand-off, swarm and pipeline topologies, subagents for context isolation, parallel agents, shared memory, inter-agent protocols, and when multiple agents are worth their cost.
resource: https://github.com/topics/multi-agent-systems
tags: [concept, multi-agent, orchestration, subagents, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: anthropic-multi-agent
    resource: "https://www.anthropic.com/engineering/multi-agent-research-system"
    title: "How we built our multi-agent research system"
    author: "Anthropic"
---

# Multi-Agent Orchestration

Sometimes one agent is not enough: tasks are too broad for one context window, parts can run in parallel, or specialists do better than a generalist. **Orchestration** is how several agents divide and combine work.

## Topologies

| Pattern | How | Examples |
|---|---|---|
| Supervisor / orchestrator–workers | A lead agent plans and delegates to workers, then synthesises | [LangGraph](../agents/langgraph/overview.md) supervisor, [CrewAI](../agents/crewai/overview.md) hierarchical process |
| Subagents | Spawn a fresh context for a sub-task; only the summary returns | [Claude Code](../agents/claude-code/overview.md), [OpenCode](../agents/opencode/overview.md) `@general`, [Letta](../memory/letta/overview.md) |
| Hand-off | Control passes between specialists | [Pydantic AI](../agents/pydanticAI/pydantic_ai.md), OpenAI Agents SDK |
| Pipeline / crew | Fixed sequence of roles | [CrewAI](../agents/crewai/index.md) sequential |
| Parallel independent agents | Several agents on separate branches or projects | [Antigravity](../agents/antigravity/agents.md), Codex cloud, Cursor cloud agents |
| Peer-to-peer across systems | Agents built separately talk over a protocol | [A2A](a2a.md) |

## Shared state

Agents can share a memory layer — [MemOS](../memory/memos/ai-integration.md) cubes, a shared [Honcho](../memory/honcho/ai-integration.md) workspace, a [Graphiti](../memory/graphiti/index.md) group — or pass artefacts (files, plans) explicitly.

## When it is worth it

Multi-agent systems use many more tokens and fail in new ways (agents misunderstanding each other, duplicated work). They pay off for broad research, parallelisable work and context isolation; for linear tasks a single agent with good tools usually wins. Measure with [evals](evals.md).

## Related

[Agent frameworks](agent-frameworks.md) · [A2A](a2a.md) · [Agents alternatives](../agents/alternatives.md) · [Concepts index](index.md)
