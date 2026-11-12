---
type: Reference
title: Hermes Agent Configuration
description: Configuring Hermes — choosing providers and models, enabling toolsets, messaging gateway setup, command approval, DM pairing and container isolation.
resource: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
tags: [hermes, configuration, security, providers]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hermes-docs
    resource: "https://hermes-agent.nousresearch.com/docs/"
    title: "Hermes Agent documentation"
    author: "site:hermes-agent.nousresearch.com"
---

# Hermes Agent — Configuration

```bash
hermes model                 # choose provider and model
hermes tools                 # enable / disable toolsets
hermes config set <key> <value>
hermes config get <key>
hermes gateway setup         # connect Telegram, Discord, Slack, WhatsApp, Signal, email
```

## Models

Any provider: Nous Portal, OpenRouter, OpenAI, Anthropic, or a custom [OpenAI-compatible](../../concepts/openai-compatible-api.md) endpoint such as [Ollama](../../runtime/ollama/index.md), [vLLM](../../runtime/vllm/index.md) or a [LiteLLM](../../runtime/litellm/index.md) gateway. Switch mid-conversation with `/model provider:model`.

## Security settings

* **Command approval** — terminal commands need approval unless they match an allowlist.
* **DM pairing** — unknown senders on messaging platforms must be approved.
* **Container isolation** — run terminal tools in Docker or another backend rather than on the host.

An agent with a shell and a public chat interface is a high-value target; keep approval on and isolate execution. See [Agent security](../../concepts/agent-security.md).

## Related

[Hermes index](index.md) · [Snippets](snippets.md)
