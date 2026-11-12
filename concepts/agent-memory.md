---
type: Concept
title: Agent Memory
description: How AI agents remember — working context, episodic, semantic and procedural memory; extraction, storage, retrieval and consolidation; vector, graph and self-edited designs; benchmarks like LoCoMo and LongMemEval; and the memory tools in this vault.
resource: https://arxiv.org/abs/2310.08560
tags: [concept, agent-memory, memory, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: memgpt
    resource: "https://arxiv.org/abs/2310.08560"
    title: "MemGPT: Towards LLMs as Operating Systems"
    author: "Packer et al., arXiv 2310.08560"
  - id: zep-paper
    resource: "https://arxiv.org/abs/2501.13956"
    title: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"
    author: "Rasmussen et al., arXiv 2501.13956"
---

# Agent Memory

LLMs are stateless: every call starts from the prompt. **Agent memory** is the machinery that lets an assistant remember users, past sessions and its own experience — deciding what to store, how to find it later, and what to put back into context.

## Kinds of memory

| Kind | Example | Typical store |
|---|---|---|
| Working | The current conversation and tool results | Context window ([Context engineering](context-engineering.md)) |
| Episodic | "Last Tuesday we debugged the payment webhook" | Logs, episodes, transcripts |
| Semantic | "Alice is vegetarian", "the API uses Postgres" | Fact stores, [knowledge graphs](knowledge-graphs.md) |
| Procedural | "How we deploy" | [Skills](agent-skills.md), rules files, learned workflows |

## The loop

1. **Extract** facts from interactions (LLM call, sometimes in the background).
2. **Store** with embeddings, entities, timestamps and scope (user / agent / session).
3. **Retrieve** with hybrid search (semantic + keyword + entity/graph + time).
4. **Inject** into the prompt within a token budget.
5. **Consolidate** — merge, invalidate, reflect, "dream" — so memory improves rather than bloats.

## Design families

| Design | Tools |
|---|---|
| Fact store with hybrid retrieval | [Mem0](../memory/mem0/index.md), [Supermemory](../memory/supermemory/index.md) |
| Temporal knowledge graph | [Graphiti](../memory/graphiti/index.md), [Zep](../memory/zep/index.md) |
| Reasoned models of people | [Honcho](../memory/honcho/index.md) (+ [OpenConcho](../memory/openconcho/index.md) UI) |
| Memory that learns (observations, mental models, skills) | [Hindsight](../memory/hindsight/index.md), [MemOS](../memory/memos/index.md), [Letta](../memory/letta/index.md) |
| Graph + vector pipeline | [Cognee](../memory/cognee/index.md) |
| Built into agents | [Hermes](../agents/hermes/index.md), [OpenClaw](../agents/openclaw/index.md), [LangGraph](../agents/langgraph/overview.md) stores, [Claude Code](../agents/claude-code/configuration.md) CLAUDE.md |

## Measuring it

LoCoMo, LongMemEval, BEAM and vendor suites; scores are highly sensitive to the answering model and retrieval budget — see [MemOS benchmarks](../memory/memos/benchmarks.md) and [Evals](evals.md).

## Risks

Memory can store secrets, stale facts or injected instructions that resurface later. Scope by user, allow deletion, and treat stored content as untrusted ([Agent security](agent-security.md)).

## Related

[Memory alternatives](../memory/alternatives.md) · [RAG](rag.md) · [Context engineering](context-engineering.md) · [Concepts index](index.md)
