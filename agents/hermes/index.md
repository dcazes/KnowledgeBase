---
type: Reference
title: Hermes
description: Agent runtime (v0.20.0 / CalVer 2026.8.3 "Herald") with desktop GUI/TUI, A2A v1.0, voice/TTS, signed webhooks, and cron-based background tasks.
resource: https://hermes-agent.nousresearch.com
tags: [hermes, agent, runtime, automation, gui, tui, toolsets, a2a, voice, tts]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: hermes-github
    resource: "https://github.com/nous-research/hermes-agent"
    title: "Hermes GitHub"
    author: "site:github.com"
  - id: hermes-docs
    resource: "https://hermes-agent.nousresearch.com/"
    title: "Hermes docs"
    author: "site:hermes-agent.nousresearch.com"
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

* **SearXNG** — Hermes can query SearXNG for grounded web lookups — see [SearXNG AI Integration](../../runtime/searxng/ai-integration.md)
* **Graphify** — first-class Graphify client; `graphify install --platform hermes` — see [Graphify AI Integration](../../memory/graphify/ai-integration.md)
* **Firecrawl** — can call Firecrawl for web extraction — see [Firecrawl AI Integration](../../browsers/firecrawl/ai-integration.md)
* **Obsidian** — can read vault notes — see [Obsidian AI Integration](../../tools/obsidian/ai-integration.md)
* **AnythingLLM** — can use as RAG backend — see [AnythingLLM AI Integration](../../apps/anythingllm/ai-integration.md)
* **OpenCode / OpenClaw / Cursor / Windsurf** — fellow agent tools — see their respective docs

## Last verified

**2026-08-12** — Config, skills, and integration docs verified against local `~/.hermes/` and upstream Hermes docs. v0.20.0 / CalVer 2026.8.3 "Herald"; A2A v1.0, voice/TTS, signed webhooks.
