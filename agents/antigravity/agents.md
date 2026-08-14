---
type: Reference
title: Antigravity 2.0 Agents
description: Reference for Antigravity 2.0's agent orchestration model — parallel autonomous agents across independent projects, the Managed Agents API, the persistent isolated Linux sandbox, and the user-trust/verification model.
resource: Antigravity 2.0
tags: [google, antigravity, agents, orchestration, sandbox, managed-agents]
timestamp: 2026-07-09T03:28:00Z
---

# Antigravity 2.0 Agents

Antigravity 2.0 is built around **agents**, not files or editor panes. This page is the reference for how agents work in the platform.

## Orchestration model

- **Multiple autonomous agents in parallel.** Antigravity is designed to run several autonomous agents at once, each working across *independent projects*. You orchestrate them from the platform rather than driving one task at a time.
- **Independent projects.** Agents are scoped to separate projects, so parallel work does not collide in a single working tree.
- **Autonomous execution.** Agents act on their own within their sandbox; the platform's job is to let you spin up, monitor, and coordinate them.

## Managed Agents (Gemini API)

- **Managed Agents** are part of the **Gemini API** surface. They are the server-side agent primitive that Antigravity orchestrates.
- They run on Google's cloud Gemini models (default **Gemini 3.5 Flash**), so the user's local hardware (e.g. a GTX 1060) does not affect agent inference.

## Persistent isolated Linux sandbox

- Each agent works inside a **persistent, isolated Linux sandbox** provided by the Managed Agents API.
- *Isolated*: agent activity is contained away from the user's host machine.
- *Persistent*: state survives across the agent's session, enabling longer-running, multi-step work.
- The sandbox is a core part of the **trust model** — agents execute in a controlled environment you can reason about, rather than arbitrarily on your local filesystem.

## User-trust / verification model

Because Antigravity targets professional developers *and* hobbyist vibe-coders, it emphasizes a model where you can **trust** the agents you run:

- Agents run in sandboxes you can inspect rather than directly on your machine.
- Orchestration keeps agent work separated per project.
- Verification steps (see [installation.md](installation.md) and [snippets.md](snippets.md)) let you confirm an agent actually executed as expected.

> Antigravity is a newer product. The exact sandbox boundaries, permissions, and verification UI should be re-checked against official docs before asserting precise runtime behavior.

## Related

- [Overview](overview.md)
- [AI Integration](ai-integration.md)
- Cross-program: compare with the user's local-first agent stack — [OpenCode](/../../opencode/index.md), [Hermes](/../../hermes/index.md)

# Citations
[1] [Antigravity 2.0 product page](https://antigravity.google/product/antigravity-2)
[2] [Google I/O 2026 developer highlights](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/)
[3] [Antigravity — official site](https://antigravity.google/)
