---
type: Software
title: Zed
description: High-performance, multiplayer code editor written in Rust by the creators of Atom and Tree-sitter — native agent panel, edit predictions, any model including local, MCP context servers, and the Agent Client Protocol for running external agents like Claude Code, Codex and Gemini CLI.
resource: https://zed.dev
tags: [zed, editor, rust, agent-client-protocol, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: zed-github
    resource: "https://github.com/zed-industries/zed"
    title: "zed-industries/zed on GitHub"
    author: "site:github.com"
  - id: zed-docs
    resource: "https://zed.dev/docs"
    title: "Zed documentation"
    author: "site:zed.dev"
  - id: acp
    resource: "https://agentclientprotocol.com"
    title: "Agent Client Protocol"
    author: "site:agentclientprotocol.com"
---

# Zed

**Zed** is a fast, GPU-rendered editor written in Rust. Its AI design is open: a built-in agent panel that works with any model (hosted, Ollama, LM Studio), and the **Agent Client Protocol (ACP)** — created by Zed — that lets *external* agents such as [Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md) or Gemini CLI run inside the editor.

| | |
|---|---|
| Category | Editors · [Coding agents](../../concepts/coding-agents.md) host |
| License | GPL-3.0-or-later (some components Apache-2.0) |
| Language | Rust |
| Latest release | v1.28.1 (2026-11-11), weekly releases |
| Platforms | macOS, Linux, Windows |

## Contents

* [Overview](overview.md) — performance, collaboration, AI design, ACP
* [Installation](installation.md)
* [Snippets](snippets.md) — settings for models, MCP and external agents
* [AI Integration](ai-integration.md) — agents, local models, tools

## Related

* Concepts: [Coding agents](../../concepts/coding-agents.md) · [MCP](../../concepts/mcp.md) · [A2A](../../concepts/a2a.md) (agent protocols)
* Peers: [VS Code](../vscode/index.md), [Cursor](../cursor/index.md), [Windsurf](../windsurf/index.md)
* Comparison: [Editors alternatives](../alternatives.md)
