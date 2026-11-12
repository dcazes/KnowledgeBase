---
type: Concept
title: Letta Overview
description: How Letta agents remember and improve — the MemGPT idea of an LLM managing its own context, memory blocks, git-backed MemFS, message search, and sleep-time compute (dreaming).
resource: https://docs.letta.com/letta-code/memory
tags: [letta, overview, memgpt, memory-blocks, sleep-time-compute]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: letta-docs
    resource: "https://docs.letta.com"
    title: "Letta documentation"
    author: "site:docs.letta.com"
  - id: memgpt-paper
    resource: "https://arxiv.org/abs/2310.08560"
    title: "MemGPT: Towards LLMs as Operating Systems"
    author: "Packer et al., arXiv 2310.08560"
  - id: sleeptime-paper
    resource: "https://arxiv.org/abs/2504.13171"
    title: "Sleep-time Compute: Beyond Inference Scaling at Test-time"
    author: "Lin et al., arXiv 2504.13171"
---

# Letta — Overview

## From MemGPT to Letta Code

The 2023 **MemGPT** paper treated the context window like RAM in an operating system: the LLM pages information in and out of a larger external store using tools. The company Letta grew out of that work and first shipped it as an API server (Letta V1). In 2026 development moved to **Letta Code**, a harness that runs agents locally or on remote machines while their state lives locally or in Letta Cloud.

## How memory works

* **Memory blocks.** Labelled sections of the system prompt (for example `persona`, `human`, project notes) that the agent can edit with tools. Because they are always in context, they act as the agent's working self-knowledge — *system prompt learning*.
* **MemFS.** All context, including memory blocks and agent-scoped skills, is tracked in git. You can sync it to your own repository (`/memory-repository set git@github.com:...`) and review how the agent changed itself over time.
* **Message search.** Agents can search their own and other agents' past conversations (`/search`), giving recall beyond what fits in context.
* **Dreaming (sleep-time compute).** Between interactions the agent reflects on recent experience and reorganises memory (`/dream`, `/reflect`, `/sleeptime`). Based on Letta's sleep-time compute research (arXiv 2504.13171).

This is [agent memory](../../concepts/agent-memory.md) controlled by the agent rather than by an external pipeline — a strong form of [context engineering](../../concepts/context-engineering.md).

## Beyond memory

* [Skills](../../concepts/agent-skills.md) at global (`~/.letta`), project (`.agents/skills`) and agent scope.
* Subagents (general-purpose, forked, recall) and agent-to-agent calls — see [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md).
* Hooks, permission modes, cron schedules and heartbeats for always-on agents.
* Channels: CLI, browser and mobile (chat.letta.com), Slack, Telegram, Discord, custom channels.

## Trade-offs

* Self-editing memory is powerful but less predictable than an external fact store; review MemFS history.
* Several features (remote computers, secrets) require a Letta account.
* The old AgentFile (`.af`) import/export is removed from Letta Code.

## Related

[Letta index](index.md) · [AI Integration](ai-integration.md) · [Agent memory](../../concepts/agent-memory.md)
