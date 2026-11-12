---
type: Software
title: OpenClaw
description: Open-source personal AI assistant that runs on your own devices and answers in your chat apps — WhatsApp, Telegram, Slack, Discord, iMessage, Signal and 20+ more — with a local Gateway, swappable model harnesses, skills (ClawHub), plugins, tools and device nodes. Governed by the OpenClaw Foundation.
resource: https://openclaw.ai
tags: [openclaw, personal-assistant, agents, agent-skills, typescript, messaging]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openclaw-github
    resource: "https://github.com/openclaw/openclaw"
    title: "openclaw/openclaw on GitHub"
    author: "site:github.com"
  - id: openclaw-docs
    resource: "https://docs.openclaw.ai"
    title: "OpenClaw documentation"
    author: "site:docs.openclaw.ai"
  - id: openclaw-site
    resource: "https://openclaw.ai"
    title: "OpenClaw website"
    author: "site:openclaw.ai"
---

# OpenClaw

**OpenClaw** (the "lobster" assistant) is a self-hosted assistant you message like a person. State, memory and credentials stay on your hardware; models and agent harnesses — Claude, Codex, local models — are plugins you can swap. It became one of the fastest-growing open-source projects of 2026 and is now run by the independent, non-profit OpenClaw Foundation.

| | |
|---|---|
| Category | Personal agents · [Agent frameworks](../../concepts/agent-frameworks.md) |
| License | MIT |
| Language | TypeScript (Node 24.16+ or 26.1+) |
| Latest release | v2026.11.3 (2026-11-10) — calendar versioning |
| Channels | WhatsApp, Telegram, Slack, Discord, Teams, Google Chat, Signal, iMessage and 20+ more |

## Contents

* [Overview](overview.md) — what it is, channels, models, skills, security model
* [Architecture](architecture.md) — Gateway, Control UI, channels, nodes
* [Installation](installation.md) — installer, npm, onboarding
* [Snippets](snippets.md) — CLI cheat sheet
* [AI Integration](ai-integration.md) — memory plugins, browsers, local models

## Related

* Concepts: [Agent skills](../../concepts/agent-skills.md) · [Agent security](../../concepts/agent-security.md) · [Agent memory](../../concepts/agent-memory.md)
* Peers: [Hermes](../hermes/index.md), [Letta](../../memory/letta/index.md), [Space Agent](../spaceagent/index.md)
* Plugins: [Honcho](../../memory/honcho/ai-integration.md), [MemOS](../../memory/memos/ai-integration.md), [Cognee](../../memory/cognee/ai-integration.md), [Supermemory](../../memory/supermemory/ai-integration.md), [Camofox](../../browsers/camofox/index.md)
* Comparison: [Agents alternatives](../alternatives.md)
