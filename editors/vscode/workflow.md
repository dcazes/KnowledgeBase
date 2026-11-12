---
type: Playbook
title: VS Code AI Workflow
description: A practical AI workflow in VS Code — combining Copilot agent mode with Claude Code or Codex extensions, MCP tools, instructions files, dev containers for isolation, and reviewing agent changes.
resource: https://code.visualstudio.com/docs
tags: [vscode, workflow, agents, dev-containers]
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

# VS Code — AI Workflow

1. **Context first.** Keep an `AGENTS.md` (and Copilot instructions) describing build, test and conventions — shared by most agents ([Context engineering](../../concepts/context-engineering.md)).
2. **Pick the agent per task.** Copilot agent mode for quick edits; [Claude Code](../../agents/claude-code/index.md) or [Codex](../../agents/codex/index.md) extensions for longer autonomous work.
3. **Add tools via MCP.** [Playwright MCP](../../browsers/playwright-mcp/index.md) for UI checks, [Graphify](../../memory/graphify/index.md) for structure, a memory server for continuity.
4. **Isolate.** Run agents in a dev container or remote environment when they execute commands ([Agent security](../../concepts/agent-security.md)).
5. **Review.** Use the diff view and source control panel; keep commits small.

## Related

[VS Code index](index.md) · [Snippets](snippets.md)
