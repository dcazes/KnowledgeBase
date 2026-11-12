---
type: Playbook
title: Hindsight AI Integration
description: Adding Hindsight to agents — the coding-agents installer for Claude Code, Codex, Cursor, OpenCode and others, 60+ framework and no-code integrations, MCP, and the LLM wrapper.
resource: https://hindsight.vectorize.io/integrations
tags: [hindsight, integration, coding-agents, mcp, n8n, dify]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hindsight-docs
    resource: "https://hindsight.vectorize.io"
    title: "Hindsight documentation"
    author: "site:hindsight.vectorize.io"
  - id: hindsight-github
    resource: "https://github.com/vectorize-io/hindsight"
    title: "vectorize-io/hindsight on GitHub"
    author: "site:github.com"
---

# Hindsight — AI Integration

## Coding agents

```bash
npx @vectorize-io/hindsight-coding-agents install all          # every detected agent
npx @vectorize-io/hindsight-coding-agents install claude-code  # just one
```

Builds a per-repository bank automatically from git history and past sessions, injects it as the agent starts, and maintains curated pages on architecture and conventions. Supported: [Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md) CLI, Cursor CLI, GitHub Copilot CLI, [OpenCode](../../agents/opencode/index.md), Kilo, Cline, [Antigravity](../../agents/antigravity/index.md) CLI, Devin CLI and more.

A documentation [skill](../../concepts/agent-skills.md) is also available: `npx skills add https://github.com/vectorize-io/hindsight --skill hindsight-docs`.

## Frameworks and apps (60+ integrations)

* **Agent frameworks:** [LangGraph](../../agents/langgraph/index.md) / LangChain, LlamaIndex, [CrewAI](../../agents/crewai/index.md) and others.
* **No-code:** [n8n](../../apps/n8n/index.md), Zapier, [Dify](../../agents/dify/index.md), Flowise.
* **Apps:** ChatGPT, Perplexity, [Obsidian](../../tools/obsidian/index.md).

## Choosing an integration style

| Style | Control | Effort |
|---|---|---|
| LLM wrapper | Automatic recall before and retain after every call | Two lines |
| [MCP](../../concepts/mcp.md) | The agent decides when to call retain / recall / reflect | Config only |
| SDK / REST | You decide exactly what to store and when | Most code |

## Related

[Hindsight index](index.md) · [Agent memory](../../concepts/agent-memory.md) · [Memory alternatives](../alternatives.md)
