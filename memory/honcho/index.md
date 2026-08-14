---
type: Reference
title: Honcho
description: AI memory + user modeling (Plastic Labs) — personas, state machine for user state, insights and goals; server + Python/TS SDKs; semantic memory layer for agents.
resource: https://github.com/plastic-labs/honcho
tags: [honcho, memory, user-modeling, personas, insights]
timestamp: 2026-08-13T00:00:00Z
---

# Honcho

A **user-modeling and memory platform** (Plastic Labs) — derives and maintains a model of each user: **personas**, a **state machine** over user states, and **insights/goals** extracted from conversation. Runs as a server with Python and TypeScript SDKs; designed to give agents persistent, semantically-grounded understanding of who they're talking to.

Local checkout: `programs/honcho` (git, plastic-labs, main, commit 2026-07-21) at **v3.0.11**; Python SDK `honcho-ai` is **v2.3.0** on PyPI (checkout SDK pyproject shows **v2.2.0**). **Not deployed** as of 2026-08-13 (no running containers).

## Contents

* [Overview](overview.md) — personas, user state machine, insights/goals, workspace/agent scoping
* [Installation](installation.md) — `pip install honcho-ai` (SDK) or local checkout; server via Docker; verify
* [Configuration](configuration.md) — API keys (Anthropic/OpenAI), workspace setup, session metadata
* [AI Integration](ai-integration.md) — Python/TS SDK patterns, session init/message flow, agent wiring, vs Mem0/MemOS
* [Snippets](snippets.md) — init session / send messages / get persona / state transitions cheat sheet
* [Alternatives](alternatives.md) — Mem0, MemOS, Graphiti, Zep vs Honcho

## Related

* [Mem0](../mem0/index.md), [MemOS](../memos/index.md) — memory stores; Honcho = user modeling on top
* [Graphiti](../graphiti/index.md) — temporal facts; Honcho = user state + personas

# Citations

[1] [Honcho GitHub](https://github.com/plastic-labs/honcho)
[2] [Honcho docs](https://docs.honcho.dev)
[3] [honcho-ai on PyPI](https://pypi.org/project/honcho-ai/)

## Last verified

**2026-08-13** — Local checkout `programs/honcho` v3.0.11 (SDK honcho-ai v2.3.0 on PyPI; checkout SDK 2.2.0); not deployed. Grounded on local checkout (recon 2026-08-12) + upstream docs.
