---
type: Concept
title: VS Code Overview
description: VS Code's architecture and strengths — Electron editor, extension host, language servers, remote development (SSH, containers, WSL, tunnels), dev containers, and why it became the base for AI editors.
resource: https://code.visualstudio.com/docs
tags: [vscode, overview, extensions, remote-development]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: vscode-site
    resource: "https://code.visualstudio.com"
    title: "Visual Studio Code"
    author: "site:code.visualstudio.com"
---

# VS Code — Overview

* **Extensions** run in a separate host process; the Marketplace (and Open VSX for forks) holds tens of thousands.
* **Language Server Protocol** — VS Code introduced LSP, now used by almost every editor and by coding agents such as [OpenCode](../../agents/opencode/index.md) for diagnostics.
* **Remote development** — edit over SSH, inside containers, WSL or tunnels; **dev containers** give reproducible environments, which also make safer sandboxes for agents ([Agent security](../../concepts/agent-security.md)).
* **Open core** — Code-OSS is MIT; [Cursor](../cursor/index.md) and [Windsurf](../windsurf/index.md) build on it.

## Related

[VS Code index](index.md) · [AI features](ai-features.md)
