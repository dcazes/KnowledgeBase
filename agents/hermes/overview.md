---
type: Concept
title: Hermes Agent Overview
description: How Hermes Agent works — the self-improvement loop that turns experience into skills, persistent memory and user profiles, 40+ tools in toolsets, terminal and messaging entry points, cron scheduling, context files and the Nous Portal tool gateway.
resource: https://hermes-agent.nousresearch.com/docs/
tags: [hermes, overview, learning-loop, skills, memory]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hermes-docs
    resource: "https://hermes-agent.nousresearch.com/docs/"
    title: "Hermes Agent documentation"
    author: "site:hermes-agent.nousresearch.com"
  - id: hermes-github
    resource: "https://github.com/NousResearch/hermes-agent"
    title: "NousResearch/hermes-agent on GitHub"
    author: "site:github.com"
---

# Hermes Agent — Overview

## Entry points

* `hermes` — interactive terminal UI.
* `hermes gateway` — the same agent on Telegram, Discord, Slack, WhatsApp, Signal, email or Home Assistant, with slash commands that mirror the CLI.

## The learning loop

1. Hermes completes a task using its tools.
2. It reflects and writes (or improves) a **skill** — a reusable procedure in the shared `SKILL.md` format.
3. Next time a similar task appears it loads the skill instead of rediscovering the steps.

Skills are [procedural memory](../../concepts/agent-memory.md); they are portable to [OpenClaw](../openclaw/index.md), [Letta](../../memory/letta/index.md) and [Claude Code](../claude-code/index.md)-style harnesses. See [Skills & plugins](skills-plugins.md).

## Memory

Persistent memory and user profiles carry facts across sessions. External memory providers — [Honcho](../../memory/honcho/index.md), [Supermemory](../../memory/supermemory/index.md), [MemOS](../../memory/memos/index.md), [Hindsight](../../memory/hindsight/index.md) — can replace or extend it (`hermes memory setup`).

## Tools

40+ tools grouped into toolsets: terminal and file operations, web search and extraction, [browser](browser.md), image generation, text-to-speech, delegation to sub-agents, and any [MCP](../../concepts/mcp.md) server. Terminal commands can run locally or in isolated backends such as Docker.

## Scheduling and context

* **Cron:** scheduled tasks whose results are delivered to a chat platform.
* **Context files:** project instructions (e.g. `AGENTS.md`) shape every conversation in a working directory.
* `/compress`, `/usage`, `/insights` manage context and cost — see [Context engineering](../../concepts/context-engineering.md).

## Nous Portal

Optional subscription giving 300+ models and a Tool Gateway (web search, image generation, TTS, cloud browser) without collecting separate API keys. Bring-your-own keys remain supported per tool.

## Related

[Hermes index](index.md) · [Configuration](configuration.md) · [Agent skills](../../concepts/agent-skills.md)
