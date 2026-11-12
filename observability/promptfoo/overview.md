---
type: Concept
title: promptfoo Overview
description: promptfoo's model — prompts, providers and test cases with assertions (deterministic, similarity, LLM-rubric), matrix comparisons and caching; red-team plugins and strategies; and pull-request code scanning for LLM security issues.
resource: https://www.promptfoo.dev/docs/
tags: [promptfoo, overview, assertions, red-teaming]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: promptfoo-docs
    resource: "https://www.promptfoo.dev/docs/"
    title: "promptfoo documentation"
    author: "site:promptfoo.dev"
---

# promptfoo — Overview

## Evals

A config lists **prompts**, **providers** (models, HTTP endpoints, scripts, agents) and **tests** (variables + assertions). promptfoo runs the full matrix and caches results.

| Assertion type | Examples |
|---|---|
| Deterministic | `contains`, `equals`, `regex`, `is-json`, JSON Schema, `javascript`/`python` functions |
| Semantic | `similar` (embedding similarity) |
| Model-graded | `llm-rubric`, `factuality`, `context-faithfulness`, `answer-relevance` |
| Operational | `latency`, `cost` |

## Red teaming

`promptfoo redteam` generates attacks from **plugins** (harm categories, PII, prompt injection, excessive agency, RBAC bypass…) and **strategies** (jailbreak iterations, encodings, multi-turn) against your app, then produces a vulnerability report — practical [agent security](../../concepts/agent-security.md) testing.

## Code scanning

Reviews pull requests for LLM-related security and compliance issues.

## Related

[promptfoo index](index.md) · [Snippets](snippets.md)
