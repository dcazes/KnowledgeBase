---
type: Concept
title: OpenClaw Overview
description: What OpenClaw does — a local-first assistant reachable from your chat apps, swappable model providers and harnesses, tools, skills from ClawHub, plugins, voice and device actions, and its security model.
resource: https://docs.openclaw.ai
tags: [openclaw, overview, skills, clawhub, channels]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openclaw-docs
    resource: "https://docs.openclaw.ai"
    title: "OpenClaw documentation"
    author: "site:docs.openclaw.ai"
  - id: openclaw-github
    resource: "https://github.com/openclaw/openclaw"
    title: "openclaw/openclaw on GitHub"
    author: "site:github.com"
---

# OpenClaw — Overview

## Local-first assistant

You install OpenClaw on a computer you control. It connects to messaging services so you can ask it to do things from your phone — research, manage files, run commands, act on devices — and it keeps memory and persona files (such as `SOUL.md`, `MEMORY.md`, `USER.md`) on that machine.

## Models and harnesses

Hosted and local model providers are configurable; agent harnesses (Claude, Codex, local models) are plugins. `ollama launch openclaw` pairs it with local [Ollama](../../runtime/ollama/index.md) models.

## Skills, plugins and tools

* **Skills** in the shared `SKILL.md` format, distributed through **ClawHub** (`openclaw skills install <slug>`) — the same format [Hermes](../hermes/index.md), [Letta](../../memory/letta/index.md) and [Claude Code](../claude-code/index.md) use. See [Agent skills](../../concepts/agent-skills.md).
* **Plugins** (`openclaw plugins install …`) add memory backends, browsers and harnesses.
* **Tools** for files, shell, web and device actions; slash commands in chat.

## Security model

* Treat inbound messages as untrusted. DM-capable channels **pair** unknown senders by default (`openclaw pairing approve <channel> <code>`).
* Tools run on the host for the main session unless sandboxing is configured.
* Skills and plugins from public hubs are code you run with your permissions — review them, and never expose the Gateway publicly. See [Agent security](../../concepts/agent-security.md).

## Related

[OpenClaw index](index.md) · [Architecture](architecture.md)
