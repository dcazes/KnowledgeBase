---
type: Concept
title: Context Engineering
description: "Context engineering — deciding what goes into a model's limited context window: instructions and rules files, retrieved knowledge, memory, tool schemas, compaction and summarisation, subagents for isolation, and progressive disclosure through skills."
resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
tags: [concept, context-engineering, prompting, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: anthropic-context
    resource: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
    title: "Effective context engineering for AI agents"
    author: "Anthropic"
---

# Context Engineering

Prompt engineering is about wording; **context engineering** is about *what information the model sees at each step*. For agents that run for many turns, context is a scarce, degrading resource: too little and the model guesses, too much and it loses focus and costs more.

## What competes for the window

| Ingredient | Techniques |
|---|---|
| Standing instructions | Short, specific rules files — `AGENTS.md`, `CLAUDE.md`, Cursor rules ([OpenCode layering](../agents/opencode/hierarchical-structure.md)) |
| Knowledge | Retrieval instead of stuffing ([RAG](rag.md), [GraphRAG](graphrag.md)); repo maps ([Aider](../agents/aider/overview.md)); code graphs ([Graphify](../memory/graphify/ai-integration.md)) |
| Memory | Only relevant facts, token-budgeted ([Agent memory](agent-memory.md), [Zep](../memory/zep/ai-integration.md) context blocks) |
| Tools | Fewer schemas, loaded on demand; [skills](agent-skills.md) instead of always-on tools; tool-output limits ([Pydantic AI](../agents/pydanticAI/overview.md) capabilities) |
| History | Compaction and summarisation (`/compact`, `/compress`), clearing old tool results |
| Sub-tasks | Subagents with their own context returning summaries ([Multi-agent orchestration](multi-agent-orchestration.md)) |

## Principles

* **Progressive disclosure** — show short descriptions, load details when needed.
* **Just-in-time retrieval** — let the agent fetch files or search rather than preloading everything.
* **Structured notes** — agents keep todo lists and notes outside the window ([Letta](../memory/letta/overview.md) memory blocks, MemFS).
* **Measure** — track token usage and quality ([LLM observability](llm-observability.md)).

## Related

[Coding agents](coding-agents.md) · [Agent memory](agent-memory.md) · [Concepts index](index.md)
