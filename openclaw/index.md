---
type: Reference
title: OpenClaw
description: Open-source personal AI assistant and self-hosted gateway (v2026.7.1-2) connecting chat channels to models, coding agents, and skills via MCP.
resource: https://openclaw.ai/
tags: [openclaw, ai-assistant, gateway, agents, skills, automation, self-hosted]
timestamp: 2026-08-12T00:00:00Z
---

# OpenClaw

An **open-source personal AI assistant** and self-hosted gateway (stable v2026.7.1-2, 2026-08-04) that connects your chat apps (Discord, Telegram, WhatsApp, Slack, 30+) to AI models and coding agents, extended by a growing **skills** ecosystem. On this machine it can act as the multi-channel front-end that drives your agents (Hermes/OpenCode) and tools. History: Clawdbot → Moltbot → OpenClaw (Jan 2026). The CLI is `openclaw`, config at `~/.openclaw/openclaw.json`, npm package `openclaw`, Docker image `openclaw/openclaw`. Since v2026.1.29, `auth: none` is removed (CVE-2026-25253 RCE) — all gateways require auth.

## Contents

* [Overview](overview.md) - what OpenClaw is
* [Installation](installation.md) - `openclaw onboard`, Windows Hub
* [Architecture](architecture.md) - gateway, channels, skills, agents
* [AI Integration](ai-integration.md) - coding agents, MCP, your stack
* [Alternatives](alternatives.md) - n8n, LangChain, Hermes, Dify
* [Snippets](snippets.md) - cheat sheet

## Instance facts

* **Local source:** not in `programs/` (no launcher found); document from upstream.
* **Role here (intended):** channel gateway to your agents/tools; skills for automation.
* **Upstream:** openclaw.ai (open source, cross-platform).

## Cross-references

* **Hermes** — can be driven via OpenClaw skills — see [Hermes AI Integration](../hermes/ai-integration.md)
* **OpenCode** — can be driven via OpenClaw skills — see [OpenCode AI Integration](../opencode/ai-integration.md)
* **Graphify** — OpenClaw can feed results to Graphify — see [Graphify AI Integration](../graphify/ai-integration.md)
* **Dify / n8n** — alternative automation backends — see [Dify Alternatives](../dify/alternatives.md)

## Last verified

**2026-08-12** — Architecture, skills model, and integration docs verified against upstream openclaw.ai and docs.openclaw.ai. Stable v2026.7.1-2 (2026-08-04); auth:none removed (CVE-2026-25253).

# Citations

[1] [OpenClaw official](https://openclaw.ai/)
[2] [GitHub](https://github.com/openclaw/openclaw)
[3] [Docs](https://docs.openclaw.ai/)