---
type: Reference
title: Space Agent
description: AI agent framework by Agent Zero (agent0ai/space-agent) — runs in the browser/frontend runtime and reshapes the workspace by building pages, tools, widgets, workflows live. Empty local dir; doc-from-upstream.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, agent0, agents, browser-runtime, skills]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: space-agent-github
    resource: "https://github.com/agent0ai/space-agent"
    title: "Space Agent GitHub"
    author: "site:github.com"
  - id: agent-zero
    resource: "https://github.com/frdel/agent-zero"
    title: "Agent Zero"
    author: "site:github.com"
---

# Space Agent

An **AI agent framework by Agent Zero** that "re-shapes the Space": the agent runs **in the browser/frontend runtime** and can build pages, tools, widgets, or workflows directly into the running workspace while you work — extending the product surface itself, not just answering inside it. Works as a personal assistant or scales to a hierarchical system of users and groups.

On this machine: `programs/spaceagent/` is **EMPTY** (no files, no checkout — verified 2026-08-12). No version number/semver upstream (repo reports 101 commits, ~1.4k stars, no release tag in README); documented from upstream only. **Not deployed.**

## Contents

* [Overview](overview.md) — what it is, browser-runtime model, SKILL.md-driven capabilities, token-efficient text protocol
* [Installation](installation.md) — desktop app (GitHub Releases) or server (`node space serve`); empty local dir note
* [Configuration](configuration.md) — user/groups, admin mode, CUSTOMWARE_PATH, supervised server
* [AI Integration](ai-integration.md) — live UI/tool building, SKILL.md system, server mode for teams, agent wiring
* [Snippets](snippets.md) — install / create user / serve / supervise cheat sheet
* [Alternatives](../alternatives.md) — OpenClaw, OpenCode, Hermes, HeyAgent vs Space Agent

## Related

* [OpenClaw](../openclaw/index.md), [OpenCode](../opencode/index.md), [Hermes](../hermes/index.md) — the other agents documented in this vault (terminal/server-side; Space Agent is browser-runtime)

## Last verified

**2026-08-13** — Local `programs/spaceagent/` empty (no checkout). Upstream `agent0ai/space-agent` (MIT, no semver) verified via web 2026-08-13. Not deployed.
