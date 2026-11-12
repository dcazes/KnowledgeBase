---
type: Concept
title: Ragas Overview
description: Ragas metrics explained — faithfulness, response relevancy, context precision, context recall, noise sensitivity, factual correctness, agent goal accuracy and tool-call accuracy — and the limits of LLM-as-judge evaluation.
resource: https://docs.ragas.io
tags: [ragas, overview, metrics, llm-as-judge]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ragas-docs
    resource: "https://docs.ragas.io"
    title: "Ragas documentation"
    author: "site:docs.ragas.io"
  - id: ragas-paper
    resource: "https://arxiv.org/abs/2309.15217"
    title: "RAGAS: Automated Evaluation of Retrieval Augmented Generation"
    author: "Es et al., arXiv 2309.15217"
---

# Ragas — Overview

| Metric | Question it answers | Needs reference? |
|---|---|---|
| Faithfulness | Are the answer's claims supported by the retrieved context? | No |
| Response relevancy | Does the answer address the question? | No |
| Context precision | Are relevant chunks ranked high? | Optional |
| Context recall | Did retrieval find everything the reference answer needs? | Yes |
| Noise sensitivity | Does irrelevant context mislead the answer? | Yes |
| Factual correctness | Does the answer match the reference facts? | Yes |
| Agent goal accuracy, tool-call accuracy | Did an agent achieve the goal / call the right tools? | Yes |

Metrics decompose answers into claims and ask a judge LLM to verify each, which is why they work without full references.

## Caveats

LLM judges have biases and variance: use a strong judge model, check a sample by hand, and track metrics over time rather than trusting single scores. See [Evals](../../concepts/evals.md).

## Related

[Ragas index](index.md) · [Snippets](snippets.md)
