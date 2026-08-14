---
type: Reference
title: OpenCode Hierarchical Knowledge Structure
description: The AGENTS.md/SOUL.md/TOOLS.md/USER.md/MEMORY.md pattern and IDENTITY/OPERATIONS/MEMORY folder layout for context scoping and token efficiency.
resource: https://opencode.ai/docs/context
tags: [opencode, context, knowledge-base, agenth, structure, tokens]
timestamp: 2026-07-09T03:25:00Z
---

# OpenCode Hierarchical Knowledge Structure

OpenCode works best when a project carries a hierarchical knowledge base. This pattern scopes context per folder and keeps token usage efficient.

## Core files

| File | Role |
| --- | --- |
| `AGENTS.md` | Operating instructions for the agent (how to work in this project). |
| `SOUL.md` | Agent identity, voice, and behavioral principles. |
| `TOOLS.md` | Catalog of available tools, commands, and how to invoke them. |
| `USER.md` | Facts about the user, preferences, and conventions. |
| `MEMORY.md` | Running memory — decisions, history, and lessons learned. |

## Folder layout

```
project/
├── AGENTS.md
├── SOUL.md
├── TOOLS.md
├── USER.md
├── MEMORY.md
├── IDENTITY/
│   ├── SOUL.md
│   └── USER.md
├── OPERATIONS/
│   ├── AGENTS.md
│   ├── TOOLS.md
│   └── backend/
│       ├── AGENTS.md        # nested, scopes backend context
│       └── TOOLS.md
└── MEMORY/
    ├── MEMORY.md
    └── logs/
        └── 2026-07-09.md
```

- **IDENTITY/** — houses `SOUL.md` and `USER.md` (who the agent is, who the user is).
- **OPERATIONS/** — houses `AGENTS.md` and `TOOLS.md` (how to operate here).
- **MEMORY/** — houses `MEMORY.md` plus `logs/` for dated memory entries.

## Nested files for context scoping

Place additional `AGENTS.md` / `TOOLS.md` inside subfolders (e.g. `OPERATIONS/backend/AGENTS.md`). OpenCode loads the nearest file up the tree when invoked from that directory, so you only pay tokens for the context that actually applies.

## Token efficiency

- The agent reads the most specific nested file, not the whole tree.
- Less irrelevant context = lower token cost and sharper responses.
- Use the `@` syntax (see [overview](overview.md)) to pull a specific file on demand: `opencode "@OPERATIONS/backend/TOOLS.md how do I run migrations?"`.

## Verify

```bash
# Confirm the core files exist in the project root
ls AGENTS.md SOUL.md TOOLS.md USER.md MEMORY.md
# Check nested context files
find . -name AGENTS.md -o -name TOOLS.md
```

# Citations
[1] [OpenCode Context Docs](https://opencode.ai/docs/context)
[2] [OpenCode GitHub repository (anomalyco)](https://github.com/anomalyco/opencode)
