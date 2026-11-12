---
type: Software
title: Ragas
description: Open-source evaluation toolkit for LLM applications, best known for reference-free RAG metrics (faithfulness, answer relevancy, context precision and recall), plus agent and tool-use metrics, synthetic test-set generation and experiment tracking.
resource: https://github.com/vibrantlabsai/ragas
tags: [ragas, evals, rag, metrics, python]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ragas-github
    resource: "https://github.com/vibrantlabsai/ragas"
    title: "vibrantlabsai/ragas on GitHub"
    author: "site:github.com"
  - id: ragas-docs
    resource: "https://docs.ragas.io"
    title: "Ragas documentation"
    author: "site:docs.ragas.io"
  - id: ragas-paper
    resource: "https://arxiv.org/abs/2309.15217"
    title: "RAGAS: Automated Evaluation of Retrieval Augmented Generation"
    author: "Es et al., arXiv 2309.15217"
---

# Ragas

**Ragas** answers "is my RAG pipeline any good?" with metrics an LLM judge can compute without hand-written answers for every question: does the answer stick to the retrieved context, did retrieval find the right passages, is the answer relevant? It has grown into a general [evals](../../concepts/evals.md) toolkit with test-set generation.

| | |
|---|---|
| Category | [Evals](../../concepts/evals.md) |
| License | Apache-2.0 |
| Language | Python (`ragas`) |
| Latest release | v0.4.3 (2026-01-13); repository moved to `vibrantlabsai/ragas` |
| Paper | arXiv 2309.15217 |

## Contents

* [Overview](overview.md) — metrics and how they work
* [Installation](installation.md)
* [Snippets](snippets.md) — evaluating a RAG sample, test-set generation
* [AI Integration](ai-integration.md) — with LightRAG, Langfuse, frameworks

## Related

* Concepts: [Evals](../../concepts/evals.md) · [RAG](../../concepts/rag.md)
* Peers: [promptfoo](../promptfoo/index.md), [Langfuse](../langfuse/index.md)
* Comparison: [Observability alternatives](../alternatives.md)
