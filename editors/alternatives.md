---
type: Comparison
title: Editors Alternatives
description: Comparison of AI-capable editors — VS Code with Copilot, Cursor, Windsurf/Devin Desktop, Zed and the archived Continue extension — and how they relate to terminal coding agents.
resource: https://github.com/topics/code-editor
tags: [editors, comparison, alternatives, ai-editor]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: vscode
    resource: "https://code.visualstudio.com"
    title: "VS Code"
    author: "site:code.visualstudio.com"
  - id: cursor
    resource: "https://cursor.com"
    title: "Cursor"
    author: "site:cursor.com"
  - id: windsurf
    resource: "https://docs.devin.ai"
    title: "Windsurf / Devin Desktop"
    author: "site:docs.devin.ai"
  - id: zed
    resource: "https://zed.dev"
    title: "Zed"
    author: "site:zed.dev"
  - id: continue
    resource: "https://github.com/continuedev/continue"
    title: "Continue"
    author: "site:github.com"
---

# Editors Alternatives

| | [VS Code](vscode/index.md) | [Cursor](cursor/index.md) | [Windsurf / Devin Desktop](windsurf/index.md) | [Zed](zed/index.md) | [Continue](continue/index.md) |
|---|---|---|---|---|---|
| Type | Editor + Copilot | VS Code fork | VS Code fork | Native Rust editor | Extension (archived) |
| Open source | MIT core, open Copilot chat | No | No | GPL-3.0 | Apache-2.0 |
| Agent | Copilot agent mode | Agent + cloud agents | Devin Local + cloud Devin | Native agent + ACP external agents | Agent mode |
| Local models | BYO keys / Ollama | Limited (chat via custom endpoint) | Limited | Ollama, LM Studio | First-class |
| MCP | Yes | Yes | Yes | Yes (context servers) | Yes |
| Standout | Ecosystem, extensions | Tab + agent polish | Devin integration | Speed, ACP, collaboration | Configurability (legacy) |

Terminal agents ([Claude Code](../agents/claude-code/index.md), [Codex](../agents/codex/index.md), [OpenCode](../agents/opencode/index.md)) increasingly run *inside* these editors via extensions or ACP, so editor choice and agent choice are becoming independent.

## Decision guide

| Want | Choose |
|---|---|
| Maximum extension ecosystem, open core | [VS Code](vscode/index.md) |
| Most polished AI-first editing | [Cursor](cursor/index.md) |
| Fast native editor, bring your own agent | [Zed](zed/index.md) |
| Cognition/Devin workflows | [Windsurf / Devin Desktop](windsurf/index.md) |

## Related

[Coding agents](../concepts/coding-agents.md) · [Agents alternatives](../agents/alternatives.md) · [AI landscape](../landscape.md)
