---
type: Software
title: Hermes — Overview
description: Agent runtime (desktop GUI/TUI) for autonomous and background tasks using terminal, file, browser, code, skills, cron, and more.
resource: https://hermes-agent.nousresearch.com
tags: [hermes, agent, runtime, automation, gui, tui, toolsets]
timestamp: 2026-07-09T03:20:00Z
---

# What Hermes is

Hermes is an **agent runtime** with a desktop GUI and TUI. It executes tasks autonomously and in the background, drawing on a broad toolset: terminal, file, browser, code execution, computer use, context engine, skills, cron, delegation, and web. It is the agent behind this conversation.

# Runtime model

* **Desktop GUI** — graphical chat surface (this app).
* **TUI / CLI** — terminal interface (`hermes`); some commands are CLI-only (e.g. `/browser connect`).
* **Background daemon** — unlike interactive-only agents, Hermes can run scheduled/background tasks (via `cronjob`).

# Toolsets

Enabled on this machine (from the setup note): `browser`, `clarify`, `code_execution`, `computer_use`, `context_engine`, `cronjob`, `delegation`, `file`, `image_gen`, `memory`, `session_search`, `skills`, `terminal`, `todo`, `web`.

Disabled: `coding`, `discord`, `discord_admin`, `feishu_*`, `homeassistant`, `kanban`, `project`, `search`, `spotify`, `tts`, `video`, `video_gen`, `vision`, `x_search`, `yuanbao`.

# How it fits your stack

| Role | Tool |
|------|------|
| Autonomous/background agent | **Hermes** |
| Interactive coding agent | OpenCode |
| Multi-channel front-end | OpenClaw |
| App builder | Dify |
| Chat UIs | OpenWebUI / AnythingLLM |

Hermes can drive **Camofox** (browser), and call **SearXNG / Firecrawl / Graphify** (tools/skills).

# Citations

[1] [Hermes (Nous Research)](https://hermes-agent.nousresearch.com)
[2] [Setup note (toolsets)](/../../vault/03%20-%20Reference/Hermes%20Setup.md)
