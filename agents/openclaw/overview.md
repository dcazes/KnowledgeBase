---
type: Software
title: OpenClaw — Overview
description: Open-source personal AI assistant and self-hosted gateway connecting chat channels to models, coding agents, and skills.
resource: https://openclaw.ai/
tags: [openclaw, ai-assistant, gateway, agents, skills, automation, self-hosted]
timestamp: 2026-07-09T03:10:00Z
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

# Citations

[1] [OpenClaw official](https://openclaw.ai/)
[2] [GitHub](https://github.com/openclaw/openclaw)
[3] [Docs — what is OpenClaw](https://docs.openclaw.ai/)
