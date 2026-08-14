---
type: Concept
title: Philosophy — Principles
description: The operating principles of this self-hosted AI stack — local-first, agent-centric memory, standards adherence, documented reality, layered tooling.
resource: ../../index.md
tags: [philosophy, principles]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: okf-specification
    resource: "../../AGENTS.md"
    title: "OKF specification"
---

# Principles

The decisions in this stack reduce to a handful of recurring principles.

## 1. Local-first & private

* Everything self-hosted on this machine — no cloud dependencies for core function.
* Local models available via [Ollama](../../runtime/ollama/index.md); secrets stay in `programs/*/secrets.md` (never documented).
* Tools that can run offline (SearXNG, Ollama, Vespa) are preferred where they fit.

## 2. Agent-centric memory

* Memory is a first-class citizen, not an afterthought: [MemOS](../../memory/memos/index.md), [mem0](../../memory/mem0/index.md), [honcho](../../memory/honcho/index.md), [LightRAG](../../memory/lightrag/index.md), [cognee](../../memory/cognee/index.md), [supermemory](../../memory/supermemory/index.md).
* Different memory shapes for different jobs (graph, vector, key-value, agentic memory) — see [Architecture → Memory](../architecture/memory/memory-comparison.md).

## 3. Standards & verification over vibes

* Docs follow the OKF v0.2 (trust-signals subset) format with `verified`/`stale_after` frontmatter.
* Facts distinguish **live state** ("currently running") from **config-derived** ("from config, not live state") — no assumptions.
* Ports/versions are verified against actual checkouts in `programs/`, not remembered.

## 4. Layered tooling, not monoliths

* Each tool does one job well; compose them (LiteLLM routes models, SearXNG searches, Firecrawl scrapes, Hermes delegates).
* The [Agent Stack](../../agents/agent-stack/index.md) is the (not-deployed) composition prototype of this idea.

## 5. Document reality, flag gaps

* Undocumented tools get docs **from upstream** when local data is absent (e.g. [Space Agent](../../agents/spaceagent/index.md), [PydanticAI](../../agents/pydanticAI/index.md)).
* Empty/placeholder state is stated honestly, never papered over.
