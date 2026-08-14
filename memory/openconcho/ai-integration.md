---
type: Concept
title: OpenConcho AI Integration
description: OpenConcho + Honcho — chat with full memory context, browse peer models, human-in-the-loop UX vs raw SDK; role in the agent stack.
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, integration, honcho, chat]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: openconcho-github-readme
    resource: "https://github.com/offendingcommit/openconcho"
    title: "OpenConcho GitHub — README"
    author: "site:github.com"
  - id: honcho-docs
    resource: "https://docs.honcho.dev"
    title: "Honcho docs"
    author: "site:docs.honcho.dev"
---

# OpenConcho — AI Integration

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
