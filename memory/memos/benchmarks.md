---
type: Software
title: MemOS — Benchmarks
description: MemOS scores on OmniMemEval (LoCoMo 88.83, LongMemEval 89.20, BEAM-10M 56.75) vs Mem0/Graphiti/EverOS; small-model behavior unverified; model-routing is the mitigation.
resource: https://github.com/MemTensor/MemOS
tags: [memos, benchmarks, locomo, longmemeval, omnmemeval, small-models, comparison]
generated: { by: "human:daniel", at: "2026-07-15T14:34:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-15T14:34:00Z" } ]
status: stable
stale_after: 2027-01-11
sources:
  - id: memos-github-benchmark-table
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemOS GitHub (benchmark table)"
    author: "site:github.com"
  - id: omnimemeval
    resource: "https://github.com/MemTensor/OmniMemEval"
    title: "OmniMemEval"
    author: "site:github.com"
  - id: hypermem-acl-2026
    resource: "https://github.com/EverMind-AI/HyperMem"
    title: "HyperMem (ACL 2026)"
    author: "site:github.com"
  - id: everos
    resource: "https://github.com/EverMind-AI/EverOS"
    title: "EverOS"
    author: "site:github.com"
---

# Published scores (OmniMemEval, per MemOS README)

Evaluated against mainstream commercial memory products across 5 user-memory and 5 agent-memory tasks.

| Benchmark | MemOS score |
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

News (README, 2026-07-02): with MemOS, OpenClaw improved average task completion from 36.63% → 50.87% across five agent tasks; MemOS leads OmniMemEval (14 commercial products, 10 datasets).

# Small-model caveat — UNVERIFIED

These numbers were measured with **large** models. No published small-model (8B–100B) benchmark exists for MemOS as of 2026-07-15. The extraction/consolidation step degrades on small LLMs; mitigation is **model routing** (see [Configuration](configuration.md)): big local LLM for write-path, 4B local embed/rerank for retrieval. Confirm by running a benchmark (EverMemBench / OmniMemEval) locally before trusting 8B extraction.

# Comparison vs other memory systems in this KB

| System | Paradigm | Graph | Vector | Small-model proof | Local-first |
|---|---|---|---|---|---|
| **MemOS** | Memory OS (MemCube) | ✅ Neo4j | ✅ Qdrant | ❌ unverified | ✅ (local plugin) |
| **Mem0** | flat vector+LLM | ❌ | ✅ | ❌ (typed objects help) | ✅ |
| **Graphiti** | temporal graph (Zep) | ✅ | ❌ | ❌ | ✅ |
| **EverOS** | engram lifecycle, Markdown-first | ❌ (optional HyperMem) | ✅ LanceDB | ❌ explicit (4B embed/rerank in HyperMem) | ✅ |
| **HyperMem** | hypergraph (topic→episode→fact) | ✅ hyperedges | ✅ (BM25+dense) | ✅ (Qwen3-Embedding-4B / Reranker-4B) | ✅ |

Note: HyperMem (ACL 2026) reports **LoCoMo 92.73%**, beating MemOS's 88.83 and Mem0's 75.80 — and does so on 4B embed/rerank models. Relevant if small-model retrieval quality becomes the binding constraint.
