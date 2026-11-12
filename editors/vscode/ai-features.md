---
type: Concept
title: VS Code AI Features
description: AI in VS Code — GitHub Copilot completions and next-edit suggestions, chat with ask/edit/agent modes, MCP servers, custom instructions and prompt files, custom agents, language-model tools for extensions, and bring-your-own models.
resource: https://code.visualstudio.com/docs/copilot/overview
tags: [vscode, copilot, agent-mode, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: vscode-site
    resource: "https://code.visualstudio.com"
    title: "Visual Studio Code"
    author: "site:code.visualstudio.com"
  - id: vscode-updates
    resource: "https://code.visualstudio.com/updates"
    title: "VS Code release notes"
    author: "site:code.visualstudio.com"
---

# VS Code — AI Features

| Feature | Notes |
|---|---|
| Completions & next-edit suggestions | Inline predictions, including where to edit next |
| Chat modes | Ask, edit and **agent** (autonomous multi-step work with terminal and tools) |
| [MCP](../../concepts/mcp.md) | Configure servers in `.vscode/mcp.json` or user settings; tools appear in agent mode |
| Instructions | `.github/copilot-instructions.md`, `*.instructions.md`, `AGENTS.md`; prompt files (`*.prompt.md`) |
| Custom agents | Markdown-defined agents with their own tools and instructions |
| Models | Copilot-provided models; bring your own keys, including Ollama and OpenAI-compatible endpoints |
| Extension APIs | Language Model and Tools APIs let extensions contribute tools and use models |

The Copilot chat extension's source is open, so forks and extensions can build on the same agent loop.

## Related

[VS Code index](index.md) · [Workflow](workflow.md) · [Coding agents](../../concepts/coding-agents.md)
