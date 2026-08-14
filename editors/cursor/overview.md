---
type: Software
title: Cursor Overview
description: What Cursor is, why it matters as an AI-first VS Code fork, and how it fits the user's local AI editor stack.
resource: https://cursor.com/
tags: [cursor, editor, ai, vscode-fork, anysphere]
timestamp: 2026-07-09T04:00:00Z
---

# Cursor Overview

Cursor is an AI-first code editor developed by Anysphere. It is a fork of VS Code — built on the Code-OSS heritage — so it inherits VS Code's extension ecosystem, themes, and keybindings while adding AI assistance as a first-class feature rather than a bolt-on.

## Why it matters

Cursor was among the first editors to make large-language-model assistance central to the editing experience: multi-line context-aware autocomplete ("Tab"), inline natural-language editing (Cmd-K), a chat sidebar, and an autonomous Agent mode that can edit many files and run terminal commands on its own. Because it is a VS Code fork, users keep their existing workflow while gaining AI features that live inside the editor rather than in a separate chat window.

## How it fits the stack

On this machine, Cursor is one option in a broader AI-editor toolkit. The table below places it beside the other editors/agents documented in this knowledge base.

| Tool | Type | AI-first | Local model capable | Notes |
|------|------|----------|---------------------|-------|
| Cursor | VS Code fork | Yes | No (cloud) | Autonomous Agent + Background Agents |
| VSCode | Editor | Plugin | Depends | Baseline editor; Cursor's parent heritage ([VSCode](../vscode/index.md)) |
| OpenCode | CLI agent | Yes | Yes (local + cloud) | Terminal-native coding agent ([OpenCode](../../agents/opencode/index.md)) |
| Windsurf | VS Code fork | Yes | No (cloud) | Cursor competitor, "Cascade" agent ([Windsurf](../windsurf/index.md)) |
| Hermes | Agent/assistant | Yes | Yes | This assistant's own runtime ([Hermes](../../agents/hermes/index.md)) |

> **Note:** Facts in this document come from established knowledge of Cursor and its public documentation. Specific version numbers and pricing tiers were not freshly verified at write time.

## Relationship to other agents

Cursor's Agent mode overlaps conceptually with OpenCode and Claude Code: all perform autonomous multi-file edits. The distinction is that Cursor runs inside a GUI editor forked from VS Code, whereas OpenCode is a terminal CLI and Claude Code is an Anthropic CLI agent. Cursor can also expose tooling to other agents via MCP (see [AI Integration](ai-integration.md)).

# Citations

[1] [Cursor](https://cursor.com/)
[2] [Cursor Docs](https://docs.cursor.com/)
