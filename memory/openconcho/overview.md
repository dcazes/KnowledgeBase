---
type: Concept
title: OpenConcho Overview
description: "What OpenConcho is — Honcho UI features: dashboard, fleet dashboard, workspaces, peers/representations, sessions, chat with memory context."
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, overview, honcho, ui]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: openconcho-github-readme
    resource: "https://github.com/offendingcommit/openconcho"
    title: "OpenConcho GitHub — README"
    author: "site:github.com"
---

# OpenConcho — Overview

OpenConcho is the **reference UI for Honcho** — you point it at your self-hosted Honcho server and get visual + conversational access to the user models Honcho maintains.

## Feature surface (from README)

| Feature | What it does |
|---|---|
| **Dashboard** | workspace count + queue status, auto-refresh every 10 s |
| **Multiple instances** | add/switch several Honcho connections |
| **Fleet dashboard** | cross-instance observability — workspaces/sessions/queue side-by-side with per-instance badges |
| **Workspaces** | paginated list with per-workspace navigation |
| **Peers** | browse peers, view representations, context, peer cards |
| **Sessions / memories / conclusions** | inspect what Honcho derived |
| **Chat** | chat with full memory context against your instance |

## Privacy model

Connection details (URLs/keys) stay **in the browser** — nothing is sent anywhere except to the Honcho URL you configure. That's the "privacy-first" claim: no telemetry/cloud middleman.

## Position

OpenConcho = Honcho's visibility layer; Honcho = the memory engine. If [Honcho](../honcho/index.md) is the memory backend, OpenConcho is how you watch/chat with it.
