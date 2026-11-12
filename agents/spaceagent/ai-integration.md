---
type: Playbook
title: Space Agent AI Integration
description: Using Space Agent with hosted or local models, porting SKILL.md capabilities to and from other harnesses, and how its self-extending workspace compares with OpenClaw, Hermes and low-code builders.
resource: https://github.com/agent0ai/space-agent
tags: [space-agent, integration, skills, comparison]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: space-agent-github
    resource: "https://github.com/agent0ai/space-agent"
    title: "agent0ai/space-agent on GitHub"
    author: "site:github.com"
---

# Space Agent — AI Integration

* **Models:** configure a hosted provider or an [OpenAI-compatible](../../concepts/openai-compatible-api.md) local server such as [Ollama](../../runtime/ollama/index.md) or [LiteLLM](../../runtime/litellm/index.md). Generating working UI code needs a strong coding model.
* **Skills:** `SKILL.md` files follow the same convention as [Hermes](../hermes/skills-plugins.md), [OpenClaw](../openclaw/overview.md) and [Claude Code](../claude-code/configuration.md), so procedures can move between them.
* **Compared with:** [OpenClaw](../openclaw/index.md) and [Hermes](../hermes/index.md) (chat-first assistants), [Dify](../dify/index.md) and [n8n](../../apps/n8n/index.md) (humans build the workflows). Space Agent's agent builds the app itself.

## Related

[Space Agent index](index.md) · [Agents alternatives](../alternatives.md)
