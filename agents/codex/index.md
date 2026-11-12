---
type: Software
title: Codex
description: OpenAI's open-source coding agent — a Rust CLI plus IDE extension, desktop and cloud tasks — with OS-level sandboxing and approval policies, AGENTS.md instructions, MCP, skills, hooks and plugins; usable with a ChatGPT plan or API key.
resource: https://developers.openai.com/codex
tags: [codex, openai, coding-agents, rust, sandbox, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: codex-github
    resource: "https://github.com/openai/codex"
    title: "openai/codex on GitHub"
    author: "site:github.com"
  - id: codex-docs
    resource: "https://developers.openai.com/codex"
    title: "Codex documentation"
    author: "site:developers.openai.com"
---

# Codex

**Codex** (Codex CLI) is OpenAI's coding agent. The open-source CLI, written in Rust, runs in your terminal with a sandbox that limits what commands can touch; the same agent powers the IDE extension and Codex cloud tasks that work on repositories in parallel and open pull requests.

| | |
|---|---|
| Category | [Coding agents](../../concepts/coding-agents.md) |
| License | Apache-2.0 |
| Language | Rust |
| Latest release | rust-v0.167.2 (2026-11-11) |
| Surfaces | CLI · IDE extension (VS Code, Cursor, Windsurf) · desktop app · cloud tasks |
| Auth | Sign in with ChatGPT (Plus/Pro/Business/Edu/Enterprise) or an API key |

## Contents

* [Overview](overview.md) — sandbox and approvals, AGENTS.md, cloud tasks
* [Installation](installation.md) — installers, npm, Homebrew, binaries
* [Snippets](snippets.md) — CLI usage, `codex exec`, config.toml
* [AI Integration](ai-integration.md) — MCP, plugins and hooks, local models

## Related

* Concepts: [Coding agents](../../concepts/coding-agents.md) · [Agent security](../../concepts/agent-security.md) · [MCP](../../concepts/mcp.md) · [Agent skills](../../concepts/agent-skills.md)
* Peers: [Claude Code](../claude-code/index.md), [OpenCode](../opencode/index.md), [Aider](../aider/index.md), [Antigravity](../antigravity/index.md)
* Comparison: [Agents alternatives](../alternatives.md)
