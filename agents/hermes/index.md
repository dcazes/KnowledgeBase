---
type: Software
title: Hermes Agent
description: Self-improving open-source AI agent from Nous Research — terminal UI and messaging gateway (Telegram, Discord, Slack, WhatsApp, Signal, email), a learning loop that writes skills from experience, persistent memory, 40+ tools, MCP, cron jobs, and any model provider.
resource: https://hermes-agent.nousresearch.com
tags: [hermes, nous-research, agents, agent-skills, mcp, python, personal-assistant]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hermes-github
    resource: "https://github.com/NousResearch/hermes-agent"
    title: "NousResearch/hermes-agent on GitHub"
    author: "site:github.com"
  - id: hermes-docs
    resource: "https://hermes-agent.nousresearch.com/docs/"
    title: "Hermes Agent documentation"
    author: "site:hermes-agent.nousresearch.com"
---

# Hermes Agent

**Hermes Agent** is a general-purpose personal agent from Nous Research that you run on your own machine and talk to from a terminal or a chat app. Its distinguishing idea is a built-in **learning loop**: after completing tasks it writes and refines [skills](../../concepts/agent-skills.md) — procedural memory — so it gets better at recurring work. It is one of the most-starred agent projects of 2026.

| | |
|---|---|
| Category | [Agent frameworks](../../concepts/agent-frameworks.md) · personal agents |
| License | MIT |
| Language | Python |
| Latest release | v0.23.1 (2026-11-10) |
| Platforms | Linux, macOS, WSL2, native Windows, Android (Termux) |
| Models | Any — Nous Portal, OpenRouter, OpenAI, Anthropic, local [OpenAI-compatible](../../concepts/openai-compatible-api.md) endpoints |

## Contents

* [Overview](overview.md) — learning loop, tools, memory, gateway, cron
* [Installation](installation.md) — installers, setup wizard, Nous Portal
* [Configuration](configuration.md) — providers, toolsets, security
* [Skills & plugins](skills-plugins.md) — skills hub, plugins, importing from other agents
* [Browser](browser.md) — web and browser tools
* [Snippets](snippets.md) — CLI and slash commands
* [AI Integration](ai-integration.md) — MCP, memory providers, local models

## Related

* Concepts: [Agent skills](../../concepts/agent-skills.md) · [Agent memory](../../concepts/agent-memory.md) · [MCP](../../concepts/mcp.md) · [Agent security](../../concepts/agent-security.md)
* Peers: [OpenClaw](../openclaw/index.md), [Letta](../../memory/letta/index.md), [Claude Code](../claude-code/index.md), [OpenCode](../opencode/index.md)
* Memory plugins: [Honcho](../../memory/honcho/index.md), [Supermemory](../../memory/supermemory/index.md), [MemOS](../../memory/memos/index.md)
* Comparison: [Agents alternatives](../alternatives.md)
