---
type: Comparison
title: Agents Alternatives
description: Comparison of agents and agent frameworks — coding agents (Claude Code, Codex, OpenCode, Aider, Antigravity), personal agents (Hermes, OpenClaw, Space Agent), code frameworks (Pydantic AI, LangGraph, CrewAI) and low-code platforms (Dify) — with a decision guide.
resource: https://github.com/topics/ai-agents
tags: [agents, comparison, alternatives, coding-agents, agent-frameworks]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: claude-code
    resource: "https://code.claude.com"
    title: "Claude Code"
    author: "site:code.claude.com"
  - id: codex
    resource: "https://github.com/openai/codex"
    title: "Codex"
    author: "site:github.com"
  - id: opencode
    resource: "https://github.com/anomalyco/opencode"
    title: "OpenCode"
    author: "site:github.com"
  - id: aider
    resource: "https://github.com/Aider-AI/aider"
    title: "Aider"
    author: "site:github.com"
  - id: antigravity
    resource: "https://antigravity.google"
    title: "Antigravity"
    author: "site:antigravity.google"
  - id: hermes
    resource: "https://github.com/NousResearch/hermes-agent"
    title: "Hermes Agent"
    author: "site:github.com"
  - id: openclaw
    resource: "https://github.com/openclaw/openclaw"
    title: "OpenClaw"
    author: "site:github.com"
  - id: pydantic-ai
    resource: "https://github.com/pydantic/pydantic-ai"
    title: "Pydantic AI"
    author: "site:github.com"
  - id: langgraph
    resource: "https://github.com/langchain-ai/langgraph"
    title: "LangGraph"
    author: "site:github.com"
  - id: crewai
    resource: "https://github.com/crewAIInc/crewAI"
    title: "CrewAI"
    author: "site:github.com"
  - id: dify
    resource: "https://github.com/langgenius/dify"
    title: "Dify"
    author: "site:github.com"
---

# Agents Alternatives

This category spans three different things people call "agents": **products that act for you** (coding and personal agents), **frameworks for building agents**, and **platforms for assembling them visually**.

## Coding agents

| | [Claude Code](claude-code/index.md) | [Codex](codex/index.md) | [OpenCode](opencode/index.md) | [Antigravity](antigravity/index.md) | [Aider](aider/index.md) |
|---|---|---|---|---|---|
| Vendor | Anthropic | OpenAI | Community (Anomaly) | Google | Community |
| Open source | No | Apache-2.0 | MIT | No | Apache-2.0 |
| Models | Claude (+ gateways) | OpenAI (+ profiles) | Any, incl. local | Gemini | Any, incl. local |
| Safety model | Permission rules, hooks, sandboxed bash | OS sandbox + approval policies | Permission rules | Managed sandboxes | Git commits, manual review |
| Extensibility | Skills, subagents, hooks, MCP, plugins | AGENTS.md, MCP, skills, hooks, plugins | Agents, commands, MCP, plugins | MCP, settings | Minimal |
| Standout | Ecosystem depth | Sandbox design, cloud tasks | Freedom of model | Parallel agent orchestration | Repo map, git discipline |

Also notable: GitHub Copilot agent/CLI, Cursor and Windsurf agents ([Editors](../editors/alternatives.md)), Kilo Code, Cline, Amp, Goose, [Letta](../memory/letta/index.md) Code.

## Personal agents

| | [Hermes](hermes/index.md) | [OpenClaw](openclaw/index.md) | [Space Agent](spaceagent/index.md) |
|---|---|---|---|
| Interface | Terminal + chat apps | Chat apps + Control UI + device nodes | Self-modifying web workspace |
| Distinctive | Learning loop writes skills | 20+ channels, foundation-governed, huge plugin ecosystem | Builds UI and tools into itself |
| Language | Python | TypeScript | JavaScript |

## Frameworks and platforms

| | [Pydantic AI](pydanticAI/index.md) | [LangGraph](langgraph/index.md) | [CrewAI](crewai/index.md) | [Dify](dify/index.md) |
|---|---|---|---|---|
| Style | Typed Python agent loop | Explicit state graphs | Role-based crews + flows | Visual canvas |
| Durable / resumable | Via integrations | Checkpointers (core) | Flows state | Platform-managed |
| Best for | Type-safe apps, structured output | Complex, long-running, human-in-the-loop | Fast multi-agent prototypes | Mixed teams, RAG apps |

Others: OpenAI Agents SDK, Claude Agent SDK, Google ADK, Microsoft Agent Framework (AutoGen + Semantic Kernel), Mastra (TypeScript), LlamaIndex agents, smolagents, Agno.

## Decision guide

| Want to… | Choose |
|---|---|
| Ship code faster in your repo | [Claude Code](claude-code/index.md), [Codex](codex/index.md) or [OpenCode](opencode/index.md) (local models) |
| An assistant you message from your phone | [OpenClaw](openclaw/index.md) or [Hermes](hermes/index.md) |
| Build a production agent in Python | [Pydantic AI](pydanticAI/index.md) or [LangGraph](langgraph/index.md) |
| Prototype a multi-agent team quickly | [CrewAI](crewai/index.md) |
| Let non-developers build LLM apps | [Dify](dify/index.md) |

## Related

[Coding agents](../concepts/coding-agents.md) · [Agent frameworks](../concepts/agent-frameworks.md) · [Multi-agent orchestration](../concepts/multi-agent-orchestration.md) · [AI landscape](../landscape.md)
