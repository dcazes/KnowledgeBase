---
type: Reference
title: Hermes
description: Agent runtime (v0.20.0 / CalVer 2026.8.3 "Herald") with desktop GUI/TUI, A2A v1.0, voice/TTS, signed webhooks, and cron-based background tasks.
resource: https://hermes-agent.nousresearch.com
tags: [hermes, agent, runtime, automation, gui, tui, toolsets, a2a, voice, tts]
timestamp: 2026-08-12T00:00:00Z
---

# Hermes

Hermes Agent terminal AI (v0.20.0 / CalVer 2026.8.3 "Herald"); skills, tools, cron, delegation. Your primary local agent interface. Supports A2A v1.0 agent-to-agent, real-time voice/TTS, and signed webhooks.

## Contents

* [Overview](overview.md) - what Hermes is, architecture, skills system
* [Installation](installation.md) - setup, config, profiles
* [Configuration](configuration.md) - config.yaml, providers, models
* [Skills & Plugins](skills-plugins.md) - built-in skills, custom skills, delegation
* [Browser](browser.md) - web browsing capabilities
* [AI Integration](ai-integration.md) - SearXNG, Graphify, Firecrawl, Obsidian vault
* [Alternatives](alternatives.md) - OpenCode, OpenClaw, Cursor, Windsurf
* [Snippets](snippets.md) - common tasks cheat sheet

## Instance facts (from local config)

* **Config:** `~/.hermes/config.yaml`
* **Providers:** OpenRouter, NVIDIA NIM, local (Ollama)
* **Skills dir:** `~/.hermes/skills/`
* **Cron jobs:** defined in config, delivered via gateway

## Cross-references

* **SearXNG** — Hermes can query SearXNG for grounded web lookups — see [SearXNG AI Integration](../searxng/ai-integration.md)
* **Graphify** — first-class Graphify client; `graphify install --platform hermes` — see [Graphify AI Integration](../graphify/ai-integration.md)
* **Firecrawl** — can call Firecrawl for web extraction — see [Firecrawl AI Integration](../firecrawl/ai-integration.md)
* **Obsidian** — can read vault notes — see [Obsidian AI Integration](../obsidian/ai-integration.md)
* **AnythingLLM** — can use as RAG backend — see [AnythingLLM AI Integration](../anythingllm/ai-integration.md)
* **OpenCode / OpenClaw / Cursor / Windsurf** — fellow agent tools — see their respective docs

## Last verified

**2026-08-12** — Config, skills, and integration docs verified against local `~/.hermes/` and upstream Hermes docs. v0.20.0 / CalVer 2026.8.3 "Herald"; A2A v1.0, voice/TTS, signed webhooks.

# Citations

[1] [Hermes GitHub](https://github.com/nous-research/hermes-agent)
[2] [Hermes docs](https://hermes-agent.nousresearch.com/)