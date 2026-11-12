---
type: Concept
title: Hermes Agent Skills & Plugins
description: Hermes skills as procedural memory — automatic skill creation, the Skills Hub, invoking skills by slash command, sharing skills with other agent harnesses — and the plugin system including agent importers and memory providers.
resource: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
tags: [hermes, skills, plugins, skills-hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hermes-docs
    resource: "https://hermes-agent.nousresearch.com/docs/"
    title: "Hermes Agent documentation"
    author: "site:hermes-agent.nousresearch.com"
---

# Hermes Agent — Skills & Plugins

## Skills

A skill is a folder with a `SKILL.md` (name, description, instructions) and optional scripts or references. Hermes:

* **creates** skills from successful work and **improves** them when they fail;
* lists them with `/skills` and runs one with `/<skill-name>`;
* shares them through the **Skills Hub**, from which other harnesses can install too (e.g. `letta skills install <path>`).

This follows the cross-tool [agent skills](../../concepts/agent-skills.md) convention also used by [Claude Code](../claude-code/index.md), [Codex](../codex/index.md), [OpenClaw](../openclaw/index.md) and [Letta](../../memory/letta/index.md).

## Plugins

`hermes plugins install <name>` adds capabilities such as `agent-importers`. Memory providers ([Honcho](../../memory/honcho/index.md), [Supermemory](../../memory/supermemory/index.md), [MemOS](../../memory/memos/index.md)) plug in via `hermes memory setup`.

## Related

[Hermes index](index.md) · [Agent skills](../../concepts/agent-skills.md)
