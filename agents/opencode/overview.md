---
type: Software
title: OpenCode Overview
description: What OpenCode is — a terminal-native AI coding agent — its benefits, how it differs from Hermes, the @ context-file syntax, and supported models.
resource: https://opencode.ai/docs
tags: [opencode, ai-agent, terminal, coding]
generated: { by: "human:daniel", at: "2026-07-09T03:25:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:25:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: opencode-documentation
    resource: "https://opencode.ai/docs"
    title: "OpenCode Documentation"
    author: "site:opencode.ai"
  - id: opencode-github-repository-anomalyco
    resource: "https://github.com/anomalyco/opencode"
    title: "OpenCode GitHub repository (anomalyco)"
    author: "site:github.com"
  - id: opencode-official-site
    resource: "https://opencode.ai"
    title: "OpenCode official site"
    author: "site:opencode.ai"
---

# OpenCode Overview

OpenCode is a terminal-native, open-source AI coding agent created by SST. It runs an interactive TUI (terminal user interface) with **no background daemons**, keeps each project folder-isolated, and uses plaintext config files.

## Benefits

- **Terminal-native** — runs in your existing shell, no separate app or GUI required.
- **No background daemons** — fully supervised; you see every step the agent takes.
- **Per-project isolation** — each project gets its own config and context, avoiding cross-contamination.
- **Plaintext config** — `.opencode.json` is human-readable and version-controllable.
- **Open source** — upstream at https://github.com/anomalyco/opencode, MIT-friendly ecosystem.

## How it differs from Hermes

| Aspect | OpenCode | Hermes |
| --- | --- | --- |
| Runtime | Terminal TUI, interactive | Background daemon |
| Scope | Per-project (project root) | Global profile (`~/.hermes/`) |
| Autonomy | Supervised — see every step | Autonomous — delivers to chat |
| Output | stdout / TUI | Chat delivery |
| Invocation | Manual (`opencode`) | Scheduled cron / on-demand |
| Best for | Hands-on coding sessions | Background tasks, scheduling |

Use both: OpenCode for hands-on interactive work, Hermes for background autonomous tasks. See [the Hermes bundle](/../../hermes/index.md).

## The `@` context-file syntax

OpenCode can target context files directly with the `@` syntax. This injects the named file's content as context for the prompt:

```bash
opencode "@AGENTS.md what are the build steps?"
opencode "@USER.md @TOOLS.md how do I test this?"
opencode "@kb/graphify/graph.json find orphaned nodes"
```

This is the bridge between OpenCode and the [hierarchical knowledge structure](hierarchical-structure.md).

## Supported models

OpenCode supports a wide range of model providers:

- **Anthropic** — Claude Sonnet 4 (`anthropic/claude-sonnet-4`)
- **OpenAI** — GPT-4o (`openai/gpt-4o`)
- **Google** — Gemini 2.5 Pro (`google/gemini-2.5-pro`, ~1M context)
- **Ollama** — local models (`ollama/llama3.1`) for offline/private work
- **NVIDIA** — Nemotron (`nvidia/nemotron`)
- **OpenAI-compatible endpoints** — point the model at any `/v1` endpoint, e.g. the local `:4000` failover proxy (see [configuration](configuration.md)).

## Verify

```bash
# Confirm the installed version (expect 1.17.18 on this instance)
opencode --version
# Launch the interactive TUI
opencode
```
