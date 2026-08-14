---
type: Software
title: OpenClaw — Overview
description: Open-source personal AI assistant and self-hosted gateway connecting chat channels to models, coding agents, and skills.
resource: https://openclaw.ai/
tags: [openclaw, ai-assistant, gateway, agents, skills, automation, self-hosted]
generated: { by: "human:daniel", at: "2026-07-09T03:10:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:10:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: openclaw-official
    resource: "https://openclaw.ai/"
    title: "OpenClaw official"
    author: "site:openclaw.ai"
  - id: github
    resource: "https://github.com/openclaw/openclaw"
    title: "GitHub"
    author: "site:github.com"
  - id: docs-what-is-openclaw
    resource: "https://docs.openclaw.ai/"
    title: "Docs — what is OpenClaw"
    author: "site:docs.openclaw.ai"
---

# What OpenClaw is

OpenClaw is an **open-source personal AI assistant** — a self-hosted gateway that connects your favorite chat apps to AI models and **coding agents**. It's described as "your own personal AI assistant. Any OS. Any Platform." and is positioned as a personal/company/family/team assistant.

# Why it matters

* **Multi-channel** — one assistant reachable from Discord, Telegram, WhatsApp, Slack, Signal, Matrix, MS Teams, iMessage, Zalo, and 30+ platforms via channel plugins.
* **Agent-capable** — can connect to AI coding agents (not just chat).
* **Skills** — a growing community builds reusable skills for automation.
* **Self-hosted** — you run the gateway; your data stays with you.
* **Cross-platform** — macOS, Linux, Windows.

# How it relates to your stack

OpenClaw is the **conversational front-end / orchestrator** layer:
* It can receive requests from chat and hand them to **Hermes** or **OpenCode** (coding agents).
* It can call your tools via **MCP** (e.g. Graphify, Firecrawl, SearXNG).
* Distinct from **Dify** (app builder) and **Hermes** (the agent runtime itself).

# Editions

* **Gateway** — the core, set up via `openclaw onboard`.
* **Windows Hub** — native Windows companion app for setup, tray status, chat, node mode, and local MCP mode.
