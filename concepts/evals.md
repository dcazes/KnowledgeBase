---
type: Concept
title: Evals
description: Evaluating LLM applications and agents — offline datasets and online monitoring, deterministic checks, LLM-as-judge and human review, RAG metrics, agent trajectory evaluation, red teaming, public benchmarks and their pitfalls, and the eval tools in this vault.
resource: https://docs.ragas.io
tags: [concept, evals, llm-as-judge, benchmarks, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ragas
    resource: "https://docs.ragas.io"
    title: "Ragas documentation"
    author: "site:docs.ragas.io"
  - id: promptfoo
    resource: "https://www.promptfoo.dev/docs/"
    title: "promptfoo documentation"
    author: "site:promptfoo.dev"
---

# Evals

LLM systems are probabilistic and change whenever you touch a prompt, model or retrieval setting. **Evals** are the tests that tell you whether a change made things better or worse.

## Kinds

| Kind | What | Tools |
|---|---|---|
| Deterministic checks | Contains, regex, JSON schema, latency, cost | [promptfoo](../observability/promptfoo/index.md) |
| LLM-as-judge | Rubrics, faithfulness, relevance | [Ragas](../observability/ragas/index.md), promptfoo, [Langfuse](../observability/langfuse/index.md) evaluators |
| RAG metrics | Context precision/recall, faithfulness | [Ragas](../observability/ragas/overview.md) |
| Agent / trajectory | Right tools, right order, goal achieved | Ragas agent metrics, Pydantic Evals, LangSmith |
| Human review | Annotation queues, thumbs feedback | Langfuse, [Open WebUI](../apps/openwebui/features.md) |
| Red teaming | Adversarial inputs: injection, jailbreaks, leaks | [promptfoo redteam](../observability/promptfoo/overview.md) |

## Offline and online

* **Offline:** fixed datasets run in CI before release.
* **Online:** score sampled production traces; turn failures into new dataset items.

## Public benchmarks

SWE-bench and Terminal-Bench (coding agents), Aider polyglot ([Aider](../agents/aider/overview.md)), LoCoMo and LongMemEval ([agent memory](agent-memory.md)), MTEB ([embeddings](embeddings.md)). Useful for shortlisting, but vendor-reported numbers often differ in model, budget and judge — see [MemOS benchmarks](../memory/memos/benchmarks.md). Always test on your own data.

## Related

[LLM observability](llm-observability.md) · [Observability alternatives](../observability/alternatives.md) · [Concepts index](index.md)
