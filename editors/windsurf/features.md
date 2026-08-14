---
type: Reference
title: Windsurf — Features
description: Windsurf (now Devin Desktop) agentic coding features — Cascade assistant (retired Jul 2026 → Devin Local), SWE-1 models, flows, command mode, and multi-file edits.
resource: https://docs.windsurf.com/
tags: [windsurf, cascade, swe-1, flows, agentic, features]
generated: { by: "human:daniel", at: "2026-07-09T03:32:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:32:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: windsurf-features-docs
    resource: "https://docs.windsurf.com/"
    title: "Windsurf features/docs"
    author: "site:docs.windsurf.com"
  - id: overview
    resource: "overview.md"
    title: "Overview"
---

# Windsurf (now Devin Desktop) — Core features

* **Cascade** (retired Jul 2026; now **Devin Local**) — the agentic assistant. Chat with it to plan and apply changes; it can read the codebase, run commands, and make coordinated multi-file edits. Operates in a "write" or "chat" mode and can take autonomous steps within guardrails.
* **SWE-1 models** — Codeium's software-engineering models, tuned for coding reasoning and edits (vs. general chat models). Used by Cascade for agentic flows.
* **Flows** — combine a command + AI into a reusable action, so repetitive workflows (e.g. "add a test for this function") become one-step operations.
* **Command mode** — drive edits with natural-language commands; Windsurf applies them in-place.
* **Codebase indexing** — Cascade builds awareness of your project so suggestions/edits fit existing structure.
* **Multi-file coordination** — edits span several files coherently (not just single-file snippets).

# Typical workflow

1. Open a repo (e.g. `programs/firecrawl/firecrawl`).
2. Ask Cascade: "Refactor the API client to use the new endpoint."
3. Review the multi-file diff; accept/iterate.
4. Save a Flow for the recurring pattern.

# Notes

Verify current Cascade/SWE-1 capabilities against docs.windsurf.com — model names and feature specifics evolve quickly.
