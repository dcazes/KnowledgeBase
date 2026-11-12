---
type: Concept
title: Agent Frameworks
description: Frameworks for building AI agents — the agent loop, state and memory, tools, structured output, durability, human-in-the-loop and observability — comparing code-first libraries, vendor SDKs, harnesses and low-code platforms.
resource: https://github.com/topics/ai-agents
tags: [concept, agent-frameworks, agents, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: anthropic-building-agents
    resource: "https://www.anthropic.com/engineering/building-effective-agents"
    title: "Building effective agents"
    author: "Anthropic"
---

# Agent Frameworks

An **agent** is an LLM in a loop: it decides on actions ([tool calls](tool-calling.md)), observes results, and continues until a goal is met. **Frameworks** provide that loop plus the hard parts around it.

## What a framework should handle

| Concern | Examples |
|---|---|
| Loop and tools | Tool registration, parallel calls, retries |
| Typed outputs | [Structured output](structured-output.md) validation |
| State and memory | Message history, checkpoints, long-term stores ([Agent memory](agent-memory.md)) |
| Durability | Resume after crashes; long-running tasks |
| Human-in-the-loop | Pause for approval, edit state, resume |
| Multi-agent | Delegation, hand-off, supervisors ([Multi-agent orchestration](multi-agent-orchestration.md)) |
| Observability and evals | Traces, scores ([LLM observability](llm-observability.md), [Evals](evals.md)) |

## Options in this vault

| Style | Tools |
|---|---|
| Typed, plain Python | [Pydantic AI](../agents/pydanticAI/index.md) |
| Explicit graphs, durable | [LangGraph](../agents/langgraph/index.md) |
| Role-based crews + flows | [CrewAI](../agents/crewai/index.md) |
| Code-as-action browser agent | [browser-use](../browsers/browser-use/index.md) |
| YAML-defined | [Docker Agent](../runtime/docker/gpu-ai.md#docker-agent) |
| Low-code / visual | [Dify](../agents/dify/index.md), [n8n](../apps/n8n/index.md) |
| Agent harnesses you configure rather than code | [Claude Code](../agents/claude-code/index.md) (and Claude Agent SDK), [Hermes](../agents/hermes/index.md), [OpenClaw](../agents/openclaw/index.md), [Letta](../memory/letta/index.md) |

Also: OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, Mastra, LlamaIndex, smolagents.

## Advice

Start with the simplest thing — a single call, then a workflow with fixed steps — and add autonomy only where it measurably helps. Many "agents" are better as deterministic [workflows](workflow-automation.md) with one or two LLM decisions.

## Related

[Agents alternatives](../agents/alternatives.md) · [Coding agents](coding-agents.md) · [Concepts index](index.md)
