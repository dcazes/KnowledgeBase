---
type: Concept
title: OpenConcho AI Integration
description: OpenConcho + Honcho — chat with full memory context, browse peer models, human-in-the-loop UX vs raw SDK; role in the agent stack.
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, integration, honcho, chat]
timestamp: 2026-08-13T00:00:00Z
---

# AI Integration

OpenConcho is the **human interface to Honcho memory** — it complements (not replaces) the [Honcho SDK](../honcho/ai-integration.md).

## Chat with memory context

The chat feature sends your messages to the configured Honcho instance with full memory context — useful for:

* debugging what Honcho knows about a user,
* manually conversing against a persona,
* inspecting conclusions/state.

## Browse derived models

* **Peers** — see each user's representations, context, peer cards.
* **Sessions / conclusions** — audit what the LLM-derived memory looks like.
* **Workspaces** — per-workspace navigation across the tenant tree.

## Role in the agent stack

* Agents use the **Honcho SDK** programmatically (memory in/out).
* Humans use **OpenConcho** to watch and steer that memory.
* Nothing here runs yet (2026-08-13) — both Honcho and OpenConcho are checkout-only.

## Analog

[OpenMemory](../mem0/installation.md) plays the same role for [Mem0](../mem0/index.md): the UI companion to the memory backend.

# Citations

[1] [OpenConcho GitHub — README](https://github.com/offendingcommit/openconcho)
[2] [Honcho docs](https://docs.honcho.dev)
