---
type: Concept
title: Honcho Overview
description: Honcho's data model and reasoning loop — workspaces, peers, sessions, scopes and messages; conclusions, representations, peer cards and session context; observer/observed collections and dream consolidation.
resource: https://honcho.dev/docs/v3
tags: [honcho, overview, peers, representations, conclusions]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: honcho-github
    resource: "https://github.com/plastic-labs/honcho"
    title: "plastic-labs/honcho on GitHub"
    author: "site:github.com"
  - id: honcho-docs
    resource: "https://honcho.dev/docs/v3"
    title: "Honcho documentation (v3)"
    author: "site:honcho.dev"
---

# Honcho — Overview

## The loop

1. **Store** conversations, events, documents or tool traces as messages on a session.
2. **Reason** — Honcho processes a queue in the background and updates peer representations.
3. **Query** — ask for context, search results, representations or a natural-language answer (the chat / "dialectic" endpoint).
4. **Inject** — put the result into any LLM call or agent framework.

## Data model

| Concept | Meaning |
|---|---|
| Workspace | Top-level container that isolates data (formerly "App") |
| Peer | Any participant — human or AI agent (formerly "User") |
| Session | A conversation; many-to-many with peers |
| Scope | A named group of sessions that bounds recall |
| Message | An atomic unit: a chat message or an ingested document chunk |

Treating agents as peers too enables multi-agent sessions and **multi-peer perspective**: Honcho can model what one peer knows about another, keyed by `(observer, observed)` pairs.

## What you get back

* **Conclusions** — deductive and inductive statements Honcho has drawn about a peer.
* **Representations** — fast snapshots of what Honcho knows about a peer, optionally session-scoped.
* **Peer cards** — compact identity summaries.
* **Session context and summaries** — prompt-ready bundles for long conversations.

Background **dream** passes consolidate memories over time (viewable in [OpenConcho](../openconcho/index.md)).

## Why it is different

Honcho focuses on *understanding people* — preferences, beliefs, learning styles — a theory-of-mind angle rather than fact lookup. Plastic Labs publishes results on LongMemEval and LoCoMo on its evals page.

## Related

[Honcho index](index.md) · [Snippets](snippets.md) · [Agent memory](../../concepts/agent-memory.md)
