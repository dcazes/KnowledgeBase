---
type: Concept
title: CrewAI Overview
description: CrewAI concepts — role-based agents, tasks with expected outputs, crews with sequential or hierarchical processes, Flows with state and event listeners, tools, memory and knowledge sources, and trade-offs versus graph-based frameworks.
resource: https://docs.crewai.com
tags: [crewai, overview, crews, flows]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: crewai-docs
    resource: "https://docs.crewai.com"
    title: "CrewAI documentation"
    author: "site:docs.crewai.com"
---

# CrewAI — Overview

| Concept | Meaning |
|---|---|
| Agent | Role, goal, backstory, LLM, tools; can delegate to others |
| Task | Description, expected output, assigned agent, optional structured output |
| Crew | Agents + tasks + **process**: `sequential` or `hierarchical` (a manager plans and delegates) |
| Flow | Event-driven orchestration with typed state, `@start`, `@listen`, `@router` decorators |
| Memory | Short-term, long-term and entity memory for agents |
| Knowledge | Documents attached to agents or crews for retrieval |

## Crews vs Flows

Crews optimise for autonomy — agents decide how to collaborate. Flows optimise for control — you decide the order and branching, calling crews where autonomy helps. Most production apps combine both.

## Trade-offs

Fast to prototype and easy to read; less fine-grained control over state and resumption than [LangGraph](../langgraph/index.md). Multi-agent role-play can cost many tokens — measure with [evals](../../concepts/evals.md) whether more agents actually help.

## Related

[CrewAI index](index.md) · [Snippets](snippets.md) · [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md)
