---
type: Reference
title: VSCode
description: Free open-source AI code editor (VS Code / Code-OSS) — the editor for programs/* repos and agent-skill authoring, with Copilot, Agent Mode, and Agent Host architecture.
resource: https://code.visualstudio.com/
tags: [vscode, editor, ide, code-oss, ai, copilot, development]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: vs-code-official-site
    resource: "https://code.visualstudio.com/"
    title: "VS Code official site"
    author: "site:code.visualstudio.com"
  - id: local-launcher-programs-vscode-desktop
    resource: "/../../programs/VSCode.desktop"
    title: "Local launcher - programs/VSCode.desktop"
---

# VSCode

A free, **open-source AI code editor** (Microsoft's VS Code, built on the Code-OSS core). On this machine it's the editor for your `programs/*` repositories (Dify, Firecrawl, SearXNG, etc.) and for writing agent skills (Graphify/Hermes/OpenCode). Launched via the `code` command. As of v1.130, VS Code ships a dedicated **Agent Host** architecture (AHP protocol, assisted tool approvals, worktree isolation for Claude/Codex) — AI is built-in via Copilot + agent host, not just a plugin.

## Contents

* [Overview](overview.md) - what VSCode is, architecture, editions
* [Installation](installation.md) - install + launch via `code`, CLI flags
* [AI Features](ai-features.md) - Copilot, Agent Mode, chat, MCP
* [Workflow](workflow.md) - editing programs/* repos and authoring agent skills
* [Alternatives](alternatives.md) - Cursor, Neovim, JetBrains, Zed
* [Snippets](snippets.md) - cheat sheet

## Instance facts (this machine)

* **Launcher:** `programs/VSCode.desktop` → `Exec=code`
* **Binary:** `/usr/bin/code` present; `node` at `~/.local/bin/node`
* **Role:** editor for `programs/*` source + agent-skill authoring

## Cross-references

* **Cursor** — Anysphere's fork; similar AI features — see [Cursor Overview](../cursor/overview.md)
* **Windsurf (now Devin Desktop)** — Cognition's AI editor; fork of VSCode — see [Windsurf Overview](../windsurf/overview.md)
* **OpenCode** — terminal agent; shares model config — see [OpenCode Overview](../../agents/opencode/overview.md)
* **Graphify** — VSCode can use Graphify MCP server — see [Graphify MCP Server](../../memory/graphify/mcp-server.md)
* **Hermes** — terminal agent; can read VSCode workspace — see [Hermes Overview](../../agents/hermes/overview.md)
* **Obsidian** — VSCode can edit vault `.md` files — see [Obsidian Overview](../../tools/obsidian/overview.md)
* **Dify / Firecrawl / SearXNG** — source repos live under `programs/` — see respective docs

## Last verified

**2026-08-12** — Launcher, binary location, and AI feature docs verified against upstream code.visualstudio.com. VS Code v1.133 (2026-08-12); Agent Host architecture (AHP protocol) since v1.130.
