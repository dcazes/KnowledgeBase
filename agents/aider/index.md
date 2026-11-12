---
type: Software
title: Aider
description: Pioneering open-source AI pair-programming tool for the terminal — edits files in your git repo with any model, builds a tree-sitter repository map for context, commits every change, and maintains the widely cited Aider polyglot coding leaderboard.
resource: https://aider.chat
tags: [aider, coding-agents, terminal, git, repo-map, python]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: aider-github
    resource: "https://github.com/Aider-AI/aider"
    title: "Aider-AI/aider on GitHub"
    author: "site:github.com"
  - id: aider-docs
    resource: "https://aider.chat/docs/"
    title: "Aider documentation"
    author: "site:aider.chat"
  - id: aider-leaderboards
    resource: "https://aider.chat/docs/leaderboards/"
    title: "Aider LLM leaderboards"
    author: "site:aider.chat"
---

# Aider

**Aider** was one of the first practical terminal coding assistants (2023) and introduced ideas now everywhere: a **repository map** so the model sees the shape of the whole codebase, automatic **git commits** for every AI change, and pluggable **edit formats**. Its polyglot benchmark leaderboard remains a common reference for comparing models on code editing.

| | |
|---|---|
| Category | [Coding agents](../../concepts/coding-agents.md) |
| License | Apache-2.0 |
| Language | Python (`aider-chat`) |
| Latest release | aider-chat 0.86.2 on PyPI (2026-02); development has slowed markedly since 2025 |
| Models | Any — Anthropic, OpenAI, Gemini, DeepSeek, OpenRouter, local via Ollama or OpenAI-compatible APIs |

## Contents

* [Overview](overview.md) — repo map, edit formats, chat modes, git workflow
* [Installation](installation.md) — aider-install, pipx/uv, Docker
* [Snippets](snippets.md) — commands and flags
* [AI Integration](ai-integration.md) — models, local inference, where it fits in 2026

## Related

* Concepts: [Coding agents](../../concepts/coding-agents.md) · [Context engineering](../../concepts/context-engineering.md) · [Evals](../../concepts/evals.md)
* Peers: [Claude Code](../claude-code/index.md), [Codex](../codex/index.md), [OpenCode](../opencode/index.md), [Continue](../../editors/continue/index.md)
* Comparison: [Agents alternatives](../alternatives.md)
