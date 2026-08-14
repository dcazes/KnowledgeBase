---
type: Software
title: MemOS — Configuration
description: MemOS .env model routing (LLM to largest local model via LiteLLM :4000; embeddings/rerank to 4B local models) and MemCube scoping/feedback controls — the small-model survival plan.
resource: https://github.com/MemTensor/MemOS
tags: [memos, configuration, model-routing, llm, embedding, small-models, cubes, feedback]
generated: { by: "human:daniel", at: "2026-07-15T14:32:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-15T14:32:00Z" } ]
status: stable
stale_after: 2027-01-11
sources:
  - id: memos-github
    resource: "https://github.com/MemTensor/MemOS"
    title: "MemOS GitHub"
    author: "site:github.com"
  - id: hypermem-acl-2026-4b-embed-rerank
    resource: "https://github.com/EverMind-AI/HyperMem"
    title: "HyperMem (ACL 2026, 4B embed/rerank)"
    author: "site:github.com"
  - id: memory-poisoning-writeup-mem0
    resource: "https://mem0.ai/blog/memory-poisoning-how-bad-inputs-corrupt-your-ai-agent-s-memory"
    title: "Memory poisoning writeup (Mem0)"
    author: "site:mem0.ai"
---

# MemOS — The small-model problem

MemOS's published benchmarks (LoCoMo 88.83, LongMemEval 89.20 — OmniMemEval) were measured with large models. Memory quality is gated by the **LLM doing extraction / consolidation / retrieval-planning** — the step most likely to degrade on an 8B model. The mitigation is **model routing by role**, not a different system.

# Model routing (recommended for this machine)

| Role | Assign to | Why |
|---|---|---|
| Generation / extraction (fragile) | **Largest local model** via LiteLLM `:4000` (e.g. Qwen3-235B MoE active ~22B, or 70B dense) | extraction quality needs the strongest model you run |
| Embedding | **4B local** (Qwen3-Embedding-4B / BGE-M3) | cheap, no large model needed |
| Rerank | **4B local** (Qwen3-Reranker-4B) | cheap, runs locally |

This mirrors what sibling project **HyperMem** (EverMind, ACL 2026) proves: retrieval quality is strong on 4B embed/rerank models while generation uses a larger model.

```dotenv
# .env (Path A) — point generation at local LiteLLM, embed/rerank at 4B local
LLM_BASE_URL=http://localhost:4000/v1
LLM_API_KEY=not-needed-local
EMBEDDING_BASE_URL=http://localhost:PORT/v1   # your 4B embedder
RERANK_BASE_URL=http://localhost:PORT/v1      # your 4B reranker
```

> VERIFY: exact env var names are from README's described shape; confirm against `docker/.env.example` after clone. The *routing strategy* (big LLM for extract, small for embed/rerank) is the durable principle regardless of key names.

# MemCube scoping (anti-junk / multi-user safety)

MemOS organizes memory into **cubes** with owner scoping. Use this to avoid the "memory poisoning" failure modes (bad input stored as truth):

* **Per-user cubes** — isolate each agent/user's memory; default retrieval scoped to that cube.
* **Shared / global cubes** — promote only after review; require higher trust.
* **Feedback / correction API** — natural-language overrides ("correct / supplement / replace") let you fix bad recalls without manual DB edits.

# Write-path policy (keep junk out)

1. Extract only **stable facts / preferences / confirmed corrections** — not speculative output.
2. Tag `source` (`human` vs `agent` vs `tool`) so retrieval can exclude `agent`-generated facts from safety-sensitive flows.
3. Let the system consolidate; you govern at the edges (review shared cubes, run a benchmark periodically).
