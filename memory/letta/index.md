---
type: Software
title: Letta
description: Stateful agent harness from the creators of MemGPT — agents with self-edited memory blocks, git-tracked context (MemFS), sleep-time 'dreaming', skills, subagents and messaging channels. Ships as Letta Code (CLI + App Server) and Letta Cloud.
resource: https://www.letta.com
tags: [letta, memgpt, agent-memory, stateful-agents, memory-blocks, typescript]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: letta-code-github
    resource: "https://github.com/letta-ai/letta-code"
    title: "letta-ai/letta-code on GitHub"
    author: "site:github.com"
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
  - id: letta-archive
    resource: "https://github.com/letta-ai/letta"
    title: "letta-ai/letta (archived V1 server)"
    author: "site:github.com"
---

# Letta

**Letta** (formerly **MemGPT**) builds agents that keep identity and memory over long horizons and improve by **rewriting their own context**. Where [Mem0](../mem0/index.md) or [Zep](../zep/index.md) are memory services an application calls, Letta is a full agent harness in which the agent itself decides what to remember.

| | |
|---|---|
| Category | [Agent memory](../../concepts/agent-memory.md) · [Agent frameworks](../../concepts/agent-frameworks.md) |
| License | Apache-2.0 |
| Current product | **Letta Code** (`@letta-ai/letta-code` on npm, `letta` on PyPI) — v0.34.56 (2026-11-12) |
| Deployment | Local CLI and App Server · Letta Cloud (hosted agent state) · chat.letta.com |
| Legacy | The Letta V1 API server (`letta-ai/letta`, last release 0.16.8) is retired; its code is on the `archive` branch |

## Contents

* [Overview](overview.md) — memory blocks, MemFS, dreaming, the MemGPT lineage
* [Installation](installation.md) — npm / uv / pipx, cloud vs local backend, App Server
* [Snippets](snippets.md) — CLI commands, skills, remote computers, headless mode
* [AI Integration](ai-integration.md) — skills ecosystem, subagents, channels, when to choose Letta

## Related

* Concepts: [Agent memory](../../concepts/agent-memory.md) · [Context engineering](../../concepts/context-engineering.md) · [Agent skills](../../concepts/agent-skills.md) · [Coding agents](../../concepts/coding-agents.md)
* Peers: [Mem0](../mem0/index.md), [Zep](../zep/index.md), [Honcho](../honcho/index.md), [Hindsight](../hindsight/index.md), [MemOS](../memos/index.md); agent harnesses [Hermes](../../agents/hermes/index.md), [OpenClaw](../../agents/openclaw/index.md), [Claude Code](../../agents/claude-code/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
