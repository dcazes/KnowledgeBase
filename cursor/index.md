---
type: Reference
title: Cursor
description: AI-first code editor by Anysphere — a VS Code fork with inline chat, Agent mode, Background Agents, and MCP support. Closed-source SaaS (docs repo only).
resource: https://cursor.com/
tags: [cursor, editor, ai, vscode-fork, anysphere]
timestamp: 2026-08-12T00:00:00Z
---

# Cursor

Cursor is an AI-first code editor built by Anysphere. It is a fork of VS Code (Code-OSS heritage), which means the familiar extensions, themes, and keybindings carry over, but the editor is rebuilt around AI assistance: inline chat, context-aware autocomplete, an autonomous Agent mode, and cloud-based Background Agents. Cursor is a closed-source SaaS product (docs repo only); releases are changelog-dated with no public numeric versioning.

This knowledge base section documents what Cursor is, how to install it, its core features, how it integrates with AI models and the Model Context Protocol (MCP), how it compares to alternatives, and practical snippets for daily use.

## Contents

- [Overview](overview.md) — what Cursor is, why it matters, and how it fits the local stack.
- [Installation](installation.md) — download, sign in, and verify.
- [Features](features.md) — Tab completion, Cmd-K, Chat, Agent mode, Background Agents, Bugbot, model support, Privacy Mode.
- [AI Integration](ai-integration.md) — MCP support and the relationship to other stack agents/editors.
- [Alternatives](alternatives.md) — Cursor vs Windsurf, VSCode, OpenCode, Zed, Claude Code.
- [Snippets](snippets.md) — quick-start, Agent mode usage, MCP config, cheat sheet.

## Instance facts

- **Locally installed:** No. No launcher was found in the machine's programs list. This section is documented from upstream sources, not a live local instance.
- **Architecture:** A fork of VS Code (Code-OSS heritage). Extensions and keybindings carry over.
- **Models:** Cloud-hosted. Supports Claude, GPT-4o/mini, and custom/OpenAI-compatible endpoints.
- **Companions in this stack:** documented alongside [VSCode](../vscode/index.md), [OpenCode](../opencode/index.md), [Windsurf](../windsurf/index.md), [Hermes](../hermes/index.md), and the [Graphify MCP server](../graphify/mcp-server.md).

## Cross-references

* **VSCode** — Cursor's upstream; similar extension ecosystem — see [VSCode Overview](../vscode/overview.md)
* **Windsurf (now Devin Desktop)** — Cognition's AI editor with Devin Local agent — see [Windsurf Overview](../windsurf/overview.md)
* **OpenCode** — terminal-native agent; different UX paradigm — see [OpenCode Overview](../opencode/overview.md)
* **Graphify** — Cursor can use Graphify MCP server — see [Graphify MCP Server](../graphify/mcp-server.md)
* **Hermes** — terminal agent that can share context — see [Hermes Overview](../hermes/overview.md)

## Last verified

**2026-08-12** — All feature descriptions and integration notes verified against upstream docs.cursor.com and Cursor changelog. Recent: Cursor Router (07-22), Cursor Start India plan (07-28), iPad + PR review (07-29), Google Workspace plugins (08-03).

# Citations

[1] [Cursor](https://cursor.com/)
[2] [Cursor Docs](https://docs.cursor.com/)