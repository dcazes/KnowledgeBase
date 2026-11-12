---
type: Comparison
title: Observability & Evals Alternatives
description: Comparison of LLM observability and evaluation tools — Langfuse, Ragas and promptfoo — and other notable options, with a guide to combining tracing, metrics and test suites.
resource: https://github.com/topics/llm-evaluation
tags: [observability, evals, comparison, alternatives]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langfuse
    resource: "https://github.com/langfuse/langfuse"
    title: "Langfuse"
    author: "site:github.com"
  - id: ragas
    resource: "https://github.com/vibrantlabsai/ragas"
    title: "Ragas"
    author: "site:github.com"
  - id: promptfoo
    resource: "https://github.com/promptfoo/promptfoo"
    title: "promptfoo"
    author: "site:github.com"
---

# Observability & Evals Alternatives

| | [Langfuse](langfuse/index.md) | [Ragas](ragas/index.md) | [promptfoo](promptfoo/index.md) |
|---|---|---|---|
| Role | Tracing platform + evals + prompts | Metric library (RAG, agents) | Test runner + red teaming |
| When | Continuously, in production | Offline, on datasets | Before release, in CI |
| Interface | Web app + SDKs (OTel) | Python | CLI + YAML |
| Licence | MIT (core) | Apache-2.0 | MIT |

Other tools: Arize Phoenix (OTel tracing + evals, open source), LangSmith (LangChain's platform), Pydantic Logfire, Helicone, Opik (Comet), Braintrust, DeepEval, Inspect AI (UK AISI), OpenAI Evals.

## Using them together

1. **Trace** everything with [Langfuse](langfuse/index.md) (or Phoenix/Logfire).
2. **Measure** RAG and agent quality with [Ragas](ragas/index.md) metrics on curated datasets.
3. **Gate** releases with [promptfoo](promptfoo/index.md) assertions and red-team scans in CI.
4. Feed production failures back into datasets and tests.

## Related

[LLM observability](../concepts/llm-observability.md) · [Evals](../concepts/evals.md) · [AI landscape](../landscape.md)
