---
type: Playbook
title: OpenConcho AI Integration
description: Using OpenConcho to inspect and debug what Honcho-backed agents remember — checking conclusions, comparing reasoning levels, and triggering consolidation.
resource: https://github.com/offendingcommit/openconcho
tags: [openconcho, integration, debugging, agent-memory]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openconcho-github
    resource: "https://github.com/offendingcommit/openconcho"
    title: "offendingcommit/openconcho on GitHub"
    author: "site:github.com"
---

# OpenConcho — AI Integration

OpenConcho does not call models itself beyond Honcho's chat endpoint; its value is **visibility** into memory used by agents such as [Hermes](../../agents/hermes/index.md), [OpenClaw](../../agents/openclaw/index.md), [Claude Code](../../agents/claude-code/index.md) or your own app through [Honcho](../honcho/index.md).

## Debugging workflows

* **"Why did the agent assume that?"** — search conclusions for the claim and follow it to the source session.
* **Tuning reasoning depth** — run the same question in the dialectic playground at every level and compare cost and quality.
* **After bulk imports** — trigger a dream pass and watch consolidation in the dream viewer.
* **Shared memory across agents** — confirm two agents pointed at one workspace see the same peer representation.

This complements trace-level tools like [Langfuse](../../observability/langfuse/index.md): Langfuse shows the calls, OpenConcho shows the resulting memory. See [LLM observability](../../concepts/llm-observability.md).

## Related

[OpenConcho index](index.md) · [Honcho AI integration](../honcho/ai-integration.md)
