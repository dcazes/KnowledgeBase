---
type: Reference
title: Hermes — Skills, Plugins, Cron, Memory
description: How Hermes extends itself via skills (~/.hermes/skills, SKILL.md), plugins, scheduled cron jobs, and persistent memory (MEMORY.md / USER.md).
resource: https://hermes-agent.nousresearch.com
tags: [hermes, skills, plugins, cron, memory, procedural-memory]
generated: { by: "human:daniel", at: "2026-07-09T03:23:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:23:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: hermes-skills-memory-setup-note-vault
    resource: "/../../vault/03%20-%20Reference/Hermes%20Setup.md"
    title: "Hermes skills/memory — setup note (vault)"
  - id: hermes-nous-research
    resource: "https://hermes-agent.nousresearch.com"
    title: "Hermes (Nous Research)"
    author: "site:hermes-agent.nousresearch.com"
  - id: configuration
    resource: "configuration.md"
    title: "Configuration"
---

# Hermes — Skills (procedural memory)

Skills are Hermes's **procedural memory** — reusable, step-by-step procedures for recurring task types. They live in `~/.hermes/skills/` in `SKILL.md` format.

| Aspect | Detail |
|--------|--------|
| Location | `~/.hermes/skills/` |
| Format | `SKILL.md` (YAML frontmatter + procedure body) |
| Role | Procedural memory — the *how* for a task |
| Scope | Active profile; profile-scoped skills under `~/.hermes/profiles/<name>/skills/` |

A skill triggers on a task, then runs its numbered steps (often shell, file, or tool calls). Good skills carry a pitfalls section and verification steps.

Example management (CLI):

```bash
hermes setup tools          # manage toolsets (skills tool must be enabled)
```

# Plugins

Plugins extend Hermes beyond built-in skills — new tools, integrations, or capabilities. They live in `~/.hermes/plugins/` (and `~/.hermes/profiles/<name>/plugins/` for other profiles).

# Cron jobs

Scheduled/background tasks run via the **cronjob** toolset. Jobs are stored under `~/.hermes/cron/`.

```bash
# From inside Hermes (cronjob tool):
cronjob action='list'        # list scheduled jobs
```

This is what lets Hermes act as a **background daemon** rather than an interactive-only agent.

# Memory (MEMORY.md / USER.md)

Hermes keeps persistent memory as two files (profile-scoped under `~/.hermes/memories/`):

| File | Purpose |
|------|---------|
| `MEMORY.md` | Agent knowledge / durable facts |
| `USER.md` | User profile and preferences |

Controlled by `memory.memory_enabled` and `memory.user_profile_enabled` in `config.yaml` (see [Configuration](configuration.md)).

# Directory summary

```
~/.hermes/
  skills/          # procedural memory (SKILL.md)
  plugins/         # extensions / tools
  cron/            # scheduled jobs
  memories/        # MEMORY.md + USER.md (profile-scoped)
```

# Verify

```bash
ls ~/.hermes/skills/ ~/.hermes/plugins/ ~/.hermes/cron/ ~/.hermes/memories/
```
