---
type: Concept
title: Zed Overview
description: What makes Zed different — Rust and GPU rendering, Tree-sitter and LSP, real-time collaboration, the agent panel with tool permissions and rules, edit predictions, MCP context servers, and the Agent Client Protocol for external agents.
resource: https://zed.dev/docs
tags: [zed, overview, acp, agent-panel]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: zed-docs
    resource: "https://zed.dev/docs"
    title: "Zed documentation"
    author: "site:zed.dev"
  - id: acp
    resource: "https://agentclientprotocol.com"
    title: "Agent Client Protocol"
    author: "site:agentclientprotocol.com"
---

# Zed — Overview

* **Speed.** Rust, GPU-accelerated UI, Tree-sitter parsing and LSP — the creators of Atom and Tree-sitter rebuilt the editor for performance.
* **Collaboration.** Shared projects, cursors and voice channels built in.
* **Agent panel.** An agentic assistant with tools (edit, terminal, search, fetch), per-tool permissions, rules files (`AGENTS.md`, `.rules`) and threads.
* **Edit predictions.** Next-edit suggestions from Zed's open model or other providers.
* **[MCP](../../concepts/mcp.md) context servers** extend the agent with tools.
* **Agent Client Protocol (ACP).** A JSON-RPC protocol between editors and coding agents — the editor-to-agent counterpart of MCP's agent-to-tool link. External agents (Claude Code, Codex, Gemini CLI and others) render their work in Zed's UI; other editors have adopted ACP too.

## Related

[Zed index](index.md) · [AI Integration](ai-integration.md)
