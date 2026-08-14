---
type: Concept
title: Space Agent Overview
description: How Space Agent works — browser-runtime agent, live workspace reshaping (pages/tools/widgets), SKILL.md text capabilities, token-efficient protocol, hierarchy.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, overview, browser-runtime, skills]
timestamp: 2026-08-13T00:00:00Z
---

# Overview

Space Agent's premise: an agent shouldn't be trapped inside a fixed product surface — it should be able to **develop its own capabilities from within** the system and keep extending the workspace toward whatever the user wants.

## Browser-runtime model

* The agent lives **in the frontend runtime** (browser tab or desktop app) and works with the same framework, modules, and UI it reshapes — it can build new **pages, tools, widgets, or workflows live** into the running workspace.
* No separate "agent sandbox" — the workspace is both the product and the agent's working surface.

## Text-based capabilities (SKILL.md)

* New capabilities live in plain-text **`SKILL.md`** files the agent writes and extends itself — the agent bootstraps its own skillset.
* **Token-efficient**: plain text and plain JavaScript rather than bulky tool-call JSON — cheaper and faster to execute.

## Modularity & scale

* **Puzzle-piece modularity** — small core, add/remove/swap pieces.
* **Per-user work** with group sharing; **Git-backed history** for rollback ("time travel").
* **Persistent admin mode** — a stable control plane when things break.
* Scales from personal assistant to a **hierarchical system of users and groups**.

## Tech stack

Node.js/JavaScript; CLI `space` / `space.js` with `commands/params.yaml`; repo: `app/`, `server/`, `commands/`, `packaging/`, `tests/`.

## Status here

Local `programs/spaceagent/` empty; not deployed. Documented from upstream (2026-08-13).

# Citations

[1] [Space Agent GitHub](https://github.com/agent0ai/space-agent)
