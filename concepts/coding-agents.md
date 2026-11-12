---
type: Concept
title: Coding Agents
description: AI coding agents — how terminal and IDE agents explore, edit, test and commit; context mechanisms (rules files, repo maps, indexing, graphs); safety via permissions and sandboxes; cloud and parallel agents; evaluation; and the agents and editors in this vault.
resource: https://www.swebench.com
tags: [concept, coding-agents, ide, terminal, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: swe-bench
    resource: "https://www.swebench.com"
    title: "SWE-bench"
    author: "site:swebench.com"
  - id: aider-leaderboards
    resource: "https://aider.chat/docs/leaderboards/"
    title: "Aider LLM leaderboards"
    author: "site:aider.chat"
---

# Coding Agents

A **coding agent** works in a repository the way a developer does: reads code, plans, edits files, runs tests and commands, and iterates until the task passes — with a human reviewing the result. By 2026 they are the most widely adopted class of AI agent.

## Landscape

| Surface | Tools |
|---|---|
| Terminal | [Claude Code](../agents/claude-code/index.md), [Codex](../agents/codex/index.md), [OpenCode](../agents/opencode/index.md), [Aider](../agents/aider/index.md), [Antigravity CLI](../agents/antigravity/index.md), [Letta Code](../memory/letta/index.md), [Hermes](../agents/hermes/index.md) |
| Editors | [Cursor](../editors/cursor/index.md), [VS Code](../editors/vscode/index.md) Copilot, [Windsurf / Devin Desktop](../editors/windsurf/index.md), [Zed](../editors/zed/index.md), [Continue](../editors/continue/index.md) (archived) |
| Cloud / parallel | Codex cloud tasks, Cursor cloud agents, Devin, [Antigravity 2.0](../agents/antigravity/agents.md), Claude Code on the web |

## What makes them work

* **Context:** rules files (`AGENTS.md`, `CLAUDE.md`), repo maps ([Aider](../agents/aider/overview.md)), embeddings indexes (Cursor), code graphs ([Graphify](../memory/graphify/index.md)), LSP diagnostics (OpenCode) — see [Context engineering](context-engineering.md).
* **Tools:** file edit, search, shell, web, [MCP](mcp.md) servers ([Playwright MCP](../browsers/playwright-mcp/index.md) for UI checks).
* **Know-how:** [skills](agent-skills.md), subagents, hooks.
* **Memory across sessions:** plugins from [Honcho](../memory/honcho/ai-integration.md), [Supermemory](../memory/supermemory/ai-integration.md), [Hindsight](../memory/hindsight/ai-integration.md), [Cognee](../memory/cognee/ai-integration.md).

## Safety

Agents run commands with your permissions. Use permission rules, OS sandboxes ([Codex](../agents/codex/overview.md)), containers or dev containers, and review diffs. See [Agent security](agent-security.md).

## Choosing models

Agentic coding rewards long-context reasoning and reliable [tool calling](tool-calling.md). Benchmarks: SWE-bench (Verified, Pro), Terminal-Bench, Aider polyglot. Local models via [Ollama](../runtime/ollama/ai-integration.md) work for smaller tasks; frontier hosted models still lead on long autonomous work.

## Related

[Agents alternatives](../agents/alternatives.md) · [Editors alternatives](../editors/alternatives.md) · [Agent frameworks](agent-frameworks.md) · [Concepts index](index.md)
