---
type: Concept
title: Codex Overview
description: How Codex works — sandbox modes (read-only, workspace-write, full access) enforced by the OS, approval policies, AGENTS.md project instructions, cloud tasks that produce pull requests, and the shared agent across CLI, IDE and cloud.
resource: https://developers.openai.com/codex
tags: [codex, overview, sandbox, approvals, agents-md]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: codex-docs
    resource: "https://developers.openai.com/codex"
    title: "Codex documentation"
    author: "site:developers.openai.com"
  - id: codex-github
    resource: "https://github.com/openai/codex"
    title: "openai/codex on GitHub"
    author: "site:github.com"
---

# Codex — Overview

## Sandbox and approvals

Codex separates **what commands may do** from **when it asks you**:

| Sandbox mode | Effect |
|---|---|
| `read-only` | Can read files, cannot write or use the network |
| `workspace-write` | Can write inside the project; network off by default |
| `danger-full-access` | No restrictions — only inside an external sandbox |

The sandbox uses OS mechanisms (Seatbelt on macOS, Landlock/seccomp on Linux, a restricted token on Windows). **Approval policies** (e.g. ask on request or on failure, never) decide when Codex pauses for confirmation. This is one of the clearest designs for [agent security](../../concepts/agent-security.md) among coding agents.

## Instructions

Codex reads `AGENTS.md` files (global, repo root and subdirectories) — the convention it helped popularise, now shared by [OpenCode](../opencode/index.md), [Cursor](../../editors/cursor/index.md), [Zed](../../editors/zed/index.md) and others. See [Context engineering](../../concepts/context-engineering.md).

## Cloud tasks

From the CLI, IDE or ChatGPT you can delegate tasks to cloud containers that clone the repo, work in parallel and return diffs or pull requests.

## Related

[Codex index](index.md) · [Snippets](snippets.md) · [Coding agents](../../concepts/coding-agents.md)
