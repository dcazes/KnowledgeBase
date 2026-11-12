---
type: Concept
title: MemOS Overview
description: MemOS concepts — the memory-OS framing, memory cubes for isolation and sharing, graph-structured multi-modal memory, the asynchronous MemScheduler, natural-language feedback and correction, and the local plugin's trace-policy-world-model-skill tiers.
resource: https://memos-docs.openmem.net
tags: [memos, overview, memory-cubes, scheduler]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: memos-github
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemTensor/MemOS on GitHub"
    author: "site:github.com"
  - id: memos-paper
    resource: "https://arxiv.org/abs/2507.03724"
    title: "MemOS: A Memory OS for AI System"
    author: "Li et al., arXiv 2507.03724"
---

# MemOS — Overview

## Memory as an OS resource

The MemOS paper (arXiv 2507.03724) argues that LLM memory should be scheduled, versioned and governed like memory in an operating system. In practice MemOS offers:

* **A unified memory API** — add, retrieve, edit, delete — over memories stored as a graph you can inspect and edit, not an opaque embedding store.
* **Multi-modal memory** — text, images, tool traces and personas retrieved together.
* **Memory cubes** — composable knowledge bases. Each cube can belong to a user, project or agent; agents read from some cubes and write to others, which gives isolation and controlled sharing in multi-agent setups.
* **MemScheduler** — asynchronous ingestion so writes do not block the conversation, built for high concurrency.
* **Feedback and correction** — natural-language feedback corrects, supplements or replaces existing memories.

## The local plugin's tiers

The `memos-local-plugin` 2.0 for [Hermes](../../agents/hermes/index.md) and [OpenClaw](../../agents/openclaw/index.md) organises self-evolving memory into **L1 traces** (raw experience), **L2 policies**, **L3 world models** and crystallised **[skills](../../concepts/agent-skills.md)**, stored locally with hybrid retrieval (SQLite FTS5 + vectors), deduplication and multi-agent collaboration.

## How it compares

MemOS is closer to [Hindsight](../hindsight/index.md) and [Letta](../letta/index.md) (memory that learns and becomes skills) than to [Mem0](../mem0/index.md)'s flat fact store. The cube model is its most distinctive idea for multi-tenant and multi-agent use.

## Related

[MemOS index](index.md) · [Benchmarks](benchmarks.md) · [Agent memory](../../concepts/agent-memory.md)
