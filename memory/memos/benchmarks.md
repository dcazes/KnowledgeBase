---
type: Reference
title: MemOS Benchmarks
description: MemOS's self-reported OmniMemEval results across user-memory and agent-memory tasks (LoCoMo, LongMemEval, PersonaMem, HaluMem, BEAM, SWE-Bench and more), and how to read vendor memory benchmarks.
resource: https://github.com/MemTensor/OmniMemEval
tags: [memos, benchmarks, evals, locomo, longmemeval]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: memos-github
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemTensor/MemOS on GitHub"
    author: "site:github.com"
  - id: omnimemeval
    resource: "https://github.com/MemTensor/OmniMemEval"
    title: "OmniMemEval benchmark suite"
    author: "site:github.com"
---

# MemOS — Benchmarks

MemOS reports these results via its own **OmniMemEval** suite (5 user-memory + 5 agent-memory tasks):

| Benchmark | Score |
|---|---|
| LoCoMo | 88.83 |
| LongMemEval | 89.20 |
| PersonaMem v2 | 40.58 |
| HaluMem | 80.91 |
| BEAM-10M | 56.75 |
| GDPVal | 62.07 |
| LiveCodeBench | 64.96 |
| OmniMath | 61.00 |
| SWE-Bench | 38.46 |
| BrowseComp-Plus | 23.85 |

It also reports OpenClaw's average task completion rising from 36.63% to 50.87% across five agent tasks when MemOS is attached.

## Reading memory benchmarks

Nearly every memory vendor claims #1 on LoCoMo or LongMemEval — [Mem0](../mem0/overview.md), [Supermemory](../supermemory/index.md), [Hindsight](../hindsight/index.md), [Honcho](../honcho/index.md), [Graphify](../graphify/overview.md). Before comparing numbers, check:

* **Same answering model?** Scores move a lot with the LLM used to answer.
* **Same retrieval budget?** More retrieved tokens usually means higher accuracy.
* **Same judge?** Most use an LLM judge; prompts differ.
* **Platform vs open source?** Some numbers come from hosted products with extra features.

Run your own evaluation on your own data where it matters — see [Evals](../../concepts/evals.md).

## Related

[MemOS index](index.md) · [Memory alternatives](../alternatives.md)
