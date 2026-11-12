---
type: Concept
title: Aider Overview
description: How Aider works — the tree-sitter repository map, edit formats (whole, diff, udiff, architect/editor), chat modes, automatic git commits, lint and test loops, watch mode with AI comments, and its benchmark leaderboard.
resource: https://aider.chat/docs/
tags: [aider, overview, repo-map, edit-formats, git]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: aider-docs
    resource: "https://aider.chat/docs/"
    title: "Aider documentation"
    author: "site:aider.chat"
  - id: aider-leaderboards
    resource: "https://aider.chat/docs/leaderboards/"
    title: "Aider LLM leaderboards"
    author: "site:aider.chat"
---

# Aider — Overview

## Repository map

Aider parses the repo with tree-sitter, ranks symbols by how connected they are, and sends a compact map of the most relevant classes and functions with each request — an early, influential piece of [context engineering](../../concepts/context-engineering.md) for code. Files you `/add` are sent in full; the rest is represented by the map.

## Edit formats

| Format | How the model edits |
|---|---|
| `whole` | Returns entire files |
| `diff` | Search/replace blocks |
| `udiff` | Unified diffs |
| Architect mode | A strong "architect" model plans; a cheaper "editor" model writes the edits |

## Workflow

* Every change becomes a git commit with a generated message; `/undo` reverts it.
* `/lint` and `/test` (or auto-lint/auto-test) feed failures back to the model.
* **Watch mode** (`--watch-files`): write `# ... AI!` comments in your editor and Aider acts on them.
* Chat modes: `code`, `ask`, `architect`, `help`.

## Leaderboards

The Aider polyglot benchmark (225 Exercism exercises across six languages) measures whether a model can edit code correctly — useful when choosing models for any coding agent. See [Evals](../../concepts/evals.md).

## Status

Aider is stable and still usable, but releases have been infrequent since late 2025 while [Claude Code](../claude-code/index.md), [Codex](../codex/index.md) and [OpenCode](../opencode/index.md) added agentic features (subagents, MCP, skills) that Aider lacks.

## Related

[Aider index](index.md) · [Snippets](snippets.md)
