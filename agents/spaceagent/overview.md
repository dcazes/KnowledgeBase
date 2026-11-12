---
type: Concept
title: Space Agent Overview
description: Space Agent's design — the agent runs in the browser layer and edits the same framework and UI it lives in, writes its own SKILL.md capabilities, acts in plain text and JavaScript, uses modular pieces, and supports users, groups, admin mode and Git-backed rollback.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, overview, self-extending, skills]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: space-agent-github
    resource: "https://github.com/agent0ai/space-agent"
    title: "agent0ai/space-agent on GitHub"
    author: "site:github.com"
---

# Space Agent — Overview

* **Browser runtime.** The agent works in the frontend (a tab or the desktop app) with the same framework, modules and UI it is changing, so new pages, widgets and workflows appear live.
* **Self-written skills.** New capabilities are `SKILL.md` files the agent writes and extends — the shared [agent skills](../../concepts/agent-skills.md) format.
* **Plain text and JavaScript instead of tool-call JSON.** Actions are expressed as JavaScript in the message, a "code as action" approach also used by [browser-use](../../browsers/browser-use/overview.md) 1.0.
* **Small core, modular pieces** that can be added, removed or swapped.
* **Users and groups.** Each user builds in their own layer; groups share tools and workflows when ready.
* **Admin mode and Git-backed history** give a stable control plane and rollback when an experiment breaks things.

## Related

[Space Agent index](index.md) · [Configuration](configuration.md)
