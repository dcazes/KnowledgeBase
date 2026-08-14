---
type: Reference
title: Philosophy
description: Design philosophy of this self-hosted AI stack — principles (local-first, agent-centric memory, standards adherence), reading guide, and cross-cutting ideas behind the kbv2 stack docs.
resource: ../../index.md
tags: [philosophy, principles, meta, design]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: okf-specification
    resource: "../../AGENTS.md"
    title: "OKF specification"
---

# Philosophy

This folder captures the **design thinking** behind the stack documented in this vault: not how a tool works, but *why the stack is shaped the way it is*.

> **Seed status** — 2026-08-13: this is an intentionally small seed (index + principles + reading guide). Expand it as decisions get made.

## Contents

* [Principles](principles.md) — the operating principles the stack follows
* [Reading Guide](reading-guide.md) — how to navigate the vault's documentation

## Stack at a glance

36 programs / 297 docs (see [index](../../index.md)): self-hosted AI agents ([Hermes](../../agents/hermes/index.md), [OpenCode](../../agents/opencode/index.md), [OpenClaw](../../agents/openclaw/index.md)), memory backends ([MemOS](../../memory/memos/index.md), [mem0](../../memory/mem0/index.md), [honcho](../../memory/honcho/index.md), [LightRAG](../../memory/lightrag/index.md), [cognee](../../memory/cognee/index.md)), search/retrieval ([SearXNG](../../runtime/searxng/index.md), [Firecrawl](../../browsers/firecrawl/index.md), Vespa/Weaviate), model routing ([LiteLLM](../../agents/agent-stack/index.md)), local models ([Ollama](../../runtime/ollama/index.md)), and the not-deployed [Agent Stack](../../agents/agent-stack/index.md) compose prototype.
