---
type: Reference
title: OpenConcho
description: Fast, privacy-first desktop & web UI for self-hosted Honcho instances (offendingcommit) — browse memories/peers/sessions, chat with memory context; v0.16.0.
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, honcho, ui, memory, desktop]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: openconcho-github
    resource: "https://github.com/offendingcommit/openconcho"
    title: "OpenConcho GitHub"
    author: "site:github.com"
  - id: openconcho-github-releases
    resource: "https://github.com/offendingcommit/openconcho/releases"
    title: "OpenConcho GitHub Releases"
    author: "site:github.com"
---

# OpenConcho

A **fast, privacy-first desktop & web UI for self-hosted [Honcho](../honcho/index.md) instances** (by offendingcommit). Browse memories, peers, sessions, and conclusions — or chat with full memory context — directly against your own Honcho server. All connection details stay in the browser; nothing leaves except requests to the URL you configure.

Local checkout: `programs/openconcho` (git, offendingcommit, main, commit 2026-06-10) at **v0.16.0**; latest upstream release is **v0.16.1** (distributed via GitHub Releases binaries + Helm chart `ghcr.io/offendingcommit/charts`, not npm). Monorepo (web UI + desktop shells, Docker compose + Helm charts). **Not deployed** as of 2026-08-13.

## Contents

* [Overview](overview.md) — what it is, feature surface (dashboard, fleet, workspaces, peers, chat)
* [Installation](installation.md) — GitHub release binaries, docker-compose, Helm; verify
* [Configuration](configuration.md) — Honcho connection URL(s), multiple instances, browser-only storage
* [AI Integration](ai-integration.md) — pairing with Honcho, chat-with-memory UX, vs raw SDK
* [Snippets](snippets.md) — run / add instance / probe cheat sheet
* [Alternatives](../alternatives.md) — Honcho UI-less SDK, OpenMemory (Mem0) UI, custom dashboards

## Related

* [Honcho](../honcho/index.md) — the backend this UI talks to (v3.0.11 local checkout)
* [Mem0 → OpenMemory](../mem0/installation.md) — analogous UI for Mem0

## Last verified

**2026-08-13** — Local checkout `programs/openconcho` v0.16.0 (latest upstream release v0.16.1 via GitHub Releases/Helm — no npm package exists); not deployed. Grounded on checkout package.json/README + upstream.
