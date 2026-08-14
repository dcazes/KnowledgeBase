---
type: Reference
title: Antigravity 2.0
description: Google's agent-first developer platform — desktop app + CLI for orchestrating autonomous agents in parallel across projects.
resource: https://antigravity.google
tags: [antigravity, google, agents, ai-editor]
timestamp: 2026-08-12T00:00:00Z
---

# Antigravity 2.0

Antigravity 2.0 is Google's **agent-first developer platform** — a dedicated desktop application (launched around Google I/O 2026) for orchestrating multiple autonomous agents working in parallel across independent projects. It shifts the paradigm away from "an IDE with AI bolted on" toward a platform built around agent orchestration, running on Google's cloud Gemini models (default: **Gemini 3.5 Flash**).

This directory is the OKF knowledge base for the Antigravity 2.0 program. Contents are web-verified as of 2026-07-09 and grounded against official Google sources (see Citations). Antigravity is a newer product, so any runtime/feature claim should be re-verified against the official site before relying on it.

## Contents

- [Overview](overview.md) — what Antigravity 2.0 is, the agent-first model, the Gemini CLI → Antigravity CLI transition
- [Installation](installation.md) — downloading the desktop app, signing in, the Antigravity CLI
- [Agents](agents.md) — agent orchestration model, Managed Agents API, isolated Linux sandbox, trust/verification model
- [AI Integration](ai-integration.md) — Gemini models, Managed Agents API, how it relates to the rest of the user's stack
- [Alternatives](alternatives.md) — comparison vs Cursor, Windsurf, OpenCode, Claude Code, Copilot/VS Code
- [Snippets](snippets.md) — download/sign-in, CLI basics, migration-from-Gemini-CLI cheat sheet

## Instance facts

- **Not locally installed.** No Antigravity program was found in the user's `programs/` directory at time of writing. Documented from official sources only.
- **Cloud-centric.** Antigravity uses Google's cloud Gemini models. The user's local GPU (NVIDIA GTX 1060) is irrelevant to Antigravity's model execution — inference happens server-side.
- **Platform caveat.** The user runs Linux. Confirm Linux availability on the official download page (`antigravity.google/download`) before assuming a desktop build exists for this platform.
- **Migration window.** As of June 18, 2026, Gemini CLI and Gemini Code Assist IDE extensions stopped serving requests for Google AI Pro/Ultra and free Gemini Code Assist for individuals; users move to Antigravity CLI and Antigravity 2.0.

## Cross-references

* **OpenCode / Hermes** — local-first terminal agents — see [OpenCode](../opencode/index.md) & [Hermes](../hermes/index.md)
* **Cursor / Windsurf** — AI editors with agent flows — see [Cursor](../cursor/index.md) & [Windsurf](../windsurf/index.md)
* **Graphify** — could ingest Antigravity project outputs — see [Graphify AI Integration](../graphify/ai-integration.md)

## Last verified

**2026-08-12** — Version pins updated: desktop app **2.8.0**, Antigravity CLI **1.1.12**; config at `~/.gemini/config/config.json`. Docker Compose deployments are community containerizations, not official — the product is Google's hosted platform. Prior verification 2026-07-09 against official Antigravity site, Google I/O 2026 announcements, and transition blog posts.

# Citations

[1] [Antigravity — official site](https://antigravity.google/)
[2] [Antigravity 2.0 product page](https://antigravity.google/product/antigravity-2)
[3] [Google I/O 2026 developer highlights](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/)
[4] [Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)