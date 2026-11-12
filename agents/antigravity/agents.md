---
type: Concept
title: Antigravity Agents
description: How Antigravity runs agents — parallel autonomous agents per project, Managed Agents in the Gemini API with persistent isolated Linux sandboxes, and the review/verification model.
resource: https://antigravity.google/product/antigravity-2
tags: [antigravity, agents, managed-agents, sandbox]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: antigravity-2
    resource: "https://antigravity.google/product/antigravity-2"
    title: "Antigravity 2.0 product page"
    author: "site:antigravity.google"
  - id: io-2026
    resource: "https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/"
    title: "Google I/O 2026 developer highlights"
    author: "site:blog.google"
---

# Antigravity — Agents

## Orchestration

Several agents run at once, each scoped to its own project so parallel work does not collide. You start, monitor and steer them from the desktop app — the [multi-agent orchestration](../../concepts/multi-agent-orchestration.md) pattern applied to software work.

## Managed Agents and sandboxes

**Managed Agents** in the Gemini API provide agents with a **persistent, isolated Linux sandbox**: they run commands, install software and keep state across a session without touching your machine. Sandboxing is central to its trust model — compare [Codex](../codex/index.md)'s OS-level sandbox and [Claude Code](../claude-code/index.md)'s permission rules.

## Verification

Because agents act autonomously, Antigravity emphasises reviewing artefacts — plans, diffs, test results, screenshots — before accepting work. Google's own warning lists autonomous code execution, data exfiltration, prompt injection and supply-chain risks; see [Agent security](../../concepts/agent-security.md).

## Related

[Antigravity index](index.md) · [Overview](overview.md)
